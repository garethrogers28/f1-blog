from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post

POSTS = [
    {
        "title": "2026 Title Contenders: Who Will Be World Champion?",
        "slug": "2026-title-contenders",
        "excerpt": "The battle for the 2026 World Championship is heating up. We look at the frontrunners and their chances.",
        "content": (
            "The 2026 Formula 1 season has delivered one of the most exciting title races in recent memory. "
            "With new regulations shaking up the pecking order, several drivers have emerged as genuine contenders "
            "for the World Championship.\n\n"
            "The early part of the season saw unexpected results, with midfield teams suddenly finding themselves "
            "at the sharp end of the grid. The new ground-effect aerodynamic regulations have levelled the playing "
            "field in ways that many predicted but few truly expected.\n\n"
            "As we head into the European leg of the calendar, the championship standings are tighter than ever. "
            "The top three drivers are separated by fewer than 20 points, and at least five drivers remain "
            "mathematically in contention. This is shaping up to be a season that will go down to the wire.\n\n"
            "The key question remains: can the current leader maintain their consistency, or will the chasing pack "
            "find another gear? With several technical upgrades expected at the upcoming races, the title fight "
            "is far from over."
        ),
    },
    {
        "title": "The Battle at the Bottom: Who Will Avoid the Wooden Spoon?",
        "slug": "battle-at-the-bottom",
        "excerpt": "While all eyes are on the front, the fight to avoid last place in the constructors' standings is just as fierce.",
        "content": (
            "Formula 1 is not just about the glitz and glamour of fighting for victories. At the back of the grid, "
            "a very different battle rages on — the fight to avoid finishing last in the Constructors' Championship.\n\n"
            "For the smaller teams, every point matters. Prize money distribution in Formula 1 is heavily weighted "
            "towards finishing position, and the difference between ninth and tenth in the constructors' standings "
            "can be worth millions of dollars. That money can make or break a team's budget for the following season.\n\n"
            "This year, two teams are locked in a particularly intense scrap at the bottom. Both have shown flashes "
            "of pace at certain circuits, but consistency has been their biggest enemy. Reliability issues, "
            "strategy errors, and qualifying mishaps have all played their part.\n\n"
            "The drivers at these teams deserve credit for their commitment. Racing at the back of the grid, often "
            "with little television coverage, they push just as hard as those at the front. Their battles may not "
            "make the headlines, but they are no less dramatic."
        ),
    },
    {
        "title": "New Teams on the Grid: Fresh Blood in Formula 1",
        "slug": "new-teams-on-the-grid",
        "excerpt": "Formula 1 welcomes new entrants for the first time in years. Can they compete with the established giants?",
        "content": (
            "The arrival of new teams in Formula 1 is always an exciting moment for the sport. Fresh investment, "
            "new talent, and different perspectives breathe life into a paddock that can sometimes feel like a "
            "closed shop.\n\n"
            "The new entrants face an enormous challenge. Building a competitive Formula 1 team from scratch requires "
            "not just financial muscle, but also the right people, infrastructure, and technical knowledge. The gap "
            "between the established teams and newcomers has historically been vast.\n\n"
            "However, the current regulatory environment is designed to help new teams become competitive more quickly. "
            "The cost cap limits how much the top teams can spend, while the aerodynamic testing restrictions give "
            "lower-placed teams more wind tunnel time. These measures should, in theory, allow new entrants to close "
            "the gap faster than ever before.\n\n"
            "Early signs have been mixed. The new teams have shown they can be reliable and occasionally scrape into "
            "the points-paying positions, but regular points finishes remain a stretch goal for now. The real "
            "question is whether they can attract the sponsorship and talent needed to take the next step."
        ),
    },
    {
        "title": "The Ferrari 312T: A Classic Machine from F1's Golden Era",
        "slug": "ferrari-312t-classic",
        "excerpt": "We take a look back at the iconic Ferrari 312T, one of the most beautiful and successful cars in F1 history.",
        "content": (
            "The Ferrari 312T is one of the most iconic Formula 1 cars ever built. Designed by Mauro Forghieri, "
            "this flat-12 powered machine dominated the mid-1970s and helped establish Ferrari's reputation as the "
            "most successful team in the sport's history.\n\n"
            "The 'T' in 312T stood for 'trasversale', referring to the transverse-mounted gearbox that was the "
            "car's key innovation. This design choice improved weight distribution and allowed the car to carry "
            "more speed through corners. Combined with the glorious sound of the flat-12 engine, the 312T was "
            "a masterpiece of engineering.\n\n"
            "Niki Lauda drove the original 312T to the 1975 World Championship, and the car's descendants — the "
            "312T2, T3, T4, and T5 — continued to win races and championships into the early 1980s. The 312T4, "
            "driven by Jody Scheckter and Gilles Villeneuve, claimed the 1979 title.\n\n"
            "Today, the Ferrari 312T remains one of the most sought-after historic racing cars. Its combination of "
            "beautiful design, competitive success, and that unforgettable engine note make it a true icon of the sport."
        ),
    },
    {
        "title": "The Lotus 79: The Car That Changed Formula 1 Forever",
        "slug": "lotus-79-ground-effect",
        "excerpt": "The Lotus 79 pioneered ground-effect aerodynamics and revolutionised how F1 cars are designed.",
        "content": (
            "When Colin Chapman unveiled the Lotus 79 in 1978, he changed the face of Formula 1 forever. The car "
            "introduced the concept of ground-effect aerodynamics to the sport, using the car's underside to generate "
            "enormous downforce without the drag penalty of conventional wings.\n\n"
            "The principle was elegant in its simplicity. Inverted wing profiles built into the sidepods, combined "
            "with sliding skirts that sealed the underside from the outside air, created a low-pressure area beneath "
            "the car. The result was a machine that was glued to the track, able to carry incredible speed through "
            "corners while remaining relatively slippery in a straight line.\n\n"
            "Mario Andretti drove the Lotus 79 to the 1978 World Championship in dominant fashion, with teammate "
            "Ronnie Peterson providing crucial support. The car was so far ahead of the competition that other teams "
            "scrambled to copy the concept for the following season.\n\n"
            "The ground-effect revolution that the Lotus 79 started would define Formula 1 car design for the next "
            "several years, and its influence can still be seen in modern F1 cars today. It remains one of the most "
            "important racing cars ever built."
        ),
    },
    {
        "title": "Ayrton Senna: The Genius Who Transcended the Sport",
        "slug": "ayrton-senna-legend",
        "excerpt": "Ayrton Senna was more than a racing driver. He was an artist, a perfectionist, and a hero to millions.",
        "content": (
            "Ayrton Senna da Silva is widely regarded as the greatest Formula 1 driver of all time. The Brazilian's "
            "raw speed, fierce determination, and almost spiritual approach to driving set him apart from every other "
            "competitor of his era — and arguably any era.\n\n"
            "Senna's ability in the wet was legendary. His performance at the 1984 Monaco Grand Prix, where he hunted "
            "down race leader Alain Prost in torrential rain while driving an inferior Toleman, announced his arrival "
            "as a once-in-a-generation talent. His qualifying laps at Monaco became the stuff of legend — six poles "
            "in a row at the most demanding circuit on the calendar.\n\n"
            "His rivalry with Alain Prost is the defining story of late-1980s Formula 1. Their battles at McLaren "
            "in 1988 and 1989, and then as rivals at different teams in 1990 and 1993, produced some of the most "
            "dramatic moments the sport has ever seen.\n\n"
            "Senna won three World Championships — in 1988, 1990, and 1991 — all with McLaren. His 65 pole positions "
            "stood as a record for over a decade. But beyond the statistics, it was his passion and intensity that "
            "made him unforgettable.\n\n"
            "His tragic death at Imola in 1994 shocked the world and led to significant safety improvements in the "
            "sport. More than 30 years on, Senna remains the benchmark against which all other drivers are measured."
        ),
    },
    {
        "title": "Michael Schumacher: The Record Breaker Who Redefined Greatness",
        "slug": "michael-schumacher-legacy",
        "excerpt": "Michael Schumacher's relentless pursuit of perfection made him the most successful driver in F1 history.",
        "content": (
            "Michael Schumacher's seven World Championships and 91 Grand Prix victories made him the most statistically "
            "successful driver in Formula 1 history for over a decade. The German's combination of raw talent, "
            "physical fitness, and meticulous preparation set new standards for professionalism in the sport.\n\n"
            "Schumacher first caught the eye at the 1991 Belgian Grand Prix, where he qualified seventh on his debut "
            "for Jordan before being snapped up by Benetton. His first two championships, in 1994 and 1995, were won "
            "with Benetton and showcased a driver of extraordinary car control and racecraft.\n\n"
            "But it was his move to Ferrari in 1996 that defined his legacy. Taking on the challenge of rebuilding "
            "the most famous team in Formula 1, Schumacher spent four years turning Ferrari from also-rans into "
            "the dominant force. The championships that followed — five consecutive titles from 2000 to 2004 — "
            "represented the most sustained period of dominance the sport had ever seen.\n\n"
            "His work ethic was legendary. Schumacher would spend hours testing, often completing more laps than any "
            "other driver. He pushed himself physically harder than his competitors, recognising early that fitness "
            "would be a key differentiator in modern Formula 1.\n\n"
            "Whether you loved him or considered him controversial, there is no denying that Michael Schumacher "
            "changed Formula 1. His records stood for a generation, and his influence on how drivers approach the "
            "sport is felt to this day."
        ),
    },
    {
        "title": "Race Review: Drama and Controversy at the Latest Grand Prix",
        "slug": "latest-race-review",
        "excerpt": "The latest Grand Prix delivered everything fans could wish for — overtaking, strategy battles, and controversy.",
        "content": (
            "If you wrote the script for this weekend's Grand Prix, nobody would believe it. From a dramatic first-lap "
            "incident to a controversial penalty that decided the podium, this race had absolutely everything.\n\n"
            "The action started before the lights even went out, with a surprise grid penalty for one of the title "
            "contenders dropping them to the back of the top ten. That set the stage for a recovery drive that would "
            "become one of the stories of the race.\n\n"
            "At the front, the battle between the top two teams was intense. Different tyre strategies created "
            "uncertainty about who was truly in the lead, and the undercut proved devastatingly effective for those "
            "who pitted early. The virtual safety car period added another layer of complexity, bunching up the field "
            "and creating opportunities for those who had not yet stopped.\n\n"
            "The closing laps were breathtaking. A late safety car restart produced a five-lap sprint to the finish, "
            "with three cars fighting for the win. The eventual victor crossed the line by less than half a second, "
            "sparking celebrations in the garage and debate in the paddock.\n\n"
            "The stewards' decision to penalise one driver for exceeding track limits on the penultimate lap "
            "reshuffled the podium and left one team fuming. Expect this story to run well into next week."
        ),
    },
    {
        "title": "Lights Out in the Rain: Reviewing a Thrilling Wet-Weather Classic",
        "slug": "wet-weather-race-review",
        "excerpt": "When the rain came down, the latest Grand Prix turned into an instant classic with heroes and heartbreak.",
        "content": (
            "Rain in Formula 1 is the great equaliser. It strips away the advantages of the fastest car and puts "
            "the emphasis squarely on driver skill, bravery, and split-second decision-making. This weekend's race "
            "was a perfect example.\n\n"
            "The conditions were treacherous from the start. Standing water on the main straight made visibility "
            "almost non-existent for those behind, and within the first three laps, two cars had already aquaplaned "
            "off the circuit. The safety car was deployed twice in the opening ten laps.\n\n"
            "The tyre choice proved critical. Those who gambled on intermediate tyres while others stayed on full "
            "wets gained a massive advantage as the track began to dry. But the drying process was uneven, with "
            "some sections of the circuit remaining dangerously wet while others were almost bone dry.\n\n"
            "The midfield runners were the big winners, with two surprise podium finishers delighting their teams "
            "and fans around the world. The championship leader, meanwhile, salvaged a points finish from what "
            "could have been a disastrous weekend.\n\n"
            "Races like this remind us why we love Formula 1. When the rain comes, anything can happen."
        ),
    },
    {
        "title": "The 1976 Japanese Grand Prix: The Race That Defined a Rivalry",
        "slug": "1976-japanese-gp-greatest",
        "excerpt": "The 1976 Japanese Grand Prix saw Niki Lauda make the bravest decision in F1 history — to walk away.",
        "content": (
            "The 1976 Formula 1 season is one of the most dramatic in the sport's history, and its climax at the "
            "Japanese Grand Prix at Fuji Speedway remains one of the most extraordinary races ever held.\n\n"
            "The backdrop was remarkable. Niki Lauda, driving for Ferrari, had suffered horrific burns in a crash "
            "at the Nurburgring just weeks earlier. His recovery was nothing short of miraculous — he returned to "
            "racing within 40 days, his face still bandaged, his body still healing. He arrived in Japan with a "
            "three-point championship lead over James Hunt.\n\n"
            "Race day brought torrential rain. The conditions were so bad that several drivers protested against "
            "racing. The start was delayed, but eventually the cars were sent out on a waterlogged circuit with "
            "almost zero visibility.\n\n"
            "After just two laps, Lauda pulled into the pits and withdrew from the race. He later explained that "
            "he valued his life more than the championship. It was an act of extraordinary courage — not the "
            "courage of a man who races through danger, but the deeper courage of a man who knows when to stop.\n\n"
            "Hunt, meanwhile, drove brilliantly in the treacherous conditions. Despite a late tyre stop that dropped "
            "him down the order, he fought back to finish third — enough to take the championship by a single point.\n\n"
            "The 1976 season, immortalised in the film Rush, remains the gold standard for championship drama."
        ),
    },
    {
        "title": "Brazil 2008: The Last-Corner Championship",
        "slug": "brazil-2008-greatest-race",
        "excerpt": "Lewis Hamilton needed just one point. Glock went wide. The rest is history.",
        "content": (
            "The 2008 Brazilian Grand Prix is the most dramatic championship decider in modern Formula 1 history. "
            "Lewis Hamilton arrived at Interlagos needing to finish fifth or higher to clinch his first World "
            "Championship, regardless of what title rival Felipe Massa did.\n\n"
            "Massa, driving for Ferrari in front of his home crowd, was magnificent all weekend. He took pole "
            "position and led the race from start to finish, doing everything in his power to keep his championship "
            "hopes alive.\n\n"
            "Hamilton, meanwhile, was having a difficult afternoon. Running in the points but struggling for pace, "
            "he found himself shuffled back to sixth position in the closing stages. Sixth was not enough — he "
            "needed fifth.\n\n"
            "As Massa crossed the line to win the race, his family and team celebrated on the pit wall. For a few "
            "agonising seconds, it appeared that Massa was world champion. The Ferrari garage erupted in joy.\n\n"
            "But on the final corner of the final lap, Timo Glock — running on dry-weather tyres on a damp track — "
            "lost pace dramatically. Hamilton swept past into fifth place, taking the championship by a single point "
            "in the most heart-stopping finish imaginable.\n\n"
            "The contrasting emotions on the Ferrari and McLaren pit walls told the whole story. In the space of "
            "30 seconds, a championship had been won and lost. It remains the most dramatic conclusion to a "
            "Formula 1 season in history."
        ),
    },
    {
        "title": "The Evolution of F1 Safety: From Deadly Danger to Modern Protection",
        "slug": "f1-safety-evolution",
        "excerpt": "Formula 1 was once the most dangerous sport on earth. The journey to modern safety standards is remarkable.",
        "content": (
            "In the early decades of Formula 1, death was an ever-present companion. Between 1950 and 1994, more "
            "than 50 drivers lost their lives in Formula 1 events. The sport was extraordinarily dangerous, and "
            "drivers accepted that risk as part of the deal.\n\n"
            "The turning point came after the tragic weekend at Imola in 1994, when both Roland Ratzenberger and "
            "Ayrton Senna lost their lives. The shock of losing the sport's biggest star forced Formula 1 to "
            "confront its safety record and make fundamental changes.\n\n"
            "The improvements since then have been extraordinary. Circuit design evolved with larger run-off areas, "
            "better barriers, and improved marshalling. Car design changed dramatically — the survival cell concept, "
            "the HANS device, and improved helmet standards all contributed to making crashes survivable.\n\n"
            "The introduction of the Halo device in 2018 was initially controversial, with many fans and even some "
            "drivers criticising its appearance. But the Halo has since been credited with saving multiple lives, "
            "most notably at the 2020 Bahrain Grand Prix when Romain Grosjean walked away from a fiery crash that "
            "would have been fatal without it.\n\n"
            "Formula 1's safety journey is one of the sport's greatest achievements. The fact that drivers can now "
            "walk away from 200mph impacts that would have been fatal just decades ago is a testament to the "
            "engineers, doctors, and administrators who have made safety their mission."
        ),
    },
]


class Command(BaseCommand):
    help = "Seed the database with 12 F1 blog posts"

    def handle(self, *args, **options):
        try:
            author = User.objects.get(username="Murphy")
        except User.DoesNotExist:
            self.stderr.write(self.style.ERROR("User 'Murphy' not found. Create the superuser first."))
            return

        created_count = 0
        for post_data in POSTS:
            _, created = Post.objects.get_or_create(
                slug=post_data["slug"],
                defaults={
                    "title": post_data["title"],
                    "author": author,
                    "content": post_data["content"],
                    "excerpt": post_data["excerpt"],
                },
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {post_data['title']}"))
            else:
                self.stdout.write(f"Already exists: {post_data['title']}")

        self.stdout.write(self.style.SUCCESS(f"\nDone! {created_count} new posts created."))
