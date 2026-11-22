"""All website copy and sourced statistics in one place, so the team can edit text without touching layout code."""
from __future__ import annotations

HERO_STRIP = [
    ("9", "people interviewed along the food chain"),
    ("$0", "upfront cost for farms"),
    ("14 days", "from delivery to farm payment"),
    ("1", "invoice for every delivery"),
]

HOOK = [
    "Think about tonight's dinner. How would you feel if you knew the carrots on your plate were picked yesterday, "
    "twenty minutes from here, by a farmer whose name you could read?",
    "Now ask yourself, when did you last actually know that? The label says Québec, but which farm, and when it was "
    "picked, stays a mystery.",
]

GAP_SHORT = ("Shoppers, specialty grocers and chefs want local food they can trace. Small farms have it, but not the "
             "time, volume or cold transport to serve a buyer every week. We connect the two.")

PROBLEM = [
    "We spoke to nine people along the food chain, and one story kept coming back. The shoppers we interviewed told "
    "us they care. They want to know where their food comes from and when it was picked. Specialty grocers and "
    "chef-driven restaurants want to offer exactly that.",
    "But between them and the farms, there is a gap.",
]
QUOTE = ("We already tried selling to restaurants and big markets, but it's hard, there are only two of us.",
         "Ferme Teasdale")
PROBLEM_AFTER = [
    "A small farm has the produce, but not the time, the volume or the cold transport to serve a buyer every week. "
    "And no grocer wants to chase a dozen small suppliers with a dozen invoices. So local stays patchy, seasonal and "
    "hard to prove.",
    "The real problem is not that nobody wants local food. There is simply no easy way to connect small farms with "
    "the buyers who want them.",
]

SOLUTION = ("We are the middleman. Farms join us, and restaurants and grocers order in one place. We handle ordering, "
            "invoicing and traceability, and we subcontract the delivery.")

BENEFITS = [
    ("1", "One order", "Order from several local farms in one place."),
    ("2", "One invoice", "A single invoice and a single point of contact, instead of a dozen."),
    ("3", "One delivery", "We pool the produce and a cold carrier brings it. A QR code on every box lets you meet the farm."),
]

STEPS = [
    ("1", "Farms join", "We list each farm with its story, its crops and its harvest calendar."),
    ("2", "Buyers order weekly", "Choose what you need from several farms and place a single order."),
    ("3", "One delivery arrives", "We pool the produce, a cold carrier delivers it, and you get one invoice."),
]

MODEL = [
    ("$0", "Farms pay nothing upfront."),
    ("about 18%", "is what we keep from each invoice."),
    ("14 days", "is how fast farms are paid."),
]
MODEL_NOTE = ("Our model works if one delivery route reaches about ten grocers ordering around three hundred dollars "
              "each, and if grocers will pay a 10 to 20 percent premium for verified local food.")

PILOT = ("We are starting small. A first trial with two or three farms and one grocer, to prove that local food can "
         "arrive fresh, on time, with a farmer's name on the box. It is a challenge, and we know it. But we are ready "
         "to take it on, because it is worth it. For the farmers, for the environment, and for everyone who wants to "
         "know what is on their plate. Once it works, we will grow to more farms, more buyers and more products.")
PILOT_ASKS = [("5", "grocers"), ("5", "farms"), ("1", "cold-chain partner")]

FAQ = [
    ("What does it cost a farm?",
     "Nothing upfront. We keep about 18% of each sale, and farms are paid within 14 days of delivery. "
     "This is a working assumption that we are testing in our pilot."),
    ("What do grocers and restaurants pay?",
     "One invoice per delivery. Orders below a minimum carry a small delivery fee, and buyers who commit to the season "
     "get the best terms."),
    ("Do I have to drop my current distributor?",
     "No. We work alongside your distributor and add local farms to what you already offer."),
    ("Which products do you start with?",
     "Fruits and vegetables. We will add other farm products once the first routes run smoothly."),
    ("Where do you deliver?",
     "We collect from farms in Montérégie and deliver to the Montréal area. We will confirm the first delivery zone "
     "with our first grocer."),
    ("How does traceability work?",
     "Every box carries a QR code. A scan opens a short page about the farm, the farmer and the harvest."),
]

STATS = [
    dict(num="79.6%", text='of Quebecers see the word "local" on a label as a plus.',
         src="Observatoire de la consommation responsable, survey of 1,100 Quebecers.",
         url="https://www.equiterre.org/en/articles/news-buying-local-biggest-quebec-trend-in-responsible-consumption"),
    dict(num="44%",
         text="of Quebecers say they bought more local products or visited local retailers more often since the tariffs.",
         src="NIQ Canada survey, December 2025, as presented by MAPAQ.",
         url="https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/agriculture-pecheries-alimentation/politique-bioalimentaire/rencontres-partenaires/PR_nouveaux_consommateurs_marches_MAPAQ.pdf"),
]

TESTS = [
    ("Premium", "Will grocers commit to weekly orders at a 10 to 20 percent premium for verified local food?"),
    ("Margin", "Does our commission cover cold delivery and the cost of running the route?"),
    ("Supply", "Can several small farms together deliver consistent volume and quality every week?"),
]


MODEL_PARTS = [
    ("Farms", ["Pay nothing upfront.", "Earn when they sell.", "Are paid within 14 days of delivery."]),
    ("Grocers and restaurants", ["Pay one invoice per delivery.", "Pay a small delivery fee below a minimum order.",
                                 "Get the best terms with a pre-season commitment."]),
    ("Us", ["Keep about 18% of each invoice.", "Subcontract cold transport.",
            "Bridge the payment gap with a Futurpreneur loan or a line of credit."]),
]

MUST_BE_TRUE = [
    "One delivery route reaches about ten grocers ordering around three hundred dollars each.",
    "Grocers will pay a 10 to 20 percent premium for verified local food.",
    "Several small farms can deliver consistent volume and quality every week.",
]


PRIVACY = ("We use your name and email only to contact you about the first season trial. "
           "We do not share them, and you can ask us to delete them at any time.")
FEEDBACK_LABEL = "What would you change about this page? (optional)"
POLL_PRIVACY = "Your answer is anonymous. We store only a yes or a no."
