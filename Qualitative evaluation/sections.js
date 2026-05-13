const SECTIONS = [
  {
    "query": "Where was the wife of Douglas Leiterman born?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the birthplace of Douglas Leiterman's wife publicly available or documented in any reliable sources?"
      },
      {
        "method": "Iterative",
        "text": "What was the wife of Douglas Leiterman's profession?"
      }
    ]
  },
  {
    "query": "Which song was released earlier, 1990-Sick (Get 'Em All) or Who'S Laughing Now (Song)?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was \"Who'S Laughing Now\" officially released in 1989?"
      },
      {
        "method": "Iterative",
        "text": "What is the artist's name associated with the song \"1990-Sick (Get 'Em All)\"?"
      }
    ]
  },
  {
    "query": "Which film has the director died later, Excursion Train or Bad Day At Black Rock?",
    "questions": [
      {
        "method": "Baseline",
        "text": "When were the directors of these two films born?"
      },
      {
        "method": "Iterative",
        "text": "What is the identity of the director who died later between the two films?"
      }
    ]
  },
  {
    "query": "Which country Dexter Young's mother is from?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is there any information available about Dexter Young's family background or nationality?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Which country Dexter Young's mother is from??"
      }
    ]
  },
  {
    "query": "Who is Sancho Ramírez's maternal grandfather?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Sancho Ramírez a member of the Castilian royal family?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Who is Sancho Ramírez's maternal grandfather??"
      }
    ]
  },
  {
    "query": "Who is the paternal grandmother of Archduchess Dolores Of Austria?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is the Archduchess Dolores Of Austria still alive?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Who is the paternal grandmother of Archduchess Dolores Of Austria??"
      }
    ]
  },
  {
    "query": "Which film was released earlier, Man'S Search For Happiness or Tell It To The Bees?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the release date of either film specified in the original query?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Which film was released earlier, Man'S Search For Happiness or Tell It To The Bees??"
      }
    ]
  },
  {
    "query": "Are the directors of films The Edifying And Joyous Story Of Colinot and Cold Moon both from the same country?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is it possible to determine if the directors' countries of origin are known or publicly disclosed for these specific films?"
      },
      {
        "method": "Iterative",
        "text": "What is the country of origin for the directors of films The Edifying And Joyous Story Of Colinot and Cold Moon?"
      }
    ]
  },
  {
    "query": "Where was the performer of song Égérie (Song) born?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the performer of song Égérie (Song) a French singer, given that the song is by Édith Piaf?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Where was the performer of song Égérie (Song) born??"
      }
    ]
  },
  {
    "query": "Where was the father of Andrew Balding born?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the birth location of Andrew Balding's father documented in any historical records or biographies?"
      },
      {
        "method": "Iterative",
        "text": "What is the name of Andrew Balding's father?"
      }
    ]
  },
  {
    "query": "What is the place of birth of the performer of song Who...?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is the performer of the song \"Who Can It Be Now?"
      },
      {
        "method": "Iterative",
        "text": "What is the performer of song \"Who...\"?"
      }
    ]
  },
  {
    "query": "Where did William S. Burroughs Jr.'s father study?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was William S. Burroughs Jr.'s father, William Lee Burroughs, an American diplomat or military officer?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Where did William S. Burroughs Jr.'s father study??"
      }
    ]
  },
  {
    "query": "Which film came out earlier, Niyoti or Angali Pangali?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the release year of both films specified in the original query?"
      },
      {
        "method": "Iterative",
        "text": "What is the subject of the films \"Niyoti\" and \"Angali Pangali\"?"
      }
    ]
  },
  {
    "query": "Who is William Ii, Count Of Flanders's paternal grandmother?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was William I of Flanders (also known as William II, Count of Flanders) actually referred to in historical records?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Who is William Ii, Count Of Flanders's paternal grandmother??"
      }
    ]
  },
  {
    "query": "Which film was released earlier, Amelie Or The Time To Love or Beginners?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the release date of either film specified in the original query?"
      },
      {
        "method": "Iterative",
        "text": "What is the location of the film \"Beginners\"?"
      }
    ]
  },
  {
    "query": "What is the place of birth of the creator of Miss Seventeen?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is the creator of Miss Seventeen a well-known artist or designer, and if so, was their work primarily focused on fashion magazines?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of What is the place of birth of the creator of Miss Seventeen??"
      }
    ]
  },
  {
    "query": "Which film came out first, Natürlich Die Nelli or Cairo Declaration (Film)?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the release year of Natürlich Die Nelli specified in the original information?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Which film came out first, Natürlich Die Nelli or Cairo Declaration (Film)??"
      }
    ]
  },
  {
    "query": "Which film was released earlier, Anna-Liisa or Children Underground?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the release year of both films specified in the original query?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Which film was released earlier, Anna-Liisa or Children Underground??"
      }
    ]
  },
  {
    "query": "Who is Frederick Of Luxembourg's paternal grandfather?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Frederick of Luxembourg born before or after 1354?"
      },
      {
        "method": "Iterative",
        "text": "What is Frederick Of Luxembourg's paternal grandfather?"
      }
    ]
  },
  {
    "query": "Which film has the director born first, Spione or Five Million Look For An Heir?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the director of both films, Michael Curtiz, born before 1906?"
      },
      {
        "method": "Iterative",
        "text": "What is the birth year of the director of Spione?"
      }
    ]
  },
  {
    "query": "What is the place of birth of the director of film Dawn Of Life?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is the director of the 2016 animated film \"Dawn of the Planet of the Apes\" (not \"Life\") credited to have been born in a specific country or region?"
      },
      {
        "method": "Iterative",
        "text": "What is the film director's occupation?"
      }
    ]
  },
  {
    "query": "Are Coal City, Illinois and Lash Kenar, Nur both located in the same country?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is it possible to confirm if both locations are part of the same administrative division or region within their respective countries?"
      },
      {
        "method": "Iterative",
        "text": "What is the country where Coal City, Illinois and Lash Kenar are both located?"
      }
    ]
  },
  {
    "query": "Which film has the director who died first, The Face Of Fu Manchu or The Hidden One?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the director of both films the same person?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Which film has the director who died first, The Face Of Fu Manchu or The Hidden One??"
      }
    ]
  },
  {
    "query": "Where was the director of film Ronnie Rocket born?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Ronnie Rocket's birthplace in the United States?"
      },
      {
        "method": "Iterative",
        "text": "What was Ronnie Rocket's profession as a film director?"
      }
    ]
  },
  {
    "query": "What is the place of birth of James Douglas, 3Rd Earl Of Angus's father?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was James Douglas, 3rd Earl of Angus, a member of the Scottish royal House of Stewart?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of What is the place of birth of James Douglas, 3Rd Earl Of Angus's father??"
      }
    ]
  },
  {
    "query": "Are both Kaufland and Otrag located in the same country?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is it possible that one of these stores is actually located in a different country than the other?"
      },
      {
        "method": "Iterative",
        "text": "What countries do Kaufland and Otrag operate in?"
      }
    ]
  },
  {
    "query": "Which film has the director died later, Just Like A Woman (1939 Film) or Madigan'S Millions?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is the release year of \"Just Like A Woman\" (1939 Film) correct?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Which film has the director died later, Just Like A Woman (1939 Film) or Madigan'S Millions??"
      }
    ]
  },
  {
    "query": "Where did Meritaten's father die?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Meritaten's father, Pharaoh Akhenaten, actually deceased at the time of her birth or was he still alive when she became queen?"
      },
      {
        "method": "Iterative",
        "text": "What was the cause of Meritaten's father's death?"
      }
    ]
  },
  {
    "query": "What is the place of birth of Princess Margaretha Of Saxony's mother?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Princess Margaretha Of Saxony's mother born in Sweden?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of What is the place of birth of Princess Margaretha Of Saxony's mother??"
      }
    ]
  },
  {
    "query": "Who was born later, D'Arcy Coulson or Thomas William Adams?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was D'Arcy Coulson's birthdate specified in any of the provided information?"
      },
      {
        "method": "Iterative",
        "text": "What was D'Arcy Coulson's profession?"
      }
    ]
  },
  {
    "query": "Where did George Lane-Fox (Mp)'s father study?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was George Lane-Fox's father, John Fox-Strangeways, a fellow of Magdalen College, Oxford?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Where did George Lane-Fox (Mp)'s father study??"
      }
    ]
  },
  {
    "query": "Which film has the director born later, Monsieur Taxi or A Yiddish World Remembered?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the birth year of the directors of these films specified in the original information?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Which film has the director born later, Monsieur Taxi or A Yiddish World Remembered??"
      }
    ]
  },
  {
    "query": "Which film has the director who died later, The Death Kiss or Her Luck In London?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the director of both films still alive when \"Her Luck In London\" was released?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Which film has the director who died later, The Death Kiss or Her Luck In London??"
      }
    ]
  },
  {
    "query": "Who is the mother of the director of film Brenda Brave?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is Brenda Brave's filmography publicly available to identify her director?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Who is the mother of the director of film Brenda Brave??"
      }
    ]
  },
  {
    "query": "Where was the place of death of Juan Carlos Gumucio's wife?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Juan Carlos Gumucio's wife murdered in Chile?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of Where was the place of death of Juan Carlos Gumucio's wife??"
      }
    ]
  },
  {
    "query": "Who is the maternal grandmother of Felipe De Marichalar Y Borbón?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is Felipe De Marichalar Y Borbón's mother, Maria Francisca Peretola, also his paternal grandmother?"
      },
      {
        "method": "Iterative",
        "text": "What is the identity of Felipe De Marichalar Y Borbón's maternal grandmother?"
      }
    ]
  },
  {
    "query": "Which country Gilduin Of Le Puiset's father is from?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is Gilduin Of Le Puiset a character in a specific book or series?"
      },
      {
        "method": "Iterative",
        "text": "What is the country of origin of Gilduin Of Le Puiset's father?"
      }
    ]
  },
  {
    "query": "Which film has the director who was born earlier, Invasion 1897 or Nene Raju Nene Mantri?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the director of both films born before 1970?"
      },
      {
        "method": "Iterative",
        "text": "What is the birth year of the director of Nene Raju Nene Mantri?"
      }
    ]
  },
  {
    "query": "Who lived longer, Giuseppe Cesari or Nicos Poulantzas?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Giuseppe Cesari's lifespan measured in years or decades?"
      },
      {
        "method": "Iterative",
        "text": "What was Giuseppe Cesari's age at death compared to Nicos Poulantzas' age at death?"
      }
    ]
  },
  {
    "query": "Which award the composer of film Bhookh (1947 Film) won?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was the award won by the composer for his work on the music score specifically, or was it an overall award recognizing his contributions to the film?"
      },
      {
        "method": "Iterative",
        "text": "What is content or subject for Which award the composer of film Bhookh (1947 Film) won??"
      }
    ]
  },
  {
    "query": "Who is the father of Beltrán Vélez De Guevara, Marquis Of Campo Real?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Beltrán Vélez De Guevara, Marquis Of Campo Real, a member of the Spanish nobility during his lifetime?"
      },
      {
        "method": "Iterative",
        "text": "What is Beltrán Vélez De Guevara, Marquis Of Campo Real's father?"
      }
    ]
  },
  {
    "query": "Which film has the director born later, Diary Of A Maniac or Return Of The Hero?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is the birth year of the directors for both films publicly available?"
      },
      {
        "method": "Iterative",
        "text": "What is the birth year of the directors of Diary Of A Maniac and Return Of The Hero?"
      }
    ]
  },
  {
    "query": "What is the date of death of Henry St John, 18Th Baron St John Of Bletso's father?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Henry St John, 18th Baron St John of Bletso's father also known by any other title or name?"
      },
      {
        "method": "Iterative",
        "text": "What is the name of Henry St John, 18th Baron St John of Bletso's mother?"
      }
    ]
  },
  {
    "query": "What is the place of birth of Jo Planckaert's father?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Is there any information available about Jo Planckaert's family or personal life that might provide insight into his father's place of birth?"
      },
      {
        "method": "Iterative",
        "text": "What is the intended meaning of What is the place of birth of Jo Planckaert's father??"
      }
    ]
  },
  {
    "query": "Where did Prince Gustav Of Thurn And Taxis (1848–1914)'s mother die?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Prince Gustav of Thurn and Taxis' mother born in Austria?"
      },
      {
        "method": "Iterative",
        "text": "What date did Prince Gustav Of Thurn And Taxis' mother die?"
      }
    ]
  },
  {
    "query": "Who died first, Madame Pasca or James A. Donohoe?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was there any information provided about the dates of death for either Madame Pasca or James A. Donohoe?"
      },
      {
        "method": "Iterative",
        "text": "What is Madame Pasca's identity?"
      }
    ]
  },
  {
    "query": "Are both businesses, Telus and Ztr Control Systems, located in the same country?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Are they both Canadian companies?"
      },
      {
        "method": "Iterative",
        "text": "What country do both Telus and Ztr Control Systems operate in?"
      }
    ]
  },
  {
    "query": "Who is Thomas Stafford, 3Rd Earl Of Stafford's father?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Thomas Stafford, 3rd Earl of Stafford, a member of the House of Plantagenet?"
      },
      {
        "method": "Iterative",
        "text": "What is Thomas Stafford, 3rd Earl of Stafford's father?"
      }
    ]
  },
  {
    "query": "Who is older, Dyson Parody or Gene Watson?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Gene Watson born before 1940?"
      },
      {
        "method": "Iterative",
        "text": "What is Dyson Parody's identity?"
      }
    ]
  },
  {
    "query": "Where was the husband of Esperanza Osmeña born?",
    "questions": [
      {
        "method": "Baseline",
        "text": "Was Esperanza Osmeña's husband a public figure or notable individual, which might help narrow down the location of his birth?"
      },
      {
        "method": "Iterative",
        "text": "What was the birthplace of Esperanza Osmeña's husband?"
      }
    ]
  }
];