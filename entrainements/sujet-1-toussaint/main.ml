

type arbre =
  | F 
  | N of arbre * int * arbre;;

let rec recherche e a = match a with
  | F -> false
  | N(g,x,d) -> (x=e) || (recherche e g) || (recherche e d);;


let rec recherche2 e a = match a with
  | F -> false
  | N(g,x,d) when (x=e) -> true
  | N(g,x,d) when (e<x) -> (recherche e g) 
  | N(g,x,d) -> (recherche e d);;