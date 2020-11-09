
using namespace std;

int tabou_search(){


    return 0;
}



int main() 
{
    vector<Bloc> arr = {Bloc(10, 12, 32), {32, 10, 12}, Bloc(4, 6, 7), Bloc(4, 5, 6), Bloc(6, 4, 5), Bloc(1, 2, 3), Bloc(3, 1, 2)};
    int a = algo_dynamic(arr);
    cout<<a<<endl;

}
compteur = 0

// solution_globale = []
// solution_locale = []

//  while compteur < 100:
//     compteur ++
//  pour chaque candidat_tabou dans tabou:
//   decrementer candidat_tabou
//   si candidat_tabou.compteur == 0:
//    on remet candidat_tabou dans la liste de candidat
//    on enleve candidat_tabou
//     hauteur_meilleur_candidat = inf
//  heuteur_offerte_par_meilleur_candidat = null
//  position_meilleur_candidat = null
//  for candidat in candidats:
//   position = trouver_premiere_position_valide_from_top()
//   if position not null:
//     hauteur_courante = hauteu_solution_local + block_jessaie_dajouter.hauteur
//     for index in range(position, len(tour)):
//       si tour[i] pas compatible:
//        hauteur_courante -= tour[i].hauteur
//                 if hauteur_meilleur_candidat < hauteur_courante:
//      meilleur_candidat = candidat
//      position_meilleur_candidat = position
//   inserer_meilleur_candidat dans solution_local()

//  for index in range(position, nb_block_dans_solution):
//    si tour[index] par compatible avec candidat:
//        on lenleve
//        on lajoute dans tabou (avec compteur associé)

//  if solution_local > solution_gloable:
//   solution_globale = solution_locale
//   compteur = 0
