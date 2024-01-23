import unittest

from module_runner import ModuleRunner


# class TestExercice1(unittest.TestCase):
#     def setUp(self):
#         self.runner = ModuleRunner("exo1")
#         self.input_questions = "Entrez le nom de la planete exploree: Entrez la date de votre visite (JJ/MM/AAAA): Decrivez la planete: "

#     def test_exercice1(self):
#         simulated_inputs = "Mars\n01/01/2024\nPlanete rouge avec surface poussiereuse\n"
#         output = self.runner.run(simulated_inputs)
#         expected = f"{self.input_questions}Votre exploration a ete ajoutee au Journal des Astres !\n-------------------------------\nTitre : Decouverte de Mars\nDate : 01/01/2024\nDescription : Planete rouge avec surface poussiereuse\n"
#         self.assertEqual(expected, output)


# class TestExercice2(unittest.TestCase):
#     def setUp(self):
#         self.runner = ModuleRunner("exo2")
#         self.input_questions = "Nombre de baguettes a fabriquer : "

#     def test_exercice2_cinq_baguettes(self):
#         simulated_inputs = "5\n"
#         output = self.runner.run(simulated_inputs)
#         expected = f"{self.input_questions}Voici les materiaux requis pour la fabrication de 5 baguettes magiques:\n- 15 piece(s) de bois\n- 5 coeur(s) de creatures magiques\n- 50 ml de vernis\n"
#         self.assertEqual(expected, output)

#     def test_exercice2_dix_baguettes(self):
#         simulated_inputs = "18\n"
#         output = self.runner.run(simulated_inputs)
#         expected = f"{self.input_questions}Voici les materiaux requis pour la fabrication de 18 baguettes magiques:\n- 54 piece(s) de bois\n- 18 coeur(s) de creatures magiques\n- 180 ml de vernis\n"
#         self.assertEqual(expected, output)


# class TestExercice3(unittest.TestCase):
#     def setUp(self):
#         self.runner = ModuleRunner("exo3")
#         self.input_questions = "Entrez la vitesse initiale (en m/s) : Entrez l'angle de lancement (en degres) : "

#     def test_vitesse_initiale_zero(self):
#         simulated_inputs = "0\n45\n"
#         output = self.runner.run(simulated_inputs)
#         expected = f"{self.input_questions}La distance parcourue par le projectile est de 0.00 metres.\n"
#         self.assertEqual(expected, output)

#     def test_valeurs_realistes_1(self):
#         simulated_inputs = "10\n30\n"
#         output = self.runner.run(simulated_inputs)
#         expected = f"{self.input_questions}La distance parcourue par le projectile est de 8.83 metres.\n"
#         self.assertEqual(expected, output)

#     def test_valeurs_realistes_2(self):
#         simulated_inputs = "20\n60\n"
#         output = self.runner.run(simulated_inputs)
#         expected = f"{self.input_questions}La distance parcourue par le projectile est de 35.31 metres.\n"
#         self.assertEqual(expected, output)


class TestExercice4(unittest.TestCase):
    def setUp(self):
        self.runner = ModuleRunner("exo4")
        self.input_questions = "Entrez le message de l'Empire : "

    def test_message_vide(self):
        simulated_inputs = "\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Les coordonnees galactiques sont 0.0.0.0.0.0.\n"
        self.assertEqual(expected, output)

    def test_phrase_1(self):
        simulated_inputs = "Vive l'Empire!\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Les coordonnees galactiques sont 0.3.2.0.0.0.\n"
        self.assertEqual(expected, output)

    def test_phrase_2(self):
        simulated_inputs = "Attaquez maintenant!\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Les coordonnees galactiques sont 4.2.1.0.1.0.\n"
        self.assertEqual(expected, output)

    def test_phrase_3(self):
        simulated_inputs = "You are a spy!\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Les coordonnees galactiques sont 2.1.0.1.1.2.\n"
        self.assertEqual(expected, output)


class TestExercice5(unittest.TestCase):
    def setUp(self):
        self.runner = ModuleRunner("exo5")
        self.input_questions = "Entrez le niveau de charge actuel de la batterie : "

    def test_valeur_valide(self):
        simulated_inputs = "75\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}[❚❚❚❚❚❚❚❚  ]\n75%\n"
        self.assertEqual(expected, output)

    def test_valeur_hors_intervalle(self):
        simulated_inputs = "110\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Erreur : niveau de charge invalide.\n"
        self.assertEqual(expected, output)

    def test_valeur_hors_intervalle_2(self):
        simulated_inputs = "-5\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Erreur : niveau de charge invalide.\n"
        self.assertEqual(expected, output)

    def test_valeur_limite(self):
        simulated_inputs = "0\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}[          ]\n0%\n"
        self.assertEqual(expected, output)

    def test_charge_complete(self):
        simulated_inputs = "100\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}[❚❚❚❚❚❚❚❚❚❚]\n100%\n"
        self.assertEqual(expected, output)

    def test_charge_22_pourcent(self):
        simulated_inputs = "22\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}[❚❚        ]\n22%\n"
        self.assertEqual(expected, output)

    def test_charge_46_pourcent(self):
        simulated_inputs = "46\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}[❚❚❚❚❚     ]\n46%\n"
        self.assertEqual(expected, output)


class TestExercice6(unittest.TestCase):
    def setUp(self):
        self.runner = ModuleRunner("exo6")
        self.input_questions = "Entrez le pourcentage de charge actuel de la batterie de la Batmobile : "

    def test_niveau_charge_valide(self):
        simulated_inputs = "75\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Temps restant : 2h20min\n"
        self.assertEqual(expected, output)

    def test_niveau_charge_hors_intervalle(self):
        simulated_inputs = "105\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Erreur : niveau de charge invalide.\n"
        self.assertEqual(expected, output)

    def test_niveau_charge_limite(self):
        simulated_inputs = "0\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Temps restant : 0h00min\n"
        self.assertEqual(expected, output)

    def test_charge_5_pourcent(self):
        simulated_inputs = "5\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Temps restant : 0h25min\n"
        self.assertEqual(expected, output)

    def test_charge_100_pourcent(self):
        simulated_inputs = "100\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Temps restant : 2h45min\n"
        self.assertEqual(expected, output)

    def test_charge_34_pourcent(self):
        simulated_inputs = "34\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Temps restant : 1h23min\n"
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
