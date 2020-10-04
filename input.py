import pandas as pd
import numpy as np

TIME_LIMIT = 12  # hours
BUDGET = 65  # euros

# All locations
locations = {
    'TE': {'title': 'La Tour Eiffel', 'duration': 4.50, 'rate': 5, 'price': 15.50},
    'ML': {'title': 'Le Musée du Louvre', 'duration': 3.00, 'rate': 4, 'price': 12.00},
    'AT': {'title': 'L’Arc de Triomphe', 'duration': 1.00, 'rate': 3, 'price': 9.50},
    'MO': {'title': 'Le Musée d’Orsay ', 'duration': 2.00, 'rate': 2, 'price': 11.00},
    'JT': {'title': 'Le Jardin des Tuileries ', 'duration': 1.50, 'rate': 3, 'price': 0.00},
    'CA': {'title': 'Les Catacombes', 'duration': 2.00, 'rate': 4, 'price': 10.00},
    'CP': {'title': 'Le Centre Pompidou', 'duration': 2.50, 'rate': 1, 'price': 10.00},
    'CN': {'title': 'La Cathédrale Notre Dame de Paris', 'duration': 2.00, 'rate': 5, 'price': 5.00},
    'BS': {'title': 'La Basilique du Sacré-Coeur', 'duration': 2.00, 'rate': 4, 'price': 8.00},
    'SC': {'title': 'La Sainte Chapelle', 'duration': 1.50, 'rate': 1, 'price': 8.50},
    'PC': {'title': 'La Place de la Concorde', 'duration': .75, 'rate': 3, 'price': 0.00},
    'TM': {'title': 'La Tour Montparnasse', 'duration': 2.00, 'rate': 2, 'price': 15.00},
    'AC': {'title': 'L’Avenue des Champs-Elysées', 'duration': 1.50, 'rate': 5, 'price': 0.00}
}

# Grouped locations where distances are lower than 1 km
locations_if_p1 = {
    'TE': {'title': 'La Tour Eiffel', 'duration': 4.50, 'rate': 5, 'price': 15.50},
    'CA': {'title': 'Les Catacombes', 'duration': 2.00, 'rate': 4, 'price': 10.00},
    'BS': {'title': 'La Basilique du Sacré-Coeur', 'duration': 2.00, 'rate': 4, 'price': 8.00},
    'TM': {'title': 'La Tour Montparnasse', 'duration': 2.00, 'rate': 2, 'price': 15.00},
    'AT_AC': {'duration': 2.50, 'price': 9.50},
    'MO_JT_PC': {'duration': 4.25, 'price': 11.00},
    'CP_CN_SC_ML': {'duration': 9.00, 'price': 35.50}
}

# Distances in km
d = pd.DataFrame(columns=list(locations.keys()), index=list(locations.keys()),
                 data=np.array([[0.00, 3.80, 2.10, 2.40, 3.50, 4.20, 5.00, 4.40, 5.50, 4.20, 2.50, 3.10, 1.90],
                                [3.80, 0.00, 3.80, 1.10, 1.30, 3.30, 1.30, 1.10, 3.40, 0.80, 1.70, 2.50, 2.80],
                                [2.10, 3.80, 0.00, 3.10, 3.00, 5.80, 4.80, 4.90, 4.30, 4.60, 2.20, 4.40, 1.00],
                                [2.40, 1.10, 3.10, 0.00, 0.90, 3.10, 2.50, 2.00, 3.90, 1.80, 1.00, 2.30, 2.10],
                                [3.50, 1.30, 3.00, 0.90, 0.00, 4.20, 2.00, 2.40, 2.70, 2.00, 1.00, 3.40, 2.10],
                                [4.20, 3.30, 5.80, 3.10, 4.20, 0.00, 3.50, 2.70, 6.50, 2.60, 3.80, 1.30, 4.90],
                                [5.00, 1.30, 4.80, 2.50, 2.00, 3.50, 0.00, 0.85, 3.70, 0.90, 2.70, 3.40, 3.80],
                                [4.40, 1.10, 4.90, 2.00, 2.40, 2.70, 0.85, 0.00, 4.50, 0.40, 2.80, 2.70, 3.90],
                                [5.50, 3.40, 4.30, 3.90, 2.70, 6.50, 3.70, 4.50, 0.00, 4.20, 3.30, 5.70, 3.80],
                                [4.20, 0.80, 4.60, 1.80, 2.00, 2.60, 0.90, 0.40, 4.20, 0.00, 2.50, 2.60, 3.60],
                                [2.50, 1.70, 2.20, 1.00, 1.00, 3.80, 2.70, 2.80, 3.30, 2.50, 0.00, 3.00, 1.20],
                                [3.10, 2.50, 4.40, 2.30, 3.40, 1.30, 3.40, 2.70, 5.70, 2.60, 3.00, 0.00, 2.10],
                                [1.90, 2.80, 1.00, 2.10, 2.10, 4.90, 3.80, 3.90, 3.80, 3.60, 1.20, 2.10, 0.00]]))

