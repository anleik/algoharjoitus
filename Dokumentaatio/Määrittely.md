# Määrittelydokumentti  

Projektin dokumentaatio on suomeksi.  

Teen projektin Pythonilla.  

Opinto-ohjelmani on Tietojenkäsittelytieteen kandidaatti.  

Projektin ydin on luolastojen satunnainen generointi kaksiulotteisessa tasossa. Se saavutetaan toteuttamalla Delaunayn triangulaatio Bowyer-Watson algoritmilla. Huoneet voidaan yhdistää toisiinsa käyttämällä syvyyshakua.   

Projektia voi hyödyntää esimerkiksi generoimaan satunnaisia tasoja peliin.  

Bowyer-Watson toimii aikavaativuudella O(n<sup>2</sup>), N pisteen kolmiointiin. Optimoinnilla se voi toimia myös aikavaativuudella O(n log n), mutta ei välttämättä kaikissa tapauksissa.  

Ohjelma ei tarvitse syötettä, vaan se tuottaa määrittelyn kokoiseen kaksiulotteiseen tasoon sopivan luolaston.  

## Viitteet  
[Vazgriz - Procedurally Generated Dungeons](https://vazgriz.com/119/procedurally-generated-dungeons)  
[Tom Stephenson - Creating Simple Procedural Dungeon Generation](https://www.tomstephensondeveloper.co.uk/post/creating-simple-procedural-dungeon-generation)  
[Gorilla Sun - Bowyer-Watson Algorithm for Delaunay Triangulation](https://www.gorillasun.de/blog/bowyer-watson-algorithm-for-delaunay-triangulation/)  
[Wikipedia - Bowyer-Watson Algorithm](https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm)  
