from django.db import migrations
from django.utils.text import slugify

def prefill_data(apps, schema_editor):
    # Get the models
    Platform = apps.get_model('common', 'Platform')
    Genre = apps.get_model('common', 'Genre')
    Game = apps.get_model('games', 'Game')

    # Prefill Platform data
    platforms = [
        {"platform_name": "PC", "description": "Personal Computer"},
        {"platform_name": "PS5", "description": "Sony's latest gen gaming console"},
        {"platform_name": "PS4", "description": "Sony's previous gen gaming console"},
        {"platform_name": "Nintendo Switch", "description": "Nintendo's handheld console"},
    ]
    platform_instances = [Platform(**platform) for platform in platforms]
    Platform.objects.bulk_create(platform_instances)

    # Now that platforms are saved, we can query the database
    pc = Platform.objects.get(platform_name="PC")
    ps5 = Platform.objects.get(platform_name="PS5")
    ps4 = Platform.objects.get(platform_name="PS4")
    nintendo_switch = Platform.objects.get(platform_name="Nintendo Switch")

    # Prefill Genre data
    genres = [
        {"genre_name": "Action", "description": "Fast-paced games"},
        {"genre_name": "Adventure", "description": "Exploration-focused games"},
        {"genre_name": "RPG", "description": "Role-playing games"},
        {"genre_name": "Horror", "description": "Spooky games that keep you on edge"},
    ]
    genre_instances = [Genre(**genre) for genre in genres]
    Genre.objects.bulk_create(genre_instances)

    # Now that genres are saved, we can query the database
    action = Genre.objects.get(genre_name="Action")
    adventure = Genre.objects.get(genre_name="Adventure")
    rpg = Genre.objects.get(genre_name="RPG")
    horror = Genre.objects.get(genre_name="Horror")

    # Prefill Game data
    games = [
        {
            "name": "The Witcher 3: Wild Hunt",
            "release_date": "2015-05-19",
            "developer": "CD Projekt Red",
            "description": "An open-world RPG where you play as Geralt of Rivia, a monster hunter, in a visually stunning medieval fantasy world.",
            "game_cover": "https://cdn1.epicgames.com/offer/14ee004dadc142faaaece5a6270fb628/EGS_TheWitcher3WildHuntCompleteEdition_CDPROJEKTRED_S2_1200x1600-53a8fb2c0201cd8aea410f2a049aba3f",
            "slug": slugify("The Witcher 3: Wild Hunt"),
        },
        {
            "name": "Tomb Raider I-III Remastered",
            "release_date": "2024-02-14",
            "developer": "Crystal Dynamics",
            "description": "Remastered versions of the classic Tomb Raider games with updated graphics and gameplay improvements.",
            "game_cover": "https://cms.gameflycdn.com/proxy/gf/boxart/480w/5042366.jpg",
            "slug": slugify("Tomb Raider I-III Remastered"),
        },
        {
            "name": "Rise of the Tomb Raider",
            "release_date": "2015-11-10",
            "developer": "Crystal Dynamics",
            "description": "Lara Croft's journey through Siberia in search of the lost city of Kitezh, featuring action-packed gameplay and a deep story.",
            "game_cover": "https://www.crystaldynamics.com/content/uploads/2015/11/Rise-of-the-Tomb-Raider-20-Year-Celebration-Edition-PlayStation-4-1.jpeg",
            "slug": slugify("Rise of the Tomb Raider"),
        },
        {
            "name": "Cyberpunk 2077: Ultimate Edition",
            "release_date": "2023-09-26",  # Placeholder date (Update when available)
            "developer": "CD Projekt Red",
            "description": "The ultimate edition of Cyberpunk 2077, with expanded storylines, new features, and enhanced graphics.",
            "game_cover": "https://cdn1.epicgames.com/offer/77f2b98e2cef40c8a7437518bf420e47/EGS_Cyberpunk2077UltimateEdition_CDPROJEKTRED_Editions_S2_1200x1600-81442c61fd09b45ecd03add7c0c3afdd",
            "slug": slugify("Cyberpunk 2077: Ultimate Edition"),
        },
        {
            "name": "Horizon Zero Dawn",
            "release_date": "2017-02-28",
            "developer": "Guerrilla Games",
            "description": "A post-apocalyptic open-world action RPG where you play as Aloy, a hunter in a world ruled by robotic creatures.",
            "game_cover": "https://m.media-amazon.com/images/I/71gCM8JhzdL.jpg",
            "slug": slugify("Horizon Zero Dawn"),
        },
        {
            "name": "Horizon Forbidden West",
            "release_date": "2022-02-18",
            "developer": "Guerrilla Games",
            "description": "A sequel to Horizon Zero Dawn, where Aloy ventures to the Forbidden West to discover the secrets of a new land and new dangers.",
            "game_cover": "https://cdn1.epicgames.com/offer/24cc2629b0594bf29340f6acf9816af8/EGS_HorizonForbiddenWestCompleteEdition_GuerrillaGamesNixxesSoftware_S2_1200x1600-6eeadae1c58ebaaa74b109bd26d96645",
            "slug": slugify("Horizon Forbidden West"),
        },
        {
            "name": "Mass Effect: Andromeda",
            "release_date": "2017-03-21",
            "developer": "BioWare",
            "description": "Set in the Andromeda galaxy, this sci-fi RPG follows the Ryder family on their journey to colonize a new galaxy while facing various alien threats.",
            "game_cover": "https://m.media-amazon.com/images/I/71zMyANthiL.jpg",
            "slug": slugify("Mass Effect: Andromeda"),
        },
        {
            "name": "Shadow of the Tomb Raider",
            "release_date": "2018-09-14",
            "developer": "Crystal Dynamics, Eidos-Montreal",
            "description": "Lara Croft faces her greatest challenges in the jungle of South America, solving puzzles and surviving brutal conditions to stop a Mayan apocalypse.",
            "game_cover": "https://m.media-amazon.com/images/I/810GPUK57wL.jpg",
            "slug": slugify("Shadow of the Tomb Raider"),
        },
        {
            "name": "Elden Ring",
            "release_date": "2022-02-25",
            "developer": "FromSoftware",
            "description": "The Elden Ring is a conduit of sorts that is at the centre of the power of the Erdtree, which blesses the Lands Between with immortality, as a result. The world is kept in balance, primarily, by Queen Marika, one of the most powerful immortals, who went on to have a few children, who are classed as demi-gods.",
            "game_cover": "https://image.api.playstation.com/vulcan/ap/rnd/202110/2000/phvVT0qZfcRms5qDAk0SI3CM.png",
            "slug": slugify("Elden Ring"),
        },

    ]

    # Create game instances without many-to-many relationships
    game_instances = [Game(**{k: v for k, v in game.items() if k not in ['genre', 'platform']}) for game in games]
    Game.objects.bulk_create(game_instances)

    # Now, assign many-to-many relationships
    # Ensure the games are saved before we assign relationships
    game1 = Game.objects.get(name="The Witcher 3: Wild Hunt")
    game1.genre.add(rpg)
    game1.platform.add(pc, ps5)
    game1.save()  # Save after modifying relationships

    game3 = Game.objects.get(name="Tomb Raider I-III Remastered")
    game3.genre.add(action, adventure)
    game3.platform.add(pc, ps5)
    game3.save()

    game4 = Game.objects.get(name="Rise of the Tomb Raider")
    game4.genre.add(action, adventure)
    game4.platform.add(pc, ps5)
    game4.save()

    game5 = Game.objects.get(name="Cyberpunk 2077: Ultimate Edition")
    game5.genre.add(action, rpg)
    game5.platform.add(pc, ps5)
    game5.save()

    game6 = Game.objects.get(name="Horizon Zero Dawn")
    game6.genre.add(action, rpg)
    game6.platform.add(pc, ps5)
    game6.save()

    game7 = Game.objects.get(name="Horizon Forbidden West")
    game7.genre.add(action, rpg)
    game7.platform.add(ps5)
    game7.save()

    game8 = Game.objects.get(name="Mass Effect: Andromeda")
    game8.genre.add(action, rpg)
    game8.platform.add(pc, ps4)
    game8.save()

    game9 = Game.objects.get(name="Shadow of the Tomb Raider")
    game9.genre.add(action, adventure)
    game9.platform.add(pc, ps5)
    game9.save()

    game10 = Game.objects.get(name='Elden Ring')
    game10.genre.add(action, rpg)
    game10.platform.add(pc, ps5, ps4)
    game10.save()

def reverse_prefill_data(apps, schema_editor):
    Platform = apps.get_model('common', 'Platform')
    Genre = apps.get_model('common', 'Genre')
    Game = apps.get_model('games', 'Game')

    # Reverse data deletion
    Platform.objects.filter(platform_name__in=["PC", "PS5", "PS4", "Nintendo Switch"]).delete()
    Genre.objects.filter(genre_name__in=["Action", "Adventure", "RPG", "Horror"]).delete()
    Game.objects.filter(name__in=["The Witcher 3: Wild Hunt", "Silent Hill 2 Remake"]).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('games', '0005_alter_review_user'),  # Update to match your dependencies
        ('common', '0006_gamesuggestion_created_at_and_more'),  # Update to match your dependencies
    ]

    operations = [
        migrations.RunPython(prefill_data, reverse_code=reverse_prefill_data),  # Add reverse_code here
    ]