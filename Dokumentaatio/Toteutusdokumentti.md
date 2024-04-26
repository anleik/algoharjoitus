# Toteutusdokumentti  

## Ohjelman rakenne  

Sovellus suorittaa Delaunayn triangulaation käyttäen Bowyer-Watsonin algoritmia satunnaisille pisteille sekä luo polun pisteiden läpi syvyyshakua käyttäen. Ohjelma sisältää funktiot näille algoritmeille sekä paljon apufunktioita tarkistamaan että syöte on oikeanlainen ja haluttu tulos on mahdollinen. Sitten ohjelma alustaa satunnaiset muuttujat ja avaa pygame-ikkunan visualisoimaan tuotettua tulosta. Tietyillä näppäimillä voi ohjelmassa uudelleengeneroida triangulaation, generoida huoneet ja/tai generoida polun huoneiden välille syvyyshaulla.  


## Aikavaativuus  

Boywer-Watsonin algoritmia on testattu erikokoisilla syötteillä. Algoritmi saavuttaa aikavaativuuden O(n<sup>2</sup>) missä n on pisteiden määrä. Esim. 100 pisteen triangulointi vie noin 0.03 sekuntia, 1000 pisteen triangulointi noin 3 sekuntia ja 10000 pisteen triangulointi noin 300 sekuntia eli aika kasvaa toisessa potenssissa syötteeseen nähden.  

![Sata]()  
![Tuhat]()  
![10Tuhat]()  

## Työn puutteita ja parannusehdotuksia  

Syvyyshakualgoritmin luonteen takia generoitu polku ei aina ole täydellinen 2d-tasossa eli polku voi mennä ristiin aiemman polun yli. Jatkokehityksessä tämän voisi toteuttaa 3d-tasossa niin että toinen polku menee toisen yli eivätkä polut törmää.  

## Laajojen kielimallien käyttö  

Työssä ei ole käytetty laajoja kielimalleja. *Huom. Joillain verkkosivuilla jotka sisältävät käyttäjien kysymyksia ja vastauksia, joskus tarjotaan laajan kielimallin generoima vastaus ja se voi jopa näkyä Google-hakusivulla ennen käyttäjien kirjoittamia vastauksia.*  

## Viitteet  
[Vazgriz - Procedurally Generated Dungeons](https://vazgriz.com/119/procedurally-generated-dungeons)  
[Tom Stephenson - Creating Simple Procedural Dungeon Generation](https://www.tomstephensondeveloper.co.uk/post/creating-simple-procedural-dungeon-generation)  
[Gorilla Sun - Bowyer-Watson Algorithm for Delaunay Triangulation](https://www.gorillasun.de/blog/bowyer-watson-algorithm-for-delaunay-triangulation/)  
[Wikipedia - Bowyer-Watson Algorithm](https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm)  
