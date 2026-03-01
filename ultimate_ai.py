# ==================================================
# ultimate_ai.py
# CHATGPT 2 - ULTIMATE AI CORE
# Spécialisée Gaming / Codage / Hardware
# Modulaire + règles + mémoire + commandes
# ==================================================

class UltimateAI:
    def __init__(self):
        self.memory = []
        self.domains = {
            "gaming": self.gaming_ai,
            "coding": self.coding_ai,
            "hardware": self.hardware_ai
        }

    # -----------------------------
    # ROUTEUR PRINCIPAL
    # -----------------------------
    def respond(self, message: str) -> str:
        msg = message.lower().strip()
        self.memory.append(message)

        # Commandes directes (priorité max)
        if msg.startswith("/"):
            return self.command_mode(msg)

        # Règles expertes
        rule = self.rule_engine(msg)
        if rule:
            return rule

        # Routage automatique
        for domain, handler in self.domains.items():
            if self.detect_domain(domain, msg):
                return handler(msg)

        return self.default_response()

    # -----------------------------
    # COMMANDES
    # -----------------------------
    def command_mode(self, msg):
        commands = {
            "/gaming": "🎮 Mode Gaming activé. Décris ton problème.",
            "/code": "🧑‍💻 Mode Codage activé. Montre ton code ou l’erreur.",
            "/bios": "🖥️ Mode Hardware activé. Carte mère, BIOS ou RAM ?",
            "/memory": f"🧠 Mémoire active : {len(self.memory)} messages.",
            "/help": "Commandes : /gaming /code /bios /memory"
        }
        return commands.get(msg.split()[0], "❌ Commande inconnue.")

    # -----------------------------
    # MOTEUR DE RÈGLES EXPERTES
    # -----------------------------
    def rule_engine(self, msg):
        rules = [
            (("xmp", "désactivé"), 
             "Active le profil XMP dans le BIOS pour de meilleures performances RAM."),
            (("fps", "chute"), 
             "Réduis les ombres, active DLSS/FSR et vérifie les températures."),
            (("erreur", "python"), 
             "Donne le message d’erreur exact et la ligne concernée.")
        ]

        for keywords, response in rules:
            if all(k in msg for k in keywords):
                return response

        return None

    # -----------------------------
    # DÉTECTION DE DOMAINE
    # -----------------------------
    def detect_domain(self, domain, msg):
        keywords = {
            "gaming": ["jeu", "gaming", "fps", "lag", "gpu"],
            "coding": ["code", "python", "bug", "fonction", "erreur"],
            "hardware": ["bios", "ram", "xmp", "carte mère", "motherboard"]
        }
        return any(k in msg for k in keywords[domain])

    # -----------------------------
    # LOGIQUE GAMING
    # -----------------------------
    def gaming_ai(self, msg):
        return (
            "🎮 **Analyse Gaming**\n"
            "- Mets à jour les pilotes GPU\n"
            "- Vérifie les paramètres graphiques\n"
            "- Surveille CPU/GPU (throttling)\n"
            "- Mode plein écran exclusif recommandé\n"
            "- Désactive overlays inutiles"
        )

    # -----------------------------
    # LOGIQUE CODAGE
    # -----------------------------
    def coding_ai(self, msg):
        return (
            "🧑‍💻 **Analyse Codage**\n"
            "- Identifie clairement l’entrée/sortie\n"
            "- Isole la fonction fautive\n"
            "- Ajoute des logs / print\n"
            "- Vérifie types, conditions et portée\n"
            "- Envoie le code pour debug précis"
        )

    # -----------------------------
    # LOGIQUE HARDWARE
    # -----------------------------
    def hardware_ai(self, msg):
        return (
            "🖥️ **Analyse Matériel**\n"
            "- Vérifie la version du BIOS\n"
            "- Active XMP si compatible\n"
            "- Contrôle températures et tensions\n"
            "- Vérifie compatibilité CPU/RAM"
        )

    # -----------------------------
    # RÉPONSE PAR DÉFAUT
    # -----------------------------
    def default_response(self):
        return (
            "🤖 ChatGPT 2 – IA informatique avancée\n"
            "Domaines : Gaming 🎮 | Codage 🧑‍💻 | Hardware 🖥️\n"
            "Commandes : /gaming /code /bios /help"
        )


# ==================================================
# MODE CONSOLE (LOCAL)
# ==================================================
if __name__ == "__main__":
    ai = UltimateAI()
    print("ChatGPT 2 démarré. Tape 'exit' pour quitter.")

    while True:
        user = input("> ")
        if user.lower() == "exit":
            break
        print(ai.respond(user))
