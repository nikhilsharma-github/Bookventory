from django.db import migrations
from django.utils import timezone


def create_demo_polls(apps, schema_editor):
    Question = apps.get_model('polls', 'Question')
    Choice = apps.get_model('polls', 'Choice')
    now = timezone.now()

    demo_data = [
        {
            'question_text': 'Who will win the next Cricket World Cup?',
            'choices': ['India', 'England', 'Australia', 'New Zealand'],
        },
        {
            'question_text': 'Which streaming service has the best music catalog?',
            'choices': ['Spotify', 'Apple Music', 'YouTube Music', 'Amazon Music'],
        },
        {
            'question_text': 'Which format do you prefer for live sports?',
            'choices': ['Stadium (in-person)', 'TV Broadcast', 'Streaming', 'Highlights only'],
        },
        {
            'question_text': 'Which genre would you like featured in our next playlist?',
            'choices': ['Pop', 'Indie', 'Hip-Hop', 'Electronic'],
        },
        {
            'question_text': 'Which upcoming movie are you most excited about?',
            'choices': ['Action Blockbuster', 'Indie Drama', 'Sci-Fi Thriller', 'Animated Film'],
        },
    ]

    for item in demo_data:
        q = Question.objects.create(question_text=item['question_text'], pub_date=now)
        for choice_text in item['choices']:
            Choice.objects.create(question=q, choice_text=choice_text, votes=0)


def remove_demo_polls(apps, schema_editor):
    Question = apps.get_model('polls', 'Question')
    # Remove demo questions by question_text
    demo_texts = [
        'Who will win the next Cricket World Cup?',
        'Which streaming service has the best music catalog?',
        'Which format do you prefer for live sports?',
        'Which genre would you like featured in our next playlist?',
        'Which upcoming movie are you most excited about?',
    ]
    Question.objects.filter(question_text__in=demo_texts).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_demo_polls, reverse_code=remove_demo_polls),
    ]
