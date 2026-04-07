"""
MMG Brief Generator
====================
Uses the Anthropic API to generate creative briefs for each
monthly batch of HP memes and TikToks.

Creative direction: Maximum humor, current trends, HP always wins.
Reads history.json to avoid repeating formats or categories.
Returns structured briefs ready for the builders to consume.
"""

import json
import os
import anthropic
import random
from datetime import datetime

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


# ── Humor examples that hit the right tone ─────────────────────────────────
HUMOR_EXAMPLES = [
    # Meme examples
    "Drake meme: [disapprove] Buying off-brand ink and praying / [approve] HP Instant Ink auto-delivers before I even know I'm out",
    "Woman yelling at cat: Me screaming at my printer at 11pm / HP OfficeJet Pro that printed 47 docs today without complaint",
    "Two buttons sweating meme: Guy panicking choosing between 'buy cheap ink' and 'actually get work done' — HP Instant Ink removes the choice entirely",
    "Distracted boyfriend: Boyfriend (me) looking at 'cheap ink' / Girlfriend (my HP Spectre) giving me the look / Other girl labeled 'regret'",
    "This is fine dog: Me watching the Wi-Fi printer from 2009 fail during a deadline / HP OfficeJet Pro in the background: already done",
    "Expanding brain: Print one thing → print from phone → HP Instant Ink never runs out → I am the printer",
    "Stonks meme: Bought HP Spectre x360 → opened 47 tabs → it handled all of them → I own a business now. Stonks.",
    "POV meme: POV you're the off-brand ink cartridge watching HP Instant Ink pull up",
    "Roman Empire meme: Men think about their HP OMEN gaming rig every day. Every. Single. Day.",
    "Main character energy: Closed a deal from a coffee shop on HP Spectre x360 with 14 hours of battery. Main character behavior.",
    "NPC vs main character: NPC runs out of ink during final exam. Main character has HP Instant Ink.",
    "Sigma rule: A sigma never runs out of ink. A sigma has HP Instant Ink.",

    # TikTok examples
    "Green screen: Me using Shia LaBeouf NOT GONNA DO IT on every reason I've used to avoid setting up HP Instant Ink",
    "POV TikTok: POV you just realized HP Spectre x360 has better battery than your relationship",
    "Duet with office chaos video: 'meanwhile me with HP Instant Ink' — zero stress, auto-delivered",
    "Day in my life: 5am woke up, 6am printed boarding pass, 7am HP OMEN already booted, I eat chaos for breakfast",
    "Brain rot TikTok: What if your printer was sentient and it was the HP OfficeJet Pro and it just wanted to be appreciated",
    "Transformation: Before HP monitor setup vs after — same person, completely different threat level",
    "Storytime: The time my HP Instant Ink auto-delivered the day before a massive presentation. I am not crying. You are crying.",
    "Couple content: Him: we should get a printer. Her: we have one. The HP OfficeJet Pro at home:",
    "Skibidi: The HP OMEN gaming setup understood the assignment and left no crumbs",
]

TRENDING_FORMATS_2026 = [
    "roman_empire",          # 'Men think about X every day'
    "main_character",        # 'This is main character behavior'
    "npc_vs_main",          # NPC gets bad outcome, main character has HP
    "sigma_rule",           # Sigma grindset meme
    "brain_rot",            # Unhinged relatable humor
    "understood_assignment", # 'Ate and left no crumbs'
    "no_because_actually",   # 'No because actually why does the HP Spectre...'
    "delulu",               # 'Delulu is the solulu' — believing HP will save you
    "side_quest",           # 'Running out of ink is a side quest I refuse to accept'
    "rent_free",            # 'HP Instant Ink living rent free in my head'
    "very_demure",          # Very mindful, very demure approach to printing
    "it_girl",             # 'It girl energy: HP Spectre, oat milk, 14hr battery'
    "rizz",                # HP product has rizz
    "ate_no_crumbs",       # HP printer ate and left no crumbs
    "iykyk",               # If you know you know
    "pov_lifestyle",       # POV you just upgraded to HP
    "couple_relatable",    # Couple dynamics meme
    "this_is_fine",        # Chaos around, HP is fine
    "stonks",              # HP = profit
    "expanding_brain",     # Increasingly enlightened HP takes
    "distracted_boyfriend", # Classic but still fires
    "drake_approve",       # Always works
    "woman_yelling_cat",   # Always works
    "two_buttons",         # Sweating over decision HP solves
]


def generate_monthly_briefs(config: dict, history: dict) -> dict:
    """
    Generate creative briefs for the monthly batch.
    Returns: { "memes": [...], "tiktoks": [...] }
    """
    avoid_formats = history.get("do_not_repeat", {}).get("formats_last_3_months", [])
    avoid_categories = history.get("do_not_repeat", {}).get("category_last_month", [])
    all_categories = config["hp_categories"]
    available_categories = [c for c in all_categories if c not in avoid_categories]

    # Combine config formats with trending 2026 formats
    all_meme_formats = list(set(config["meme_formats"] + TRENDING_FORMATS_2026))
    all_tiktok_formats = list(set(config["tiktok_formats"] + TRENDING_FORMATS_2026))

    available_meme_formats = [f for f in all_meme_formats if f not in avoid_formats]
    available_tiktok_formats = [f for f in all_tiktok_formats if f not in avoid_formats]

    # Pick 3 random humor examples to seed inspiration
    selected_examples = random.sample(HUMOR_EXAMPLES, min(6, len(HUMOR_EXAMPLES)))
    current_month = datetime.now().strftime("%B %Y")

    prompt = f"""You are the head creative at Motivated Mind Group (MMG), making social media
content for HP Inc. consumer products. Think: Duolingo owl energy meets HP.
Unhinged but brand-safe. Funny first, product second.

MONTH: {current_month}

GENERATE:
- 3 TikTok briefs
- 4 Meme briefs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CREATIVE RULES — READ THESE CAREFULLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HUMOR LEVEL: 8/10. We want laugh-out-loud relatable, not chuckle-and-scroll.
The joke lands FIRST. The HP product is the reason the joke works.

HP IS ALWAYS THE HERO — but in a funny way:
- HP doesn't save the day like a superhero. HP saves the day because it
  just quietly worked while everything else failed.
- Off-brand ink, slow printers, dead batteries — these are the villains.
- HP products are the main character energy in a sea of NPCs.
- Never mock HP. Celebrate HP through the lens of chaos it prevents.

CURRENT TRENDS TO USE (pick what fits):
- Roman Empire ("Men think about HP OMEN every day")
- Main character / NPC energy
- Brain rot humor (unhinged, fast, absurdist)
- Sigma grindset (HP is the sigma choice)
- "Understood the assignment / ate and left no crumbs"
- POV formats with very specific relatable scenarios
- "No because WHY does the HP Spectre have better battery than my will to live"
- Couple dynamics (him vs her printer decisions)
- Very demure, very mindful (applied to printing)
- Rizz / delulu culture
- Side quest humor ("running out of ink is a side quest I refuse")
- It girl energy meets HP products

EXAMPLE TONES THAT WORK:
{chr(10).join('- ' + ex for ex in selected_examples)}

WHAT MAKES GREAT HP CONTENT:
- Specific, relatable moments: printing boarding pass at 11pm,
  running out of ink the day of a deadline, gaming at 3am
- Real HP product names: HP Spectre x360, HP OMEN, HP OfficeJet Pro,
  HP Instant Ink, HP LaserJet, HP 27" monitor
- The contrast: chaos around them / HP product performing flawlessly
- Self-aware Gen Z humor that pokes fun at itself while loving the product
- Never say "quality" or "reliable" — SHOW IT through the joke

FORMAT RULES:
- Cover DIFFERENT HP categories: {available_categories} (avoid: {avoid_categories})
- Use DIFFERENT formats within this batch
- No repeats from last 3 months: {avoid_formats}
- Available meme formats: {available_meme_formats[:15]}
- Available TikTok formats: {available_tiktok_formats[:10]}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT FORMAT (JSON only, no preamble, no markdown):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{{
  "tiktoks": [
    {{
      "type": "TikTok",
      "category": "category-name-here",
      "format": "format_name_here",
      "title": "Short punchy title that would work as a caption",
      "hook": "First 2 seconds — this must stop the scroll. Be funny or weird immediately.",
      "concept": "2-3 sentences describing the video. Make it specific and visual.",
      "top_text": "Text overlay at top (punchy, conversational)",
      "bottom_text": "Text overlay at bottom (the punchline or HP payoff)",
      "suggested_audio": "Specific trending audio or sound that fits the vibe",
      "hp_product_featured": "Specific HP product name (not just 'HP printer')",
      "call_to_action": "CTA — funny not corporate (e.g. 'link in bio if you're built different')"
    }}
  ],
  "memes": [
    {{
      "type": "Meme",
      "category": "category-name-here",
      "format": "format_name_here",
      "title": "Short punchy title",
      "top_text": "TOP MEME TEXT — ALL CAPS, PUNCHY, THE SETUP",
      "bottom_text": "BOTTOM TEXT — ALL CAPS, THE PUNCHLINE, HP IS THE ANSWER",
      "concept": "1-2 sentences on the visual. What does the meme template show? Be specific.",
      "hp_product_featured": "Specific HP product name",
      "humor_note": "One sentence explaining why this is funny / why it hits",
      "color_scheme": "dark_blue|light|dark|hp_branded",
      "background_style": "Description of visual style"
    }}
  ]
}}"""

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=3000,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.content[0].text.strip()

    # Strip any markdown fences
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    if raw.endswith("```"):
        raw = raw.rsplit("```", 1)[0]

    briefs = json.loads(raw.strip())

    # Validate counts
    if len(briefs["tiktoks"]) < 3:
        raise ValueError(f"Expected 3 TikTok briefs, got {len(briefs['tiktoks'])}")
    if len(briefs["memes"]) < 4:
        raise ValueError(f"Expected 4 meme briefs, got {len(briefs['memes'])}")

    return briefs


def preview_briefs():
    """
    Test the brief generator and print output.
    Run directly: python brief_generator.py
    """
    from dotenv import load_dotenv
    import pathlib

    load_dotenv(pathlib.Path(__file__).parent.parent / ".env")

    sample_config = {
        "hp_categories": [
            "Ink-InstantInk-Tank",
            "Laptops-Desktops-PCs",
            "Printers-Scanners-MFP",
            "Monitors",
            "Accessories"
        ],
        "meme_formats": [
            "drake_approve_disapprove", "iykyk", "pov", "comparison_before_after",
            "nobody_hp", "green_screen_reaction", "couple_relatable",
            "distracted_boyfriend", "this_is_fine", "expanding_brain",
            "woman_yelling_at_cat", "stonks"
        ],
        "tiktok_formats": [
            "green_screen_celebrity", "pov_lifestyle", "duet_trend",
            "day_in_life", "comparison_reveal", "transformation",
            "storytime_hook", "tutorial_twist"
        ]
    }

    sample_history = {
        "do_not_repeat": {
            "formats_last_3_months": ["drake_approve_disapprove", "pov_lifestyle"],
            "category_last_month": ["Ink-InstantInk-Tank", "Laptops-Desktops-PCs"]
        }
    }

    print("Generating briefs with new humor direction...\n")
    briefs = generate_monthly_briefs(sample_config, sample_history)

    print("=" * 60)
    print("TIKTOKS")
    print("=" * 60)
    for i, t in enumerate(briefs["tiktoks"], 1):
        print(f"\nTikTok #{i}: {t['title']}")
        print(f"  Format: {t['format']} | Category: {t['category']}")
        print(f"  Hook: {t['hook']}")
        print(f"  Concept: {t['concept']}")
        print(f"  Product: {t['hp_product_featured']}")
        print(f"  Audio: {t['suggested_audio']}")

    print("\n" + "=" * 60)
    print("MEMES")
    print("=" * 60)
    for i, m in enumerate(briefs["memes"], 1):
        print(f"\nMeme #{i}: {m['title']}")
        print(f"  Format: {m['format']} | Category: {m['category']}")
        print(f"  Top: {m['top_text']}")
        print(f"  Bottom: {m['bottom_text']}")
        print(f"  Product: {m['hp_product_featured']}")
        if m.get('humor_note'):
            print(f"  Why it works: {m['humor_note']}")

    return briefs


if __name__ == "__main__":
    preview_briefs()