preferences = {
    '1': 'If two sites are geographically very close (within a radius of 1 km of walking), he will prefer to visit '
         'these two sites instead of visiting only one.',
    '2': 'He absolutely wants to visit the Eiffel Tower (TE) and Catacombes (CA)',
    '3': 'If he visits Notre Dame Cathedral (CN) then he will not visit the Sainte Chapelle (SC).',
    '4': 'He absolutely wants to visit Tour Montparnasse (TM).',
    '5': 'If he visits the Louvre (ML) Museum then he must visit the Pompidou Center (CP).',
}

questions = {
    '1': 'It is assumed that Mr. Doe gives equal importance to each tourist site, and he wants to visit the maximum '
         'number of sites. Which list(s) of places could you recommend to him ? This solution will be called '
         'ListVisit 1.',
    '2a': 'For each of the five preferences above, suggest to Mr. Doe, one or more lists of tourist sites to visit. '
          'Are the obtained lists different from the solution ListVisit1? To answer this last question, you can '
          'implement a python function returning True (respectively False) if two lists are identical (respectively '
          'different).',
    '2b': 'If Mr. Doe wishes, at the same time, to take into account Preference 1 and Preference 2, which list(s) '
          'would you recommend to him ?',
    '2c': 'If Mr. Doe wishes, at the same time, to take into account Preference 1 and Preference 3, which list(s) '
          'would you recommend to him ?',
    '2d': 'If Mr. Doe wishes, at the same time, to take into account Preference 1 and Preference 4, which list(s) '
          'would you recommend to him ?',
    '2e': 'If Mr. Doe wishes, at the same time, to take into account Preference 2 and Preference 5, which list(s) '
          'would you recommend to him ?',
    '2f': 'If Mr. Doe wishes, at the same time, to take into account Preference 3 and Preference 4, which list(s) '
          'would you recommend to him ?',
    '2g': 'If Mr. Doe wishes, at the same time, to take into account Preference 4 and Preference 5, which list(s) '
          'would you recommend to him ?',
    '2h': 'If Mr. Doe wishes, at the same time, to take into account Preference 1, Preference 2 and Preference 4, '
          'which list(s) would you recommend to him ?',
    '2i': 'If Mr. Doe wishes, at the same time, to take into account Preference 2, Preference 3 and Preference 5, '
          'which list(s) would you recommend to him ?',
    '2j': 'If Mr. Doe wishes, at the same time, to take into account Preference 2, Preference 3, Preference 4 and '
          'Preference 5, which list(s) would you recommend to him ?',
    '2k': 'If Mr. Doe wishes, at the same time, to take into account Preference 1, Preference 2, Preference 4 and '
          'Preference 5, which list(s) would you recommend to him ?',
    '2l': 'If Mr. Doe wishes, at the same time, to take into account Preference 1, Preference 2, Preference 3, '
          'Preference 4 and Preference 5, which list(s) would you recommend to him ?',
    '2m': 'Is the solution ListVisit1 different to these solutions founded above '
          '(with the combination of preferences) ?',
    '3': '...'
}
