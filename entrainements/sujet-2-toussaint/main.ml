

type litteral =
  | V of int (* variable *)
  | NV of int;; (* négation de variable *)

type clause = litteral list;;
type fnc = clause list;;

let rec var_max_clause c = match c with
  | [] -> failwith "clause vide"
  | [(NV x)] -> x
  | [(V x)] -> x
  | (V x)::q -> max x (var_max_clause q)
  | (NV x)::q −> max x (var_max_clause q);;

let rec var_max f = match f with
  | [] -> failwith "fnc vide"
  | [x] -> var_max_clause x
  | x::q -> max x (var_max_clause x) var_max f;;

type trileen =
  | Vrai
  | Faux
  | Indetermine;;

let non c = match c with
  | Vrai -> Faux
  | Faux -> Vrai
  | x -> x;;

let et a b = 
  if (a=Faux || b=Faux) then Faux
  else begin 
    if (a=Vrai && b=Vrai) then Vrai
    else Indetermine
  end;;

let ou a b =
  if (a=Vrai || b=Vrai) then Vrai
  else begin 
    if (a=Faux && b=Faux) then Vrai
    else Indetermine
  end;;


let rec evalclause c t = match c with
    | [] -> Faux (* élément neutre pour 'ou' *)
    | (V i)::q -> ou t.(i) (evalclause q t)
    | (NV i)::q -> ou (non t.(i)) (evalclause q t)

let rec eval f t = match f with
    | [] -> Vrai (* élément neutre pour 'et' *)
    | x::q -> et (evalclause x t) (eval q t)



let rec evalclause_paraisseux c t = match c with
    | [] -> Faux (* élément neutre pour 'ou' *)
    | (V i)::q -> if (t.(i)=Vrai) then Vrai else (evalclause_paraisseux q t)
    | (NV i)::q -> if ((non t.(i))=Vrai) then Vrai else (evalclause_paraisseux q t)

let rec eval_paraisseux f t = match f with
    | [] -> Vrai (* élément neutre pour 'et' *)
    | x::q -> let e = evalclause_paraisseux x t in
              if (e=Faux) then Faux else
              begin
                let ee = eval_paraisseux q t in
                  if (ee=Faux) then Faux else
                  if (ee=Vrai) then e else
                  Indetermine
              end;;


let k_stat f =
  let n = var_max f in
  let arr = Array.make (n+1) Indetermine in
  let rec test k =
    let b = eval f arr in
    if (b=Vrai) then true else
    if (b=Faux) then false else
    begin
      arr.(k) <- Vrai
      if ((test (k+1))) then true else
      begin
        arr.(k) <- False
        if ((test (k+1))) then true else 
        begin
          arr.(k) <- Indetermine
          false
        end
      end
    end
  in test 0;;

let k_stat_arr f =
  let n = var_max f in
  let arr = Array.make (n+1) Indetermine in
  let rec test k =
    let b = eval f arr in
    if (b=Vrai) then true else
    if (b=Faux) then false else
    begin
      arr.(k) <- Vrai
      if ((test (k+1))) then true else
      begin
        arr.(k) <- False
        if ((test (k+1))) then true else 
        begin
          arr.(k) <- Indetermine
          false
        end
      end
    end
  in test 0
  arr;;

let k_stat_rapide f =
  let n = var_max f in
  let arr = Array.make (n+1) Indetermine in
  let rec test k =
    let b = eval f arr in
    if (b=Vrai) then failwith "satisfiable" else
    if (b=Faux) then false else
    begin
      arr.(k) <- Vrai
      if ((test (k+1))) then failwith "satisfiable" else
      begin
        arr.(k) <- False
        if ((test (k+1))) then failwith "satisfiable" else 
        begin
          arr.(k) <- Indetermine
          false
        end
      end
    end
  in
  try test 0 ; false with Failure "satisfiable" -> true;;

let valide t j =
  let k = ref 0 in
  while !k < j && t.(!k) <> t.(j) && abs (t.(!k) - t.(j)) <> abs (!k - j) do
    incr k;
  done;
  !k = j;;

(* Condition selon la diagonale: abs (t.(!k) - t.(j)) <> abs (!k - j) 
  Condition selon la colonne: t.(!k) <> t.(j) *)

let n_reine n =
  let arr = Array.make n 0 in
  let rec explore i j =
    arr.(j) <- i
    if (valide arr j) then
    begin
      if (j = (n-1)) then true
      else if explore 0 (j+1) then true
      else if i < (n-1) then explore (i+1) j
      else false
    end
    else
      if (i < (n-1)) then explore (i+1) j
    else false
  in let r = explore 0 0
  in if r then arr else failwith "aucune sol";;

let n_reine_compteur n =
  let arr = Array.make n 0 in
  let c = ref 0 in
  let rec explore i j = 
    arr.(j) <- i;
    if (valide arr j) then
      begin
        if (j = (n-1)) then 
          begin
            incr c;
            if (i < (n-1)) then explore (i+1) j
          end;
        else 
          begin
            chercher (j+1) 0;
            if (i < (n-1)) then explore (i+1) j
          end;
      end;
    else
      if (i < (n-1)) then explore (i+1) j
  in explore 0 0;
  !c;;

let sans_fixe t j =
  let k = ref 0 in
  while !k < j && t.(!k) <> t.(j) do
    incr k;
  done;
  !k = j && t.(j) <> j;;

let n_reine_sans_fixe_compteur n =
  let arr = Array.make n 0 in
  let c = ref 0 in
  let rec explore i j =
    arr.(j) <- i;
    if (sans_fixe arr j) then
    begin
      if (j = (n-1)) then 
      begin
        incr c;
        if i < (n-1) then explore (i+1) j
      end
      else 
      begin
        chercher (j+1) 0;
        if i < (n-1) then explore (i+1) j
      end
    end
    else
      if (i < (n-1)) then explore (i+1) j
  in explore 0 0; !c;;