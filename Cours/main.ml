
(*Question pour blaireau*)
let rec pivot l x = match l with
  | [] -> [], []
  | r::q -> let l1,l2 = pivot q x in
            if (r <= x) then 
              r::l1,l2
            else 
              l1, r::l2;;

let rec  quicksort l = 
  | [] -> []
  | t::q -> let l1, l2 = quicksort q t in
            (quicksort l1)@(t::(quicksort l2));;


(* exo 3 *)            
let rec minimum f lambda = match f with
 [i]->([],i)
 |(i::q)-> let (r,j)=minimum q lambda in 
           if (lambda.(i)<=lambda(j)) then
            (q,i)
           else
            (i::r,q)

let rec creerfile n = match n with
  | 0 -> []
  | n -> (n-1)::creerfile (n-1);;

let rec creerfile n = 
  let rec creerfile_aux k accu = match k with
  | 0 -> accu
  | k -> creerfile_aux (k-1) ((k-1)::accu) in
creerfile_aux n [];;


let dijkstra g s =
  let n = Array.length g in
  let lambda = Array.make n max_int in

  let rec relacher l x = match l with 
    | []->()
    | (y,p)::q->lambda.(y)<- min lambda(y) lambda(x+p)
                relacher q x in


  let rec etape f = match f with
    | [] -> lambda
    | _ -> let (newf,mini) = minimum f lambda in
           relache g.(mini) mini;
           etape newf 
  in
  
  etape (creerfile n);;