from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from django.core.management import BaseCommand
from chatterbot.trainers import ListTrainer


class Command(BaseCommand):
    help = "Training the chatbot"

    def handle(self, *args, **options):
        chatbot = ChatBot(**settings.CHATTERBOT)
        trainer = ListTrainer(chatbot)
        trainer.train(
            [
                "Hello",
                "Hi there!",
                "How are you doing?",
                "I'm doing great.",
                "That is good to hear",
                "Thank you.",
                "You're welcome.",
            ]
        )

        self.stdout.write(self.style.SUCCESS("Successfully trained!"))
