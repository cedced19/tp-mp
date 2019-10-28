type reservation = (int*int*int) list;;

let rec selection (l: reservation) (t: int) = match l with
  [] -> []
  | (i,d,f)::q -> if (d<t) then
                    (selection q t)
                  else 
                    (i,d,f)::(selection q t);;

let rec choix (l: reservation) = match l with
  [] -> []
  | (i,d,f)::q -> (i,d,f)::(choix (selection q f));;


let rec une_passe (l: reservation) = match l with
  |[] -> false,[]
  |[x] -> false,[x]
  |(i,d,f)::reste -> let boolean,res=(une_passe reste) in 
              let (_,_,x) = (List.hd res) in
              if f<=x then 
                boolean,(i,d,f)::res 
              else 
                true,(List.hd res)::(i,d,f)::(List.tl res);;

let rec tribulle (l: reservation) = match l with
  |[] -> []
  |l -> let (modifiee,liste)=une_passe l in 
        if modifiee then 
          (List.hd liste)::tribulle(List.tl liste) 
        else liste;;

(* Valeur de test: let l = [(1,1,8);(2,2,5);(3,4,7);(4,1,3);(5,5,9);(6,8,11);(7,9,10);(8,13,16);(9,11,14)];;*)

let choix l =
  let rec choix_aux l t = match l with
    [] -> []
    |(i,d,f)::q -> if d<t then 
                    choix_aux q t
                  else 
                    (i,d,f)::(choix_aux q f)
  in choix_aux l 0;;

let rechmax arr d =
  let k=ref (d-1) in
  while !k>=0 && arr.(!k) <> -1 do 
    decr k 
  done;
  !k ;;

let affecter taches =
  let n=Array.length taches in
  let r=Array.make n (-1) in
  let penalite=ref 0 in

  for i=0 to n-1 do
    let (d,w) = taches.(i) in
    let k = rechmax r d in
    if (k>=0) then
      r.(k)<-i
    else
      begin
        r.(rechmax r n) <-i;
        penalite:=!penalite+w
      end;
  done;
  !penalite;;

(* Valeur de test: let l = [|(4, 7); (2, 6); (4, 5); (3, 4); (1, 3); (4, 2); (6, 1)|];;*)

let stations d a r =
  let n = Array.length d in
  let arrets = Array.make (n+1) false in
  arrets.(0)<-true
  let p = ref 0 in (* position de la voiture *)
  let i = ref 0 in (* dernière station *)
  while !p+r<a do 
    let t=ref 0 in (* distance depuis le dernier plein *)
    while !i<n & !t+d.(!i)<=r do
      t:= !t+d.(!i);
      p:= !p+d.(!i);
      incr i
    done;
    arrets.(!i) <- true
  done;
  arrets;;


let stations_euro e d a l k =
  let n = Array.length d in
  let arrets = Array.make (n+1) 0 in (* tableau contenant le nombre de litre acheté à chaque station *)
  let p = ref 0 in (* position de la voiture *)
  let i = ref 0 in (* station atteinte *)
  let r = ref 0 in (* contenu du réservoir actuel *)
  while !i<=n do
    let j=ref (!i+1) in
    let dist=ref 0 in
    (* On recherche une station moins chère *)
    while !j<=n && e.(!j)>e.(!i) && k*(!dist+d.(!j-1))<=l do
      dist:=!dist+d.(!j-1);
      incr j;
    done;
    if !j=n+1 then (* Il n'y a pas de solution *)
      begin
        if (a-(!p))*k <= l then (* On peut finir: on prend le minimum *)
          begin
            arrets.(!i) <- (a-(!p))*k-(!r)
          end
        else (* On prend le maximum *)
          begin
            arrets.(!i) <- l-(!r);
            p:=!p+d.(!i);
            r:=!r-k*d.(!i);
            incr i;
          end
      end
    else (* Il y a une solution *)
      begin
        dist:=!dist+d.(!j-1);
        p:=!p+(!dist);
        arrets.(!i) <- max (!dist*k-(!r)) 0;
        r:=!r-k*(!dist)+arrets.(!i);
        i:=!j
      end;
  done;
  arrets;;


(* Valeur de test: 
let d=[|12;30;16;20|];;
let e=[|15;11;13;15;10|];;
let a =100;;
let k=1;;
let l=80;;
*)


(* Faire "coloriage des sommets d'un graphe" et "le voyageur de commerce" une fois le chapitre en question fait *)