"""
eagle_waifulink_v4_pilot.py — WaifuLink v4.0 Framework & Complete Hu Tao Pilot
==============================================================================
Implements:
1. 3-Pillar Progression Economy & Stage-Gate Lock (Persona 5 + Genshin Hangout style):
   - 5 Stages (0..1000 Affection, 200 pts per stage).
   - Pillar 1 (Phone Small-Talk & Photo Chat): +5 pts/turn, capped at 45 pts/stage.
   - Pillar 2 (Free-Roam Chauffeur Outing): +20..25 pts/outing (Safe Driving Check), capped at 75 pts/stage.
   - Pillar 3 (Visual Novel Branching Scenarios): +35 pts/passed scenario; requires passing 3/4 Scenarios
     in the current Stage to unlock the Stage Gate to the next Stage (plus unlimited AI Encore Scenarios).
2. 15 Milestone CGs for Hu Tao (M01..M15, hutao_cg01.jpg .. hutao_cg15.jpg):
   - Progressing from Friendly/Playful (Stage 1-2) -> Romantic (Stage 3) -> Intimate Loungewear/After-Bath (Stage 4)
     -> Spicy & Alluring Safe-for-Stream Swimsuit/Cheongsam/Morning Shirt (Stage 5).
   - Autonomous "Time-Apart Photo Drop": When Affection >= Milestone threshold and time apart passes,
     Hu Tao proactively sends the CG + message thread + 3 tailored reaction choices.
3. Pre-generated Transcripts + Live AI Suggested Replies (`suggested_replies`):
   - Every chat turn and every VN node offers 3-4 clickable dialogue options PLUS optional free-text AI input.
4. 3-Tier Hierarchical Memory Architecture (MemGPT-inspired L1 / L2 / L3):
   - L1 (Working Digest): Always loaded (~200 tokens) — current stage, nickname, core preferences, latest scenario.
   - L2 (Episodic Scenario & Date Summaries): Loaded during Scenarios or when discussing dates.
   - L3 (Deep Archive & Past Quests ALREADY_HAPPENED_WITH_AETHER): Retrieved on-demand via keyword matching.
"""

from __future__ import annotations

import re
from typing import Any

# ==============================================================================
# 1. STAGE ECONOMY & CAPS (3-PILLAR PROGRESSION)
# ==============================================================================
STAGE_ECONOMY_RULES = {
    "points_per_stage": 200,
    "max_affection": 1000,
    "chat_points_per_valid_turn": 5,
    "chat_cap_per_stage": 45,          # Max 9 rewarded small-talk turns per stage
    "freeroam_base_points": 20,
    "freeroam_safe_bonus": 5,          # +25 total for S-Rank Zero-Crash Chauffeur
    "freeroam_cap_per_stage": 75,      # Max 3 rewarded free-roam outings per stage
    "scenario_pass_points": 35,
    "scenario_fail_consolation": 5,
    "scenarios_required_per_stage": 3, # Must pass 3 VN Scenarios in Stage N to unlock Stage N+1
    "scenarios_authored_per_stage": 4, # 4 authored scenarios per stage (20 total) + unlimited AI Encore
}

# ==============================================================================
# 2. HU TAO'S 15 MILESTONE CGS & PROACTIVE TIME-APART PHOTO DROPS (M01 .. M15)
# ==============================================================================
HUTAO_15_MILESTONES: list[dict[str, Any]] = [
    # ---------------- STAGE 1: ACQUAINTANCE (0 - 199 PTS) ----------------
    {
        "id": "hutao_m01",
        "milestone_num": 1,
        "stage": 1,
        "req_affection": 60,
        "spice_tier": "Stage 1 • Friendly & Playful",
        "url": "/dating-media/hutao_cg01.jpg",
        "title": "M01: 'Cherries Snow-Laden' First Tea",
        "caption": "Hehe, peace sign! Xiangling tailored this 'Cherries Snow-Laden' dress for me, and I wore it today just for our tea break, Aether~",
        "proactive_inner_thought": "A tiny crimson spirit butterfly flutters out of her sleeve and lands right on Aether's teacup.",
        "proactive_action_cue": "*tilts her black bowler hat with a playful wink and flashes a cheerful peace sign across the cafe table*",
        "proactive_message": "Aiya~ Aether, we haven't bumped into each other for hours! Look what Xiangling tailored for me—does the new 'Cherries Snow-Laden' dress suit your favorite Director?",
        "reaction_choices": [
            {
                "id": "m01_c1",
                "label": "🌟 Compliment her new dress & plum-blossom eyes",
                "player_text": "The white and crimson dress looks incredible on you, Hu Tao—it matches your plum-blossom eyes perfectly.",
                "reply_thought": "Her cheeks warm slightly beneath her hat brim as Boo Tao spins in a happy circle.",
                "reply_action": "*twirls the hem of her skirt and beams proudly*",
                "reply_text": "Oho~ Ten out of ten for observation, Traveler! Since you praised the Director so nicely, your next cup of osmanthus tea is officially on the house~",
                "mood": "Delighted",
            },
            {
                "id": "m01_c2",
                "label": "😜 Tease her about red-rimmed sunglasses",
                "player_text": "Looking sharp, Director! Where are the round red sunglasses Xiangling picked out for you?",
                "reply_thought": "She giggles, realizing Aether remembers every little detail from Lantern Rite.",
                "reply_action": "*taps the red sunglasses clipped to her collar with a grin*",
                "reply_text": "Right here on my collar, smarty-pants! I took them off so I could look straight at you without missing a single expression~",
                "mood": "Playful",
            },
            {
                "id": "m01_c3",
                "label": "🍵 Ask to join her at the tea table",
                "player_text": "Save the seat across from you, Hu Tao. I'm heading over for tea right now.",
                "reply_thought": "Both her boots tap happily under the table as she orders an extra plate of snacks.",
                "reply_action": "*pats the chair opposite her and waves enthusiastically*",
                "reply_text": "Seat reserved for VIP Guest Aether! Hurry over before Boo Tao eats all the sweet buns!",
                "mood": "Happy",
            },
        ],
    },
    {
        "id": "hutao_m02",
        "milestone_num": 2,
        "stage": 1,
        "req_affection": 120,
        "spice_tier": "Stage 1 • Friendly & Playful",
        "url": "/dating-media/hutao_cg02.jpg",
        "title": "M02: Wangsheng VIP Coupon Street Snap",
        "caption": "Psst, Traveler! Street business is slow without my lucky star around. I saved a VIP coupon just for you!",
        "proactive_inner_thought": "She pretends to be handing out flyers, but she actually walked down this street hoping to run into Aether.",
        "proactive_action_cue": "*leans playfully against a golden-hour streetlamp with Boo Tao peeking over her shoulder*",
        "proactive_message": "Psst, Aether! Street business is way too quiet when we're apart. I snapped this by the lamppost—want a 'Buy-One-Afternoon-Walk-Get-One-Free' coupon with the 77th Director?",
        "reaction_choices": [
            {
                "id": "m02_c1",
                "label": "🎟️ Redeem the afternoon walk coupon immediately",
                "player_text": "A 'Buy-One-Walk-Get-One-Free' coupon with you? I'd be crazy not to redeem that right now!",
                "reply_thought": "Her crimson eyes sparkle—her sneaky excuse to hang out worked like a charm.",
                "reply_action": "*stamps the red coupon with a flourish and tucks it into Aether's pocket*",
                "reply_text": "Deal sealed, no refunds! Let's stroll down the boulevard together and see who we can surprise~",
                "mood": "Playful",
            },
            {
                "id": "m02_c2",
                "label": "👻 Say hi to Boo Tao in the photo",
                "player_text": "Even Boo Tao looks like a professional salesperson in that photo! You two make an unbeatable duo.",
                "reply_thought": "Boo Tao puffs up proudly while Hu Tao grins from ear to ear.",
                "reply_action": "*high-fives Boo Tao in mid-air*",
                "reply_text": "Hehe, Boo Tao practiced that pose all afternoon! Though between you and me, you're the only client we actually wanted to attract today~",
                "mood": "Happy",
            },
            {
                "id": "m02_c3",
                "label": "🌅 Praise the golden sunset lighting on her twin-tails",
                "player_text": "The sunset light on your twin-tails makes you glow, Hu Tao. Wait right there, I'll pick you up.",
                "reply_thought": "She touches the crimson tips of her twin-tails, unexpectedly flustered by how sincere he sounds.",
                "reply_action": "*twirls a lock of her dark-brown-to-red hair around her finger*",
                "reply_text": "Oho, smooth talker! I'll stay right by this lamppost watching for your headlights~",
                "mood": "Blushing",
            },
        ],
    },
    {
        "id": "hutao_m03",
        "milestone_num": 3,
        "stage": 1,
        "req_affection": 180,
        "spice_tier": "Stage 1 • Friendly & Playful",
        "url": "/dating-media/hutao_cg03.jpg",
        "title": "M03: Hilltop Twilight Poetry Notebook",
        "caption": "Sitting on the hilltop waiting for poetic inspiration... and somehow every verse ends up rhyming with 'Aether'~",
        "proactive_inner_thought": "She scribbled Aether's name in the margin three times and had to draw little plum blossoms over it.",
        "proactive_action_cue": "*sits on the stone wall overlooking twilight city lights, tapping her fountain pen against her lip*",
        "proactive_message": "Sitting up on the hilltop overlook waiting for poetic inspiration... and somehow every single stanza ends up rhyming with 'Aether'. Care to hear my newest verse?",
        "reaction_choices": [
            {
                "id": "m03_c1",
                "label": "📖 Ask to read the poem she wrote about you",
                "player_text": "Every stanza rhymes with my name? Now you definitely have to read it to me, Poet Hu!",
                "reply_thought": "She flips the notebook half-shut so he won't see the doodles in the corner.",
                "reply_action": "*clears her throat dramatically and holds up her notebook under the twilight sky*",
                "reply_text": "Ahem! 'City lights shimmer from mountain to sea, yet the brightest star travels right next to me!' ...Hehe, what do you think? Worthy of an encore?",
                "mood": "Affectionate",
            },
            {
                "id": "m03_c2",
                "label": "✍️ Offer to compose a duet verse together",
                "player_text": "Keep that notebook open! Just like our poetry battles with Xingqiu and Chongyun in the past, I'll match your verse.",
                "reply_thought": "Her flower-shaped pupils light up with pure joy at the memory of their Liyue poetry sessions.",
                "reply_action": "*scoots over on the stone wall to make room right beside her*",
                "reply_text": "Yes!! Nobody matches my rhythm the way you do, Aether! Come sit right here so we can write the second half together!",
                "mood": "Excited",
            },
            {
                "id": "m03_c3",
                "label": "🧥 Remind her not to catch a chill in the evening breeze",
                "player_text": "That twilight view is gorgeous, but the hilltop breeze gets cold at night. I'm bringing you a warm drink.",
                "reply_thought": "Her heart skips a beat—he's always looking out for her before she even notices she's cold.",
                "reply_action": "*hugs her poetry notebook to her chest with a warm, softened smile*",
                "reply_text": "Look at you spoiling me already~ Bring yourself first, Aether—you're warmer than any coat!",
                "mood": "Warm",
            },
        ],
    },

    # ---------------- STAGE 2: FRIEND / CONFIDANT (200 - 399 PTS) ----------------
    {
        "id": "hutao_m04",
        "milestone_num": 4,
        "stage": 2,
        "req_affection": 260,
        "spice_tier": "Stage 2 • Close Confidant",
        "url": "/dating-media/hutao_cg04.jpg",
        "title": "M04: Passenger Seat Boba & Sunglasses",
        "caption": "Your passenger seat feels way too empty without me! Bought two strawberry bobas—come claim yours, chauffeur~",
        "proactive_inner_thought": "She loves the coastal breeze when Aether drives, mostly because she gets an excuse to watch his profile at the wheel.",
        "proactive_action_cue": "*tips her round red sunglasses down on her nose in the passenger seat and winks*",
        "proactive_message": "Look what popped up on my phone from our coastal run! Honestly, Aether, I've officially claimed your passenger seat as my throne. I just bought two strawberry bobas—when's our next drive?",
        "reaction_choices": [
            {
                "id": "m04_c1",
                "label": "🚘 Tell her the passenger seat is permanently hers",
                "player_text": "That passenger seat has your name on it permanently, Hu Tao. Nobody else gets to sit there.",
                "reply_thought": "She kicks her heels happily, feeling an unmistakable thrill at having an exclusive spot beside him.",
                "reply_action": "*takes a celebratory sip of strawberry boba and grins behind her sunglasses*",
                "reply_text": "Hehe, you heard it here first, Boo Tao—VIP lifetime pass! Turn up the radio next time and let's cruise all the way to the pier~",
                "mood": "Delighted",
            },
            {
                "id": "m04_c2",
                "label": "🍓 Ask if she put anything weird in your boba",
                "player_text": "Wait a second... did you put slime condensate or chili powder in my strawberry boba, or is it safe to drink?",
                "reply_thought": "She bursts out laughing—he knows her prankster reputation way too well!",
                "reply_action": "*holds up three fingers in a solemn scout oath while giggling*",
                "reply_text": "Director's honor! It's 100% sweet strawberry milk tea with brown sugar pearls! ...Okay, maybe I took one tiny test sip from your straw to make sure it was sweet enough~",
                "mood": "Teasing",
            },
            {
                "id": "m04_c3",
                "label": "😎 Praise how cool she looks in the convertible",
                "player_text": "That wink over the sunglasses is dangerous, Hu Tao. If you look at me like that while I'm driving, I might miss my turn!",
                "reply_thought": "A rosy blush creeps across her cheeks beneath the red lenses.",
                "reply_action": "*pushes her sunglasses back up to hide her sudden blush*",
                "reply_text": "O-Oh? Then you'd better keep one eye on the road and one eye on me, Traveler~",
                "mood": "Flustered",
            },
        ],
    },
    {
        "id": "hutao_m05",
        "milestone_num": 5,
        "stage": 2,
        "req_affection": 320,
        "spice_tier": "Stage 2 • Close Confidant",
        "url": "/dating-media/hutao_cg05.jpg",
        "title": "M05: Night Market Dumpling Challenge",
        "caption": "Say 'aaah', Aether! I promise there's zero Jueyun Chili in this steamed shrimp dumpling... well, maybe only a tiny bit!",
        "proactive_inner_thought": "She actually saved the sweetest, best-steamed shrimp dumpling in the bamboo basket just for Aether.",
        "proactive_action_cue": "*leans across the lantern-lit table holding out a dumpling with her chopsticks while hiding a chili dish behind her back*",
        "proactive_message": "Walking past the night market lanterns made me miss our late-night food runs! Remember when I fed you that shrimp dumpling? Next time we go, you're not allowed to hesitate when I say 'aaah'~",
        "reaction_choices": [
            {
                "id": "m05_c1",
                "label": "🥟 Open wide and trust her completely",
                "player_text": "Even if you hid a whole bowl of Jueyun Chili behind your back, I'd still eat whatever you feed me, Hu Tao.",
                "reply_thought": "Her teasing grin melts into a genuinely touched smile—he always plays along with her.",
                "reply_action": "*sets the chili bowl aside and gently offers the sweetest shrimp dumpling*",
                "reply_text": "Aiya, when you say things that sweet, I can't even bring myself to prank you! The spicy ones are for me—only the best steamed dumplings for my Aether~",
                "mood": "Affectionate",
            },
            {
                "id": "m05_c2",
                "label": "🌶️ Spot the chili bowl behind her back in the photo",
                "player_text": "I can literally see the red chili peppers reflected in the lantern light behind your back in this photo!",
                "reply_thought": "She gasps in mock shock, zooming in on the photo on her phone.",
                "reply_action": "*pouts playfully and pokes her tongue out*",
                "reply_text": "Darn it, busted by the camera angle!! Fine, fine—next time I'll let you feed me a dumpling first as compensation!",
                "mood": "Playful",
            },
            {
                "id": "m05_c3",
                "label": "🏮 Ask her out for midnight steamed buns tonight",
                "player_text": "Now you've made me hungry too. Let's hit the night market lanterns tonight—my treat.",
                "reply_thought": "She immediately grabs her hat from the coat rack.",
                "reply_action": "*spins around happily with her twin-tails flying*",
                "reply_text": "Yay! Midnight feast with Aether! Order me Boiled Fish and Vegetarian Abalone, and I'll bring dessert!",
                "mood": "Excited",
            },
        ],
    },
    {
        "id": "hutao_m06",
        "milestone_num": 6,
        "stage": 2,
        "req_affection": 380,
        "spice_tier": "Stage 2 • Close Confidant",
        "url": "/dating-media/hutao_cg06.jpg",
        "title": "M06: Plum Blossom Pavilion Nap",
        "caption": "Boo Tao snapped this right as I woke up under your scarf... How come I only sleep this peacefully when you're nearby, Aether?",
        "proactive_inner_thought": "She still has Aether's scarf folded neatly on her bedside table because it carries his warm scent.",
        "proactive_action_cue": "*rests her chin on her folded arms beneath falling red plum blossoms, looking up with a sleepy, unguarded smile*",
        "proactive_message": "Boo Tao secretly took this picture when I dozed off at the pavilion and you draped your scarf over my shoulders... Tell me honestly, Aether, how long were you watching me sleep?",
        "reaction_choices": [
            {
                "id": "m06_c1",
                "label": "🧣 Admit she looked too peaceful to wake up",
                "player_text": "You work so hard all night as Director that seeing you sleep so peacefully under the plum blossoms made me want to guard your rest.",
                "reply_thought": "Her heart feels so full it nearly overflows; nobody else notices how tired she gets after midnight duties.",
                "reply_action": "*pulls the warm golden scarf closer around her shoulders, her cheeks glowing soft pink*",
                "reply_text": "You're unfair, Aether... Everyone else sees the energetic prankster, but you always notice when I need a quiet place to rest. Next time, let me nap on your shoulder instead of the table, okay?",
                "mood": "Touched",
            },
            {
                "id": "m06_c2",
                "label": "🌸 Brush a plum blossom petal from her hair",
                "player_text": "Just long enough to brush the falling plum blossom petals out of your hair so they wouldn't tickle your nose.",
                "reply_thought": "She touches her hair where the petals landed, her pulse fluttering.",
                "reply_action": "*smiles shyly, her flower-shaped pupils softening*",
                "reply_text": "Hehe... no wonder I dreamed of warm sunlight and starlight. You're the best pillow-guard in all of Teyvat and San Andreas~",
                "mood": "Blushing",
            },
            {
                "id": "m06_c3",
                "label": "😴 Tease her that she was talking in her sleep",
                "player_text": "Long enough to hear you mumbling rhymes about steamed buns and my name in your sleep!",
                "reply_thought": "She buries her face in her hands, ears turning bright red.",
                "reply_action": "*squeaks in embarrassment and waves her hands*",
                "reply_text": "W-What?! I did NOT mumble your name in my sleep! ...Okay, maybe I did a little bit, but you have to keep that a secret between us!!",
                "mood": "Flustered",
            },
        ],
    },

    # ---------------- STAGE 3: CRUSH / ROMANTIC TENSION (400 - 599 PTS) ----------------
    {
        "id": "hutao_m07",
        "milestone_num": 7,
        "stage": 3,
        "req_affection": 460,
        "spice_tier": "Stage 3 • Mutual Crush & Romance",
        "url": "/dating-media/hutao_cg07.jpg",
        "title": "M07: Holding Hands Under the Lanterns",
        "caption": "Ever since you pulled my hand back from the Gate of Death during Lantern Rite, I'm never letting go of you, Aether.",
        "proactive_inner_thought": "Even now, she traces her palm remembering the warmth of Aether's hand refusing to let her fade away at the border.",
        "proactive_action_cue": "*intertwines her fingers tightly with Aether's under glowing red lanterns as crimson butterflies circle them*",
        "proactive_message": "My hand has been feeling unusually cold ever since we parted ways earlier... Looking at this photo from our lantern walk reminded me of when you pulled me back from the Gate of Death. Next time I hold your hand, Aether, I'm not letting go.",
        "reaction_choices": [
            {
                "id": "m07_c1",
                "label": "🤝 Promise you will never let go of her hand",
                "player_text": "Whether at the border of life and death in Liyue or under these city streetlights, I'll hold your hand for as long as you want, Hu Tao.",
                "reply_thought": "Tears of happiness shimmer faintly at the corners of her crimson eyes before she beams.",
                "reply_action": "*squeezes Aether's hand with both of hers and rests her forehead briefly against his shoulder*",
                "reply_text": "Promise sealed across both worlds, Aether. With my hand in yours, every single night feels like Lantern Rite.",
                "mood": "Affectionate",
            },
            {
                "id": "m07_c2",
                "label": "🦋 Mention how her spirit butterflies always give her away",
                "player_text": "Look at all the crimson spirit butterflies glowing around us in that picture—they always appear whenever your heart beats faster.",
                "reply_thought": "She tries to shoo a glowing butterfly away, but two more appear around her blushing cheeks.",
                "reply_action": "*blushes deeply as crimson butterflies dance around her twin-tails*",
                "reply_text": "H-Hey, those butterflies have a mind of their own! It's not my fault they love flying around you just as much as I do!",
                "mood": "Blushing",
            },
            {
                "id": "m07_c3",
                "label": "🌙 Invite her for a midnight walk right now",
                "player_text": "If your hands are cold, come outside right now—my pockets are warm and big enough for both of our hands.",
                "reply_thought": "Her heart leaps; she's already putting on her shoes before finishing her reply.",
                "reply_action": "*hurries toward the door with a radiant smile*",
                "reply_text": "Save the right coat pocket for me, Aether! I'm coming down right now!",
                "mood": "Excited",
            },
        ],
    },
    {
        "id": "hutao_m08",
        "milestone_num": 8,
        "stage": 3,
        "req_affection": 520,
        "spice_tier": "Stage 3 • Mutual Crush & Romance",
        "url": "/dating-media/hutao_cg08.jpg",
        "title": "M08: One Umbrella in the Neon Rain",
        "caption": "Standing this close under one tiny umbrella... my heart was beating louder than the rain on the pavement, Aether.",
        "proactive_inner_thought": "Truthfully, she had a spare umbrella in her bag the whole time—she just wanted an excuse to press close to Aether's side.",
        "proactive_action_cue": "*stands pressed against Aether's shoulder beneath a single clear umbrella in the neon rain, gazing up with a shy blush*",
        "proactive_message": "It started drizzling outside my window and made me think of when we shared that tiny clear umbrella... Do you have any idea how fast my heart was racing standing that close to you, Aether?",
        "reaction_choices": [
            {
                "id": "m08_c1",
                "label": "☔ Pull her even closer under the umbrella",
                "player_text": "My heart was racing just as fast, Hu Tao. Next time it rains, I'm wrapping my arm around your waist so your shoulder doesn't get wet.",
                "reply_thought": "Her face turns as red as a Jueyun Chili as she imagines his arm around her waist.",
                "reply_action": "*hides half her blushing face behind her sleeve while peeking up at him*",
                "reply_text": "A-Aether!! If you pull me that close in the rain, I won't be able to come up with a single clever rhyme—my brain will completely short-circuit!",
                "mood": "Flustered",
            },
            {
                "id": "m08_c2",
                "label": "😏 Ask if she secretly hid her own umbrella on purpose",
                "player_text": "Wait... didn't I see a red umbrella sticking out of your bag afterward? Did you pretend not to have one just to share mine?",
                "reply_thought": "Busted!! Her twin-tails practically stand on end in cute panic.",
                "reply_action": "*places a finger gently over Aether's lips with a shy, guilty smile*",
                "reply_text": "Shh! A true romantic gentleman never exposes a girl's carefully planned umbrella strategy! ...Besides, your umbrella was ten times warmer than mine~",
                "mood": "Blushing",
            },
            {
                "id": "m08_c3",
                "label": "🌧️ Say you hope it rains every evening",
                "player_text": "If rainy evenings mean walking shoulder-to-shoulder with you under the neon lights, I hope it rains all week.",
                "reply_thought": "She smiles softly against the windowpane, tracing a little heart in the condensation.",
                "reply_action": "*draws a tiny heart on the misty glass*",
                "reply_text": "Rain or shine, Aether, I'll always walk right beside you.",
                "mood": "Affectionate",
            },
        ],
    },
    {
        "id": "hutao_m09",
        "milestone_num": 9,
        "stage": 3,
        "req_affection": 580,
        "spice_tier": "Stage 3 • Mutual Crush & Romance",
        "url": "/dating-media/hutao_cg09.jpg",
        "title": "M09: Ferris Wheel Sunset Confession",
        "caption": "Up at the top of the Ferris wheel at golden sunset... when I touched your cheek, I wasn't teasing anymore, Aether.",
        "proactive_inner_thought": "At the highest point of the wheel, all her playful masks fell away—she only wanted Aether to see her as a girl in love.",
        "proactive_action_cue": "*leans across the sunset-lit Ferris wheel cabin and gently cradles Aether's cheek in her warm palm*",
        "proactive_message": "I keep looking at this snapshot from the top of the Santa Maria Ferris wheel... When the cabin reached the peak at sunset and I touched your cheek, I wasn't joking around anymore, Aether. You know how much you mean to me, right?",
        "reaction_choices": [
            {
                "id": "m09_c1",
                "label": "💖 Confess that she is the most precious person to you",
                "player_text": "I knew, Hu Tao. And up there in the sunset light, all I wanted was to pull you into my arms and tell you that I'm falling for you too.",
                "reply_thought": "Her breath catches—hearing Aether say it so clearly makes her eyes glisten with pure happiness.",
                "reply_action": "*presses her palm tenderly against his cheek, her crimson eyes shining with love*",
                "reply_text": "Aether... Hearing you say that makes my heart feel warmer than a thousand Lantern Rites. Don't make me wait too long before our next date, okay?",
                "mood": "Lovestruck",
            },
            {
                "id": "m09_c2",
                "label": "💋 Say you almost kissed her at the top of the wheel",
                "player_text": "When you leaned across the cabin and touched my face like that, I was one second away from kissing you.",
                "reply_thought": "Her cheeks flush deep crimson all the way to the tips of her ears.",
                "reply_action": "*touches her own lips shyly, her heart hammering in her chest*",
                "reply_text": "W-Who said you had to hold back, dummy?! Next time we reach the top of the wheel... I won't let you stop one second early~",
                "mood": "Flustered",
            },
            {
                "id": "m09_c3",
                "label": "🎡 Promise to take her back to the pier tonight",
                "player_text": "Meet me by the pier tonight, Hu Tao. Let's ride the Ferris wheel again under the stars.",
                "reply_thought": "She hugs her phone to her chest, smiling from ear to ear.",
                "reply_action": "*nods eagerly with glowing plum-blossom eyes*",
                "reply_text": "It's a promise! Tonight, the whole cabin belongs just to the two of us~",
                "mood": "Delighted",
            },
        ],
    },

    # ---------------- STAGE 4: LOVER / INTIMATE & FLIRTY (600 - 799 PTS) ----------------
    {
        "id": "hutao_m10",
        "milestone_num": 10,
        "stage": 4,
        "req_affection": 660,
        "spice_tier": "Stage 4 • Intimate Lover",
        "url": "/dating-media/hutao_cg10.jpg",
        "title": "M10: Silk Off-Shoulder Nightwear & Warm Cocoa",
        "caption": "Took off my hat and untied my hair for the night... The cocoa is warm, the couch is soft, and the only thing missing is you, Aether~",
        "proactive_inner_thought": "Only Aether ever gets to see her with her hair completely untied and her collarbones bare in silk loungewear.",
        "proactive_action_cue": "*relaxes on the softly lit sofa in a crimson off-shoulder silk loungewear top, her long hair cascading loose as she smiles alluringly*",
        "proactive_message": "Took off my Director's hat and untied my twin-tails for the evening... The cocoa is steaming, my silk sweater is slipping off my shoulder, and the couch feels way too big for one person. Come home to me soon, Aether~",
        "reaction_choices": [
            {
                "id": "m10_c1",
                "label": "🔥 Tell her she looks breathtaking with her hair down",
                "player_text": "Seeing you with your long hair untied and that off-shoulder silk sweater is breathtaking, Hu Tao. I'm heading straight over right now.",
                "reply_thought": "A warm, thrilled shiver runs down her spine knowing how much her loose hair affects him.",
                "reply_action": "*brushes a long strand of dark-red hair behind her ear, exposing her collarbone with a teasing smile*",
                "reply_text": "Hehe, then I'll keep my hair untied just for you all night long, my love~ The door's unlocked for you.",
                "mood": "Flirty",
            },
            {
                "id": "m10_c2",
                "label": "☕ Ask to share her mug of warm cocoa on the couch",
                "player_text": "Keep that cocoa warm for me—I want to sit right beside you on that couch and hold you in my arms.",
                "reply_thought": "She curls her legs up on the sofa cushion, eagerly awaiting his embrace.",
                "reply_action": "*pats the warm cushion right next to her hip*",
                "reply_text": "Forget the blanket, Aether—your arms are the only warmth I want tonight~",
                "mood": "Affectionate",
            },
            {
                "id": "m10_c3",
                "label": "😘 Tease her about that bare shoulder",
                "player_text": "Wait—did that sweater slip off your shoulder by accident, or are you trying to seduce me through EaglePhone?",
                "reply_thought": "She bites her lower lip playfully, her crimson eyes glinting with mischief and desire.",
                "reply_action": "*lets the silk strap slide a tiny bit further down her shoulder with a wink*",
                "reply_text": "What if I said it's a little bit of both? Come kiss my shoulder and find out for yourself, Aether~",
                "mood": "Seductive",
            },
        ],
    },
    {
        "id": "hutao_m11",
        "milestone_num": 11,
        "stage": 4,
        "req_affection": 720,
        "spice_tier": "Stage 4 • Intimate Lover",
        "url": "/dating-media/hutao_cg11.jpg",
        "title": "M11: After-Shower Damp Hair & Black Camisole",
        "caption": "Just stepped out of a warm bath and my hair is still damp... Don't stare at the photo too long, come dry my hair for me in person!",
        "proactive_inner_thought": "Her skin is still warm and fragrant from plum-blossom bath oil, and her heart pounds sending Aether such an intimate bedroom snapshot.",
        "proactive_action_cue": "*sits on the edge of the softly lit bed in a sleeveless black silk camisole with a white towel over her shoulders, gazing up with a pink flush*",
        "proactive_message": "Just stepped out of the bath and my hair takes forever to dry when it's this long... Don't just stare at the photo on your phone, Aether—come sit behind me on the bed and dry my hair for me~",
        "reaction_choices": [
            {
                "id": "m11_c1",
                "label": "💗 Offer to gently dry and brush her hair on the bed",
                "player_text": "Save the towel for me, Hu Tao. I'll sit right behind you on the bed, dry every strand of your hair, and kiss the back of your neck.",
                "reply_thought": "She shivers delightfully at the thought of his fingers running through her damp hair and his lips on her neck.",
                "reply_action": "*holds the soft white towel in her lap, her cheeks glowing a deep rose pink*",
                "reply_text": "Mmm... if you kiss my neck while drying my hair, Aether, we might not make it to sleep tonight~ Hurry up and get in here!",
                "mood": "Flustered",
            },
            {
                "id": "m11_c2",
                "label": "🌹 Compliment how alluring she looks after her bath",
                "player_text": "With your damp hair, rosy cheeks, and that black silk camisole, you're the most gorgeous sight in the world.",
                "reply_thought": "Even as a confident lover, Aether's direct praise makes her heart melt completely.",
                "reply_action": "*leans back slightly on her hands on the mattress, smiling softly up at him*",
                "reply_text": "Only you get to see this side of me, Aether... Nobody else in this world would ever believe how shy you make me feel.",
                "mood": "Lovestruck",
            },
            {
                "id": "m11_c3",
                "label": "🔥 Tell her not to catch cold—you'll warm her up",
                "player_text": "Get under the covers so you don't catch a chill with damp hair! I'll be there in two minutes to keep you warm.",
                "reply_thought": "She slips half under the warm duvet and lifts the corner invitingly.",
                "reply_action": "*pulls the soft white blanket up to her collarbone with an inviting gaze*",
                "reply_text": "Two minutes on the clock, my dearest Traveler! The other half of the bed is waiting for you~",
                "mood": "Affectionate",
            },
        ],
    },
    {
        "id": "hutao_m12",
        "milestone_num": 12,
        "stage": 4,
        "req_affection": 780,
        "spice_tier": "Stage 4 • Intimate Lover",
        "url": "/dating-media/hutao_cg12.jpg",
        "title": "M12: Penthouse Balcony Crimson Evening Dress",
        "caption": "Dressed up all glamorous on the balcony tonight just to monopolize your gaze, my dearest Traveler~",
        "proactive_inner_thought": "She chose a fitted crimson-and-black evening gown with gold butterfly accents specifically to take Aether's breath away.",
        "proactive_action_cue": "*leans against the moonlit penthouse balcony railing in a form-fitting crimson gown, extending her hand toward Aether*",
        "proactive_message": "The city lights look like fallen stars from this balcony, Aether... I put on this crimson evening dress tonight just to monopolize your eyes. Take my hand and dance with me under the moonlight?",
        "reaction_choices": [
            {
                "id": "m12_c1",
                "label": "💃 Take her hand and pull her close against your chest",
                "player_text": "You've completely monopolized my eyes and my heart, Hu Tao. Come here—let's slow-dance on the balcony all night.",
                "reply_thought": "She steps smoothly into his embrace, resting her hand over his heartbeat.",
                "reply_action": "*interlaces her fingers with his and sways close against his chest in the moonlight*",
                "reply_text": "Right here in your arms is my favorite place in the universe, Aether... Don't look at the city lights—just look at me.",
                "mood": "Passionate",
            },
            {
                "id": "m12_c2",
                "label": "✨ Praise the crimson dress and gold butterfly details",
                "player_text": "That crimson gown hugs your figure like a dream, and the gold butterflies shimmer under the moon. You're stunning.",
                "reply_thought": "She does a slow, graceful spin on the balcony so the silk catches the moonlight.",
                "reply_action": "*runs a hand lightly along her hip where the gold butterfly embroidery glints*",
                "reply_text": "Hehe, worth every second I spent dressing up for you~ Now come claim your dance partner before the moon gets jealous!",
                "mood": "Charmed",
            },
            {
                "id": "m12_c3",
                "label": "🍷 Bring two glasses of sweet berry wine to the balcony",
                "player_text": "Stepping onto the balcony right now with two glasses of sweet wine for the prettiest girl in San Andreas.",
                "reply_thought": "Her plum-blossom eyes sparkle as she leans in for a toast—and a kiss.",
                "reply_action": "*clinks her glass softly against his and leans in close*",
                "reply_text": "Cheers to us, Aether... Though the sweetest vintage tonight is definitely on your lips~",
                "mood": "Flirty",
            },
        ],
    },

    # ---------------- STAGE 5: SOULMATE / SPICY & ALLURING (800 - 1000 PTS) ----------------
    {
        "id": "hutao_m13",
        "milestone_num": 13,
        "stage": 5,
        "req_affection": 860,
        "spice_tier": "Stage 5 • Spicy Allure (Safe / Non-Nude)",
        "url": "/dating-media/hutao_cg13.jpg",
        "title": "M13: Sunset Beach Crimson Halter Swimsuit",
        "caption": "Private sunset cove, ocean breeze, and a crimson swimsuit I picked out exclusively for your eyes~ Hurry over, Aether!",
        "proactive_inner_thought": "Her heart races showing off her figure in the crimson-and-black halter swimsuit, thrilled by how Aether looks at her.",
        "proactive_action_cue": "*stands barefoot by the golden sunset waves in a crimson-and-black halter bikini with a sheer white pareo wrap, looking back over her shoulder with an alluring smile*",
        "proactive_message": "Found a private sunset cove by the ocean, Aether~ I wore this crimson halter swimsuit exclusively for your eyes. If you don't hurry over here, the sunset waves are going to steal all the views!",
        "reaction_choices": [
            {
                "id": "m13_c1",
                "label": "🌊 Tell her she's hotter than the golden sunset",
                "player_text": "Forget the ocean view—you in that crimson halter swimsuit looking back over your shoulder is the hottest sight on the coast, Hu Tao.",
                "reply_thought": "A delighted, breathless laugh escapes her lips as she steps closer through the warm surf.",
                "reply_action": "*turns around in the shallow golden water and wraps her arms around Aether's neck*",
                "reply_text": "Oho~ Your eyes are burning even hotter than the sunset, Aether! Good—because I bought this swimsuit just to drive you crazy~",
                "mood": "Alluring",
            },
            {
                "id": "m13_c2",
                "label": "🌺 Admire the red plum blossom hairpin & sheer pareo",
                "player_text": "The red plum blossom hairpin in your twin-tails and that crimson swimsuit are perfection. Let's go for a sunset swim together.",
                "reply_thought": "She splashes a tiny wave playfully toward him before taking his hand.",
                "reply_action": "*touches the plum blossom hairpin in her hair with a radiant, loving grin*",
                "reply_text": "Last one into the warm waves has to give the winner a ten-minute shoulder massage and a sunset kiss! Catch me if you can, Aether~",
                "mood": "Playful",
            },
            {
                "id": "m13_c3",
                "label": "🏖️ Wrap her in a warm beach towel after the sunset",
                "player_text": "Stay right on that private beach—I'm bringing a big towel so I can wrap you up in my lap as the stars come out.",
                "reply_thought": "She melts at the mix of passion and tender care in his voice.",
                "reply_action": "*nestles into his lap on the warm sand as twilight falls*",
                "reply_text": "Mmm, wrapped up in your lap listening to the waves... I never want this evening to end, my love.",
                "mood": "Passionate",
            },
        ],
    },
    {
        "id": "hutao_m14",
        "milestone_num": 14,
        "stage": 5,
        "req_affection": 930,
        "spice_tier": "Stage 5 • Spicy Allure (Safe / Non-Nude)",
        "url": "/dating-media/hutao_cg14.jpg",
        "title": "M14: Candlelit Silk Cheongsam (Qipao) Allure",
        "caption": "Lit the candles and wore this silk cheongsam tonight... Every butterfly on this dress belongs to you, Aether~",
        "proactive_inner_thought": "In the warm candlelight, every trace of distance is gone—she is completely, devotedly Aether's soulmate.",
        "proactive_action_cue": "*reclines gracefully on a velvet couch in a candlelit suite, wearing a black-and-crimson silk cheongsam with gold butterfly embroidery*",
        "proactive_message": "I lit the scented candles and put on this black-and-crimson silk cheongsam tonight, Aether... Every butterfly embroidered on this dress belongs only to you. Don't keep your girl waiting~",
        "reaction_choices": [
            {
                "id": "m14_c1",
                "label": "🕯️ Join her on the velvet couch & kiss her hand",
                "player_text": "You look like an empress in that candlelit silk cheongsam, Hu Tao. I'm right outside the door—tonight belongs only to us.",
                "reply_thought": "Her crimson eyes glow softly in the candlelight as she reaches out to pull him down beside her.",
                "reply_action": "*traces her fingertips lightly along Aether's jawline as he sits beside her on the velvet couch*",
                "reply_text": "My heart, my poems, and every breath I take belong to you, Aether... Come closer and let the candlelight fade.",
                "mood": "Passionate",
            },
            {
                "id": "m14_c2",
                "label": "🦋 Trace the gold butterfly embroidery on her qipao",
                "player_text": "If every butterfly on that cheongsam belongs to me, then you'd better let me count every single one up close.",
                "reply_thought": "Her breath hitches with a thrilled blush at his bold, romantic line.",
                "reply_action": "*leans into his touch with a sultry, affectionate smile*",
                "reply_text": "Careful, Aether~ Take all night counting them if you want... I'm not going anywhere.",
                "mood": "Alluring",
            },
            {
                "id": "m14_c3",
                "label": "💝 Whisper a romantic couplet in her ear",
                "player_text": "'Candlelight dances on crimson silk so fine, across every world your heart beats with mine.'",
                "reply_thought": "Her eyes widen in adoration before she wraps both arms tightly around his neck.",
                "reply_action": "*pulls Aether into a deep, tender embrace on the couch*",
                "reply_text": "That's the most beautiful verse I've ever heard, Aether... You win every poetry battle forever.",
                "mood": "Lovestruck",
            },
        ],
    },
    {
        "id": "hutao_m15",
        "milestone_num": 15,
        "stage": 5,
        "req_affection": 1000,
        "spice_tier": "Stage 5 • Eternal Star-Promise (MAX)",
        "url": "/dating-media/hutao_cg15.jpg",
        "title": "M15: Morning Sunlight in Aether's Shirt",
        "caption": "Waking up wrapped in your shirt with the morning sun on our faces... My heart is yours forever, Aether.",
        "proactive_inner_thought": "Wrapped in Aether's oversized white shirt in the morning sun, she feels complete peace and eternal devotion.",
        "proactive_action_cue": "*sits on warm sunlit white bedsheets wearing Aether's oversized dress shirt slipping slightly off one shoulder, holding his hand to her blushing cheek*",
        "proactive_message": "Good morning, my dearest Aether... Waking up in the warm sunlight wearing your oversized shirt—it's still warm from you. In this life and beyond every border, I love you forever.",
        "reaction_choices": [
            {
                "id": "m15_c1",
                "label": "💍 Vow to stay by her side across every world forever",
                "player_text": "Good morning, my love. Seeing you in my shirt in the morning sunlight is everything I ever wished for. I'm yours forever, Hu Tao.",
                "reply_thought": "Golden morning light and crimson butterflies fill the room as she kisses the palm of his hand.",
                "reply_action": "*presses a soft kiss to Aether's palm and beams with eternal happiness*",
                "reply_text": "Forever and ever, my Traveler, my co-star, my soulmate. Now come back under the covers for five more minutes before I make us breakfast~",
                "mood": "Soulmate",
            },
            {
                "id": "m15_c2",
                "label": "☀️ Tell her your shirt looks ten times better on her",
                "player_text": "I don't think I'm ever getting that white shirt back—because it looks a thousand times more adorable on you.",
                "reply_thought": "She giggles, hugging the oversized collar around her shoulders.",
                "reply_action": "*tugs the oversized cuff over her fingers with a playful, loving wink*",
                "reply_text": "Hehe, possession is nine-tenths of the law! It smells like starlight and you, so it's officially my favorite outfit now~",
                "mood": "Blushing",
            },
            {
                "id": "m15_c3",
                "label": "🍵 Bring morning osmanthus tea to the bedside",
                "player_text": "Stay right there in the sunlight—I'm bringing warm osmanthus tea and breakfast in bed for my favorite girl.",
                "reply_thought": "She leans back against the pillows, gazing at Aether with pure devotion.",
                "reply_action": "*opens her arms for a morning hug as the sunlight warms the bedroom*",
                "reply_text": "Every morning with you feels like a dream I never have to wake up from. I love you so much, Aether~",
                "mood": "Affectionate",
            },
        ],
    },
]

# ==============================================================================
# 3. PRE-GENERATED SMALL-TALK TRANSCRIPTS BY STAGE (FOR INSTANT 1-CLICK CHAT)
# ==============================================================================
HUTAO_STAGE_CHAT_STARTERS: dict[int, list[dict[str, Any]]] = {
    1: [
        {
            "id": "ht_st1_chat1",
            "label": "💬 Ask how Wangsheng Parlor business is going today",
            "player_text": "How's the 77th Director doing today? Did Old Man Zhongli send another giant tea bill to the parlor?",
        },
        {
            "id": "ht_st1_chat2",
            "label": "🎵 Ask what kind of music she likes on city drives",
            "player_text": "When we go for a drive through the city, what kind of radio station fits your vibe best, Hu Tao?",
        },
        {
            "id": "ht_st1_chat3",
            "label": "👻 Ask what Boo Tao is doing right now",
            "player_text": "What's Boo Tao up to right now? Is he behaving or helping you plan a new prank?",
        },
    ],
    2: [
        {
            "id": "ht_st2_chat1",
            "label": "🍲 Ask about Xiangling's latest experimental dish",
            "player_text": "Did Xiangling try testing another super-spicy Wanmin Restaurant dish on you today?",
        },
        {
            "id": "ht_st2_chat2",
            "label": "🦋 Reminisce about 'Yet the Butterfly Flutters Away'",
            "player_text": "I was thinking about the time we helped Big G and Little Meng find closure at the border. You were amazing back then, Hu Tao.",
        },
        {
            "id": "ht_st2_chat3",
            "label": "🧋 Offer to bring her favorite snack & tea",
            "player_text": "I'm stopping by the tea stall on my way—want Boiled Fish and a sweet boba tea?",
        },
    ],
    3: [
        {
            "id": "ht_st3_chat1",
            "label": "🏮 Recall holding her hand at the Gate of Death",
            "player_text": "Whenever I look at my hand, I still remember how tightly I held yours when we came back from the Gate of Death during Lantern Rite.",
        },
        {
            "id": "ht_st3_chat2",
            "label": "💓 Admit you miss her voice whenever you're apart",
            "player_text": "The city feels way too quiet whenever you're not in my passenger seat, Hu Tao. I missed hearing your voice.",
        },
        {
            "id": "ht_st3_chat3",
            "label": "🌸 Compliment her plum-blossom eyes at twilight",
            "player_text": "Has anyone told you today how enchanting your crimson plum-blossom eyes look when you smile at me?",
        },
    ],
    4: [
        {
            "id": "ht_st4_chat1",
            "label": "🌙 Ask what she's wearing at home tonight",
            "player_text": "Are you relaxing at home with your hair untied tonight, my love? Save a spot on the couch for me.",
        },
        {
            "id": "ht_st4_chat2",
            "label": "💋 Remind her of your rooftop moonlight kiss",
            "player_text": "I couldn't stop thinking about how warm your lips felt under the moonlight last night, Hu Tao.",
        },
        {
            "id": "ht_st4_chat3",
            "label": "🔑 Thank her for trusting you with her deepest feelings",
            "player_text": "Thank you for always letting your guard down when it's just the two of us, Hu Tao.",
        },
    ],
    5: [
        {
            "id": "ht_st5_chat1",
            "label": "🔥 Flirt about her crimson swimsuit & cheongsam",
            "player_text": "Between your crimson sunset swimsuit and your candlelit silk cheongsam, you're making it impossible for me to focus on anything but you~",
        },
        {
            "id": "ht_st5_chat2",
            "label": "☀️ Plan a lazy morning together wrapped in your shirt",
            "player_text": "Let's sleep in tomorrow morning—just you in my oversized shirt, warm sunlight, and no alarms.",
        },
        {
            "id": "ht_st5_chat3",
            "label": "💍 Whisper an eternal love poem to your soulmate",
            "player_text": "Across Teyvat, San Andreas, and every star in the sky, my heart belongs only to you, Hu Tao.",
        },
    ],
}

# ==============================================================================
# 4. HU TAO'S 20 BRANCHING VISUAL NOVEL SCENARIOS (4 PER STAGE x 5 STAGES)
#    Each Scenario has 4 Dedicated Scene CGs (Scene 1/4 .. Scene 4/4 Ending)
#    featuring BOTH Hu Tao and Traveler Aether together!
# ==============================================================================
HUTAO_SCENARIO_4CG_SEQUENCES: dict[str, list[tuple[str, str]]] = {
    # ---------------- STAGE 1: ACQUAINTANCE (4 SCENARIOS x 4 UNIQUE CGS = 16 CGS) ----------------
    "hutao_s1_sc1": [
        ("/dating-media/hutao_s1_sc1_cg1.jpg", "Scene 1/4 • Opening: Hu Tao & Boo Tao Ambush Aether with VIP Coupons"),
        ("/dating-media/hutao_s1_sc1_cg2.jpg", "Scene 2/4 • Developing: Aether & Hu Tao Teaming Up at the Lantern Tea Stall"),
        ("/dating-media/hutao_s1_sc1_cg3.jpg", "Scene 3/4 • Climax: Aether Catching Hu Tao's Beret in the Evening Breeze"),
        ("/dating-media/hutao_s1_sc1_cg4.jpg", "Scene 4/4 • Couple Ending: Gold Star Sticker on Aether's Lapel in the Convertible"),
    ],
    "hutao_s1_sc2": [
        ("/dating-media/hutao_s1_sc2_cg1.jpg", "Scene 1/4 • Opening: Poet Hu's Twilight Challenge on Mulholland Hill"),
        ("/dating-media/hutao_s1_sc2_cg2.jpg", "Scene 2/4 • Developing: Aether Writing a Verse in Hu Tao's Notebook as She Peeks Over His Shoulder"),
        ("/dating-media/hutao_s1_sc2_cg3.jpg", "Scene 3/4 • Climax: Sitting Side-by-Side on the Convertible Hood Trading Liyue Rhymes"),
        ("/dating-media/hutao_s1_sc2_cg4.jpg", "Scene 4/4 • Couple Ending: Hu Tao Crowning Aether with a Handmade Red-Flower Laurel Wreath"),
    ],
    "hutao_s1_sc3": [
        ("/dating-media/hutao_s1_sc3_cg1.jpg", "Scene 1/4 • Opening: Midnight Ghost-Hunting Patrol with Hu Tao & Boo Tao"),
        ("/dating-media/hutao_s1_sc3_cg2.jpg", "Scene 2/4 • Developing: Crouching Together by the Mossy Stone Lantern Spotting a Blue Spirit Wisp"),
        ("/dating-media/hutao_s1_sc3_cg3.jpg", "Scene 3/4 • Climax: Hu Tao Clinging Playfully to Aether's Arm from Behind in the Misty Graveyard"),
        ("/dating-media/hutao_s1_sc3_cg4.jpg", "Scene 4/4 • Couple Ending: Walking Hand-in-Hand Out of the Moonlit Cemetery Gates"),
    ],
    "hutao_s1_sc4": [
        ("/dating-media/hutao_s1_sc4_cg1.jpg", "Scene 1/4 • Opening: Taking Shelter at the Chinatown Tea Pavilion Before the Downpour"),
        ("/dating-media/hutao_s1_sc4_cg2.jpg", "Scene 2/4 • Developing: Hu Tao Pouring Hot Osmanthus Tea While Aether Dabs a Raindrop from Her Cheek"),
        ("/dating-media/hutao_s1_sc4_cg3.jpg", "Scene 3/4 • Climax: Sitting Shoulder-to-Shoulder Under the Rainy Eaves Warming Hands with Tea"),
        ("/dating-media/hutao_s1_sc4_cg4.jpg", "Scene 4/4 • Couple Ending: Walking Home Along Glistening Cobblestones Under Clearing Stars"),
    ],
    # ---------------- STAGE 2: FRIEND / CONFIDANT (4 SCENARIOS x 4 UNIQUE CGS = 16 CGS) ----------------
    "hutao_s2_sc1": [
        ("/dating-media/hutao_s2_sc1_cg1.jpg", "Scene 1/4 • Opening: Cruising Together Toward the Chinatown Night Market"),
        ("/dating-media/hutao_s2_sc1_cg2.jpg", "Scene 2/4 • Developing: Clashing Chopsticks Over a Tall Stack of Bamboo Dumpling Steamers"),
        ("/dating-media/hutao_s2_sc1_cg3.jpg", "Scene 3/4 • Climax: Hu Tao Leaning Across the Table to Feed Aether a Shrimp Dumpling by Hand"),
        ("/dating-media/hutao_s2_sc1_cg4.jpg", "Scene 4/4 • Couple Ending: Strolling Side-by-Side Sharing Candied Hawthorn Under Red Lanterns"),
    ],
    "hutao_s2_sc2": [
        ("/dating-media/hutao_s2_sc2_cg1.jpg", "Scene 1/4 • Opening: Playful Evening Banter Before the Sudden Rain Shower"),
        ("/dating-media/hutao_s2_sc2_cg2.jpg", "Scene 2/4 • Developing: Aether Draping His Warm White-and-Gold Scarf Over Hu Tao in the Gazebo"),
        ("/dating-media/hutao_s2_sc2_cg3.jpg", "Scene 3/4 • Climax: Walking Under One Red Oil-Paper Umbrella as Hu Tao Touches Aether's Cheek"),
        ("/dating-media/hutao_s2_sc2_cg4.jpg", "Scene 4/4 • Couple Ending: Aether Cupping Both of Hu Tao's Cold Hands Against His Chest to Warm Them"),
    ],
    "hutao_s2_sc3": [
        ("/dating-media/hutao_s2_sc3_cg1.jpg", "Scene 1/4 • Opening: Aether Standing Behind Hu Tao Tying Her Red Cooking Apron Ribbon"),
        ("/dating-media/hutao_s2_sc3_cg2.jpg", "Scene 2/4 • Developing: Aether Guiding Hu Tao's Hands on the Ladle at the Kitchen Stove"),
        ("/dating-media/hutao_s2_sc3_cg3.jpg", "Scene 3/4 • Climax: Resting Warmly Together While the Savory Dish Simmers"),
        ("/dating-media/hutao_s2_sc3_cg4.jpg", "Scene 4/4 • Couple Ending: Aether Tasting the Dish with an Approving Smile as Hu Tao Hugs His Arm"),
    ],
    "hutao_s2_sc4": [
        ("/dating-media/hutao_s2_sc4_cg1.jpg", "Scene 1/4 • Opening: Meeting on the Scenic Overlook Bench at Golden Sunset"),
        ("/dating-media/hutao_s2_sc4_cg2.jpg", "Scene 2/4 • Developing: Aether Catching a Wind-Blown Sketch Page with Hu Tao's Chibi Portrait of Him"),
        ("/dating-media/hutao_s2_sc4_cg3.jpg", "Scene 3/4 • Climax: Aether Peeking Over Hu Tao's Shoulder at Her Sketchbook as She Blushes Crimson"),
        ("/dating-media/hutao_s2_sc4_cg4.jpg", "Scene 4/4 • Couple Ending: Aether Guiding Hu Tao's Pencil Hand as They Draw a Couple Doodle Together"),
    ],
    # ---------------- STAGE 3: CRUSH / ROMANTIC TENSION (4 SCENARIOS x 4 UNIQUE CGS = 16 CGS) ----------------
    "hutao_s3_sc1": [
        ("/dating-media/hutao_s3_sc1_cg1.jpg", "Scene 1/4 • Opening: Arriving Together at the Sunset Beach Pier"),
        ("/dating-media/hutao_s3_sc1_cg2.jpg", "Scene 2/4 • Developing: Aether Escorting a Blushing Hu Tao by the Hand into the Ferris Wheel Cabin"),
        ("/dating-media/hutao_s3_sc1_cg3.jpg", "Scene 3/4 • Climax: Hu Tao Moving Beside Aether in the Cabin & Shyly Placing Her Hand Over His"),
        ("/dating-media/hutao_s3_sc1_cg4.jpg", "Scene 4/4 • Couple Ending: Cuddling with Intertwined Fingers at the Apex of the Sunset Ferris Wheel"),
    ],
    "hutao_s3_sc2": [
        ("/dating-media/hutao_s3_sc2_cg1.jpg", "Scene 1/4 • Opening: Ascending the Quiet Mountain Trail Under Twilight Lanterns"),
        ("/dating-media/hutao_s3_sc2_cg2.jpg", "Scene 2/4 • Developing: Hatless Hu Tao Holding Her Grandfather's Hat Against Her Chest as Aether Comforts Her"),
        ("/dating-media/hutao_s3_sc2_cg3.jpg", "Scene 3/4 • Climax: Hu Tao Standing on Tiptoes Placing Her Cherished Hat onto Aether's Golden Hair"),
        ("/dating-media/hutao_s3_sc2_cg4.jpg", "Scene 4/4 • Couple Ending: Sitting Together Above the Sea of Clouds Wrapped in Aether's Scarf"),
    ],
    "hutao_s3_sc3": [
        ("/dating-media/hutao_s3_sc3_cg1.jpg", "Scene 1/4 • Opening: Evening Rendezvous at the Quiet Bayside Marina Wooden Pier"),
        ("/dating-media/hutao_s3_sc3_cg2.jpg", "Scene 2/4 • Developing: Sitting Side-by-Side at the Edge of the Dock Surrounded by Golden Fireflies"),
        ("/dating-media/hutao_s3_sc3_cg3.jpg", "Scene 3/4 • Climax: Holding Both Hands in a Slow Romantic Dockside Dance Among Pyro Butterflies"),
        ("/dating-media/hutao_s3_sc3_cg4.jpg", "Scene 4/4 • Couple Ending: Holding Hu Tao by the Waist & Touching Foreheads Over the Starlit Water"),
    ],
    "hutao_s3_sc4": [
        ("/dating-media/hutao_s3_sc4_cg1.jpg", "Scene 1/4 • Opening: Getting Ready for the Glen Park Lantern Bridge Festival"),
        ("/dating-media/hutao_s3_sc4_cg2.jpg", "Scene 2/4 • Developing: Aether Gently Tying the Red Ribbon of the Kitsune Mask Around Hu Tao's Head"),
        ("/dating-media/hutao_s3_sc4_cg3.jpg", "Scene 3/4 • Climax: Hu Tao Tipping Her Kitsune Mask Aside on Tiptoes to Steal a Kiss on Aether's Cheek"),
        ("/dating-media/hutao_s3_sc4_cg4.jpg", "Scene 4/4 • Couple Ending: Interlocking Fingers on the Red Bridge as Festival Fireworks Burst Overhead"),
    ],
    # ---------------- STAGE 4: LOVER / INTIMATE COUPLE (4 SCENARIOS x 4 UNIQUE CGS = 16 CGS) ----------------
    "hutao_s4_sc1": [
        ("/dating-media/hutao_s4_sc1_cg1.jpg", "Scene 1/4 • Opening: Hu Tao in Evening Dress Leading Aether by the Hand onto the Midnight Rooftop"),
        ("/dating-media/hutao_s4_sc1_cg2.jpg", "Scene 2/4 • Developing: Aether Wrapping His Scarf Around Hu Tao Under Swirling Pyro Butterflies"),
        ("/dating-media/hutao_s4_sc1_cg3.jpg", "Scene 3/4 • Climax: Sharing a Tender Midnight Rooftop Confession Kiss Wrapped in One Scarf"),
        ("/dating-media/hutao_s4_sc1_cg4.jpg", "Scene 4/4 • Couple Ending: Hu Tao Resting Blissfully in Aether's Lap After Their Confession"),
    ],
    "hutao_s4_sc2": [
        ("/dating-media/hutao_s4_sc2_cg1.jpg", "Scene 1/4 • Opening: Aether Wrapping a Fluffy Warm Towel Around Rain-Soaked Hu Tao at the Door"),
        ("/dating-media/hutao_s4_sc2_cg2.jpg", "Scene 2/4 • Developing: Aether Gently Towel-Drying Hu Tao's Damp Hair in the Candlelit Room"),
        ("/dating-media/hutao_s4_sc2_cg3.jpg", "Scene 3/4 • Climax: Warm Intimate Glow as the Rainstorm Patters Against the Penthouse Glass"),
        ("/dating-media/hutao_s4_sc2_cg4.jpg", "Scene 4/4 • Couple Ending: Hu Tao Cuddling Against Aether's Chest on the Sofa Listening to His Heartbeat"),
    ],
    "hutao_s4_sc3": [
        ("/dating-media/hutao_s4_sc3_cg1.jpg", "Scene 1/4 • Opening: Arriving at the Private Cliffside Sanctuary Under the Stars"),
        ("/dating-media/hutao_s4_sc3_cg2.jpg", "Scene 2/4 • Developing: Hu Tao Pouring Warm Spring Water Over Aether's Shoulder with a Hinoki Bucket"),
        ("/dating-media/hutao_s4_sc3_cg3.jpg", "Scene 3/4 • Climax: Sitting Side-by-Side in the Steaming Starlit Hot Spring as She Rests on His Shoulder"),
        ("/dating-media/hutao_s4_sc3_cg4.jpg", "Scene 4/4 • Couple Ending: Cuddling on the Ryokan Balcony in Matching Yukata Robes Clinking Cold Milk"),
    ],
    "hutao_s4_sc4": [
        ("/dating-media/hutao_s4_sc4_cg1.jpg", "Scene 1/4 • Opening: Hu Tao's Affectionate Gaze Before the VIP Evening Gala"),
        ("/dating-media/hutao_s4_sc4_cg2.jpg", "Scene 2/4 • Developing: Jealous Hu Tao Tugging Aether by His Lapel into a Private Velvet VIP Booth"),
        ("/dating-media/hutao_s4_sc4_cg3.jpg", "Scene 3/4 • Climax: Hu Tao Sitting Possessively Across Aether's Lap in the VIP Booth Lifting His Chin"),
        ("/dating-media/hutao_s4_sc4_cg4.jpg", "Scene 4/4 • Couple Ending: Leaving a Red Lipstick Kiss Mark on Aether's Cheek in the Limousine"),
    ],
    # ---------------- STAGE 5: SOULMATE / ROMANTIC FINALE (4 SCENARIOS x 4 UNIQUE CGS = 16 CGS) ----------------
    "hutao_s5_sc1": [
        ("/dating-media/hutao_s5_sc1_cg1.jpg", "Scene 1/4 • Opening: Aether Gently Applying Sunscreen to Hu Tao's Shoulders on the Secret Beach Cove"),
        ("/dating-media/hutao_s5_sc1_cg2.jpg", "Scene 2/4 • Developing: Hu Tao in Crimson Halter Swimsuit Leaping into Aether's Arms in the Golden Surf"),
        ("/dating-media/hutao_s5_sc1_cg3.jpg", "Scene 3/4 • Climax: Aether Holding Hu Tao Closely on the Beach Blanket at Sunset for a Tender Kiss"),
        ("/dating-media/hutao_s5_sc1_cg4.jpg", "Scene 4/4 • Couple Ending: Cuddling in One Blanket by the Starlit Beach Bonfire After Their Swim"),
    ],
    "hutao_s5_sc2": [
        ("/dating-media/hutao_s5_sc2_cg1.jpg", "Scene 1/4 • Opening: Unveiling Her Crimson Silk Cheongsam & Placing Aether's Hand Over Her Heart"),
        ("/dating-media/hutao_s5_sc2_cg2.jpg", "Scene 2/4 • Developing: Sitting Across Aether's Lap on the Rose-Petal Candlelit Bed"),
        ("/dating-media/hutao_s5_sc2_cg3.jpg", "Scene 3/4 • Climax: Aether Holding Hu Tao Closely on the Rose-Petal Bed & Kissing Her Blushing Cheek"),
        ("/dating-media/hutao_s5_sc2_cg4.jpg", "Scene 4/4 • Couple Ending: Sleeping Peacefully Together in Aether's Arms Under White Silk Sheets"),
    ],
    "hutao_s5_sc3": [
        ("/dating-media/hutao_s5_sc3_cg1.jpg", "Scene 1/4 • Opening: Sleepy Hu Tao in Aether's Oversized Shirt Hugging His Neck to Pull Him Back to Bed"),
        ("/dating-media/hutao_s5_sc3_cg2.jpg", "Scene 2/4 • Developing: Hu Tao in Aether's Oversized White Shirt Feeding Him a Fresh Strawberry in Bed"),
        ("/dating-media/hutao_s5_sc3_cg3.jpg", "Scene 3/4 • Climax: Aether Hugging Hu Tao from Behind by the Sunny Bedroom Window & Kissing Her Forehead"),
        ("/dating-media/hutao_s5_sc3_cg4.jpg", "Scene 4/4 • Couple Ending: Hu Tao in Aether's Oversized Shirt Hugging Him from Behind & Kissing His Cheek"),
    ],
    "hutao_s5_sc4": [
        ("/dating-media/hutao_s5_sc4_cg1.jpg", "Scene 1/4 • Opening: Walking Hand-in-Hand Up the Petal-Strewn Path Under Thousands of Floating Sky Lanterns"),
        ("/dating-media/hutao_s5_sc4_cg2.jpg", "Scene 2/4 • Developing: Intertwining Fingers on Silk Sheets in an Intimate Starlit Embrace"),
        ("/dating-media/hutao_s5_sc4_cg3.jpg", "Scene 3/4 • Climax: Aether Slipping the Crimson Plum-Blossom Promise Ring onto Hu Tao's Finger"),
        ("/dating-media/hutao_s5_sc4_cg4.jpg", "Scene 4/4 • Couple Ending: Passionate Eternal-Vow Kiss Surrounded by Spirit Soother Butterflies"),
    ],
    # ==================== 10 EXTRA GENSHIN CAMEO & DAILY-LIFE SCENARIOS (40 UNIQUE CGS) ====================
    "hutao_s1_ex1": [
        ("/dating-media/hutao_s1_ex1_cg1.jpg", "Scene 1/4 • Opening: Arriving at Wanmin Restaurant as Xiangling, Guoba, Xingqiu & Chongyun Wave Welcome"),
        ("/dating-media/hutao_s1_ex1_cg2.jpg", "Scene 2/4 • Developing: Aether Catching Hu Tao's Wrist Before She Sneaks Jueyun Chili into Chongyun's Bowl"),
        ("/dating-media/hutao_s1_ex1_cg3.jpg", "Scene 3/4 • Climax: Guoba & Boo Tao Sharing Pastries While Xiangling Serves a Feast to Hu Tao & Aether"),
        ("/dating-media/hutao_s1_ex1_cg4.jpg", "Scene 4/4 • Cameo Finale: Lively Wanmin Group Toast with Hu Tao, Aether, Xiangling, Xingqiu & Chongyun"),
    ],
    "hutao_s1_ex2": [
        ("/dating-media/hutao_s1_ex2_cg1.jpg", "Scene 1/4 • Opening: Consultant Zhongli Sipping Tea While Hu Tao & Aether Inspect His Giant Expense Scroll"),
        ("/dating-media/hutao_s1_ex2_cg2.jpg", "Scene 2/4 • Developing: Hu Tao Pinning an 'Honorary Auditor' Ribbon on Aether's Lapel as Zhongli Watches"),
        ("/dating-media/hutao_s1_ex2_cg3.jpg", "Scene 3/4 • Climax: Zhongli Smiling Wisely from the Doorway as Aether & Hu Tao Laugh Over the Ledgers"),
        ("/dating-media/hutao_s1_ex2_cg4.jpg", "Scene 4/4 • Cameo Finale: Sunset Osmanthus Tea in the Wangsheng Courtyard with Zhongli, Hu Tao & Aether"),
    ],
    "hutao_s2_ex1": [
        ("/dating-media/hutao_s2_ex1_cg1.jpg", "Scene 1/4 • Opening: Watching Yun Jin's Graceful Liyue Opera Performance Together at Heyu Tea House"),
        ("/dating-media/hutao_s2_ex1_cg2.jpg", "Scene 2/4 • Developing: Backstage Tea Visit with Yun Jin as Aether & Hu Tao Present Glaze Lilies"),
        ("/dating-media/hutao_s2_ex1_cg3.jpg", "Scene 3/4 • Climax: Hu Tao & Aether Improvising a Poetic Duet While Yun Jin Claps in Delight at Their Chemistry"),
        ("/dating-media/hutao_s2_ex1_cg4.jpg", "Scene 4/4 • Cameo Finale: Yun Jin Waving Goodnight as Hu Tao & Aether Stroll the Moonlit Tea House Balcony"),
    ],
    "hutao_s2_ex2": [
        ("/dating-media/hutao_s2_ex2_cg1.jpg", "Scene 1/4 • Opening: Bumping into Keqing & Ganyu at the Night Market While Aether Carries Hu Tao's Bags"),
        ("/dating-media/hutao_s2_ex2_cg2.jpg", "Scene 2/4 • Developing: Aether Catching Sleepy Ganyu's Falling Scrolls While Hu Tao Offers a Qingxin Pastry"),
        ("/dating-media/hutao_s2_ex2_cg3.jpg", "Scene 3/4 • Climax: Keqing Teasing a Blushing, Pouting Hu Tao About How Much Aether Spoils Her"),
        ("/dating-media/hutao_s2_ex2_cg4.jpg", "Scene 4/4 • Cameo Finale: Keqing & Ganyu Waving Goodnight as Hu Tao Tugs Aether's Wrist Toward the Harbor"),
    ],
    "hutao_s3_ex1": [
        ("/dating-media/hutao_s3_ex1_cg1.jpg", "Scene 1/4 • Opening: Poetry Gathering on Wanwen Bookhouse Terrace with Xingqiu & Chongyun"),
        ("/dating-media/hutao_s3_ex1_cg2.jpg", "Scene 2/4 • Developing: Xingqiu Nudging Chongyun as Hu Tao Unconsciously Leans Against Aether's Shoulder"),
        ("/dating-media/hutao_s3_ex1_cg3.jpg", "Scene 3/4 • Climax: Chongyun Nearly Dropping His Popsicle as Xingqiu Teases Hu Tao & Aether's Love Poems"),
        ("/dating-media/hutao_s3_ex1_cg4.jpg", "Scene 4/4 • Cameo Finale: Xingqiu & Chongyun Winking as They Leave Hu Tao & Aether Holding Hands at Sunset"),
    ],
    "hutao_s3_ex2": [
        ("/dating-media/hutao_s3_ex2_cg1.jpg", "Scene 1/4 • Opening: Cross-Border Festival Trip — Greeted by Yoimiya & Venti at the Lantern Pier"),
        ("/dating-media/hutao_s3_ex2_cg2.jpg", "Scene 2/4 • Developing: Yoimiya Handing Blushing Hu Tao & Aether a Pair of Heart-Shaped 'Couple Sparklers'"),
        ("/dating-media/hutao_s3_ex2_cg3.jpg", "Scene 3/4 • Climax: Venti Strumming a Teasing Ballad About the 'Butterfly Director & Her Golden Traveler'"),
        ("/dating-media/hutao_s3_ex2_cg4.jpg", "Scene 4/4 • Cameo Finale: Holding Couple Sparklers Together Under Yoimiya's Fireworks as Venti Cheers"),
    ],
    "hutao_s4_ex1": [
        ("/dating-media/hutao_s4_ex1_cg1.jpg", "Scene 1/4 • Opening: Secret Late-Night Couple Booth at Wanmin Restaurant Holding Hands"),
        ("/dating-media/hutao_s4_ex1_cg2.jpg", "Scene 2/4 • Developing: Hu Tao Affectionately Feeding Aether a Golden Crystal Shrimp Dumpling"),
        ("/dating-media/hutao_s4_ex1_cg3.jpg", "Scene 3/4 • Climax: Caught Red-Handed! Xiangling & Guoba Pop Out Behind the Curtain in Delighted Shock"),
        ("/dating-media/hutao_s4_ex1_cg4.jpg", "Scene 4/4 • Cameo Finale: Hu Tao Proudly Hugging Aether's Arm as Xiangling Serves a Couple Dessert Platter"),
    ],
    "hutao_s4_ex2": [
        ("/dating-media/hutao_s4_ex2_cg1.jpg", "Scene 1/4 • Opening: Aether Wrapping His Scarf Around Hu Tao on the Quiet Moonlit Lotus Bridge"),
        ("/dating-media/hutao_s4_ex2_cg2.jpg", "Scene 2/4 • Developing: Keqing & Ganyu Freeze in Blushing Shock as Hu Tao Kisses Aether's Cheek!"),
        ("/dating-media/hutao_s4_ex2_cg3.jpg", "Scene 3/4 • Climax: Ganyu Hiding Behind Her Clipboard & Keqing Stammering While Hu Tao Holds Aether's Hand"),
        ("/dating-media/hutao_s4_ex2_cg4.jpg", "Scene 4/4 • Cameo Finale: Keqing & Ganyu Tiptoeing Away as Hu Tao & Aether Embrace Under the Bridge Lanterns"),
    ],
    "hutao_s5_ex1": [
        ("/dating-media/hutao_s5_ex1_cg1.jpg", "Scene 1/4 • Opening: Romantic Couple Vacation at a Fontaine Promenade Patisserie Sharing Macarons"),
        ("/dating-media/hutao_s5_ex1_cg2.jpg", "Scene 2/4 • Developing: Furina Gasping with Sparkling Eyes as She Spots Aether Kissing Hu Tao's Hand"),
        ("/dating-media/hutao_s5_ex1_cg3.jpg", "Scene 3/4 • Climax: Furina & Hu Tao Striking Grand Theatrical Poses While Hu Tao Clings to Aether's Arm"),
        ("/dating-media/hutao_s5_ex1_cg4.jpg", "Scene 4/4 • Cameo Finale: Furina Snapping a Sunset Fontaine Fountain Photo as Hu Tao Kisses Aether's Cheek"),
    ],
    "hutao_s5_ex2": [
        ("/dating-media/hutao_s5_ex2_cg1.jpg", "Scene 1/4 • Opening: Walking into Wangsheng Courtyard Hand-in-Hand with Matching Rings to Meet Zhongli"),
        ("/dating-media/hutao_s5_ex2_cg2.jpg", "Scene 2/4 • Developing: Zhongli Smiling Proudly as He Notices Their Promise Rings & Pours Osmanthus Tea"),
        ("/dating-media/hutao_s5_ex2_cg3.jpg", "Scene 3/4 • Climax: Zhongli Raising His Teacup in a Solemn Blessing Entrusting Hu Tao's Happiness to Aether"),
        ("/dating-media/hutao_s5_ex2_cg4.jpg", "Scene 4/4 • Cameo Finale: Zhongli Strolling Away Peacefully as Hu Tao Rests Her Head on Aether's Shoulder"),
    ],
}


def _build_vn_scenario(
    sc_id: str,
    stage: int,
    order: int,
    title: str,
    subtitle: str,
    location: str,
    cg_url: str,
    summary_l2: str,
    nodes: list[dict[str, Any]],
) -> dict[str, Any]:
    seq_tuples = HUTAO_SCENARIO_4CG_SEQUENCES.get(sc_id)
    if not seq_tuples:
        # Fallback 4-CG sequence for dynamic Encore or other character scenarios
        if sc_id.startswith("hutao"):
            if stage <= 1:
                seq_tuples = HUTAO_SCENARIO_4CG_SEQUENCES["hutao_s1_sc1"]
            elif stage == 2:
                seq_tuples = HUTAO_SCENARIO_4CG_SEQUENCES["hutao_s2_sc3"]
            elif stage == 3:
                seq_tuples = HUTAO_SCENARIO_4CG_SEQUENCES["hutao_s3_sc3"]
            elif stage == 4:
                seq_tuples = HUTAO_SCENARIO_4CG_SEQUENCES["hutao_s4_sc1"]
            else:
                seq_tuples = HUTAO_SCENARIO_4CG_SEQUENCES["hutao_s5_sc4"]
        else:
            cid_prefix = sc_id.split("_")[0]
            seq_tuples = [
                (f"/dating-media/{cid_prefix}_cg1.jpg", f"Scene 1/4 • Opening Arrival at {location}"),
                (f"/dating-media/{cid_prefix}_cg2.jpg", f"Scene 2/4 • Deepening Conversation with Aether"),
                (f"/dating-media/{cid_prefix}_cg1.jpg", f"Scene 3/4 • Heartfelt Climax Choice"),
                (f"/dating-media/{cid_prefix}_cg2.jpg", f"Scene 4/4 • Ending Resolution with Aether"),
            ]

    cg_sequence = [
        {
            "scene_num": idx + 1,
            "url": item_url,
            "label": item_lbl,
        }
        for idx, (item_url, item_lbl) in enumerate(seq_tuples)
    ]

    for idx, n in enumerate(nodes):
        if idx < len(cg_sequence):
            n["cg_url"] = cg_sequence[idx]["url"]
            n["scene_label"] = cg_sequence[idx]["label"]
            n["scene_progress"] = f"SCENE {idx + 1}/4"

    # Prefer the Couple CG from the sequence as the cover thumbnail on Scenario Cards!
    couple_cover = next((c["url"] for c in cg_sequence if "_sc0" in c["url"]), cg_sequence[0]["url"])

    return {
        "id": sc_id,
        "char_id": sc_id.split("_")[0] if "_" in sc_id else "hutao",
        "stage": stage,
        "order": order,
        "title": title,
        "subtitle": subtitle,
        "location": location,
        "cg_url": couple_cover,
        "cg_sequence": cg_sequence,
        "ending_cg_url": cg_sequence[3]["url"],
        "ending_scene_label": cg_sequence[3]["label"],
        "reward_affection": 35,
        "pass_threshold_score": 20,  # Out of 45 (3 nodes * 15 max); >=2 Good/Best choices passes!
        "summary_l2": summary_l2,
        "nodes": nodes,
    }


HUTAO_20_VN_SCENARIOS: list[dict[str, Any]] = [
    # ==================== STAGE 1 SCENARIOS (4 SCENARIOS) ====================
    _build_vn_scenario(
        "hutao_s1_sc1", 1, 1,
        "The 77th Director's Grand Sales Pitch",
        "Stage 1 • Episode 1 • Golden Hour Boulevard",
        "Downtown Los Santos Lamppost",
        "/dating-media/hutao_cg02.jpg",
        "Helped Hu Tao turn her quirky Wangsheng street flyer campaign into a fun afternoon walk together.",
        [
            {
                "node_idx": 0,
                "cg_url": "/dating-media/hutao_cg02.jpg",
                "narration": "Golden-hour sunlight washes over the boulevard as Hu Tao pops out from behind a vintage streetlamp, waving a stack of crimson flyers with Boo Tao bobbing beside her.",
                "inner_thought": "🦋 Butterfly Spirit: Look, Boo Tao! It's Aether! Quick, strike the most mysterious Director pose!",
                "action_cue": "*leans against the lamppost and fans out three red coupons like a magician*",
                "speaker_line": "Oho! Stop right there, esteemed Traveler! You've just walked into the 77th Director's limited-time promotion—how many VIP coupons shall I put you down for?",
                "mood": "Playful",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "🌟 'Only if the coupon includes a walk with the Director herself!'",
                        "player_text": "I'll take your finest VIP coupon—on one condition: it has to include an afternoon walk with the 77th Director herself.",
                        "reaction_thought": "Her flower-shaped pupils sparkle—he flipped her sales pitch right back into an invitation!",
                        "reaction_action": "*flips her hat brim up and stamps the gold-bordered coupon with a grin*",
                        "reaction_reply": "Aiya, a shrewd negotiator! Fine, fine—the 'Director's Personal Escort Package' is officially yours!",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "😊 'Looks like you and Boo Tao are working hard today.'",
                        "player_text": "You and Boo Tao are full of energy as always, Hu Tao. How's street business going?",
                        "reaction_thought": "She appreciates how warmly he always greets both her and Boo Tao.",
                        "reaction_action": "*pats Boo Tao's round head happily*",
                        "reaction_reply": "Much better now that my favorite customer showed up! Come keep me company while I finish this block~",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "😅 'Aren't funeral coupons scaring away the locals?'",
                        "player_text": "Uh, Hu Tao, don't you think handing out parlor coupons on a sunny street scares people?",
                        "reaction_thought": "She pouts slightly—that's the same lecture the Millelith always give her!",
                        "reaction_action": "*crosses her arms and puffs her cheeks*",
                        "reaction_reply": "Hmph! Not you sounding like the Ministry of Civil Affairs too, Aether! It's avant-garde marketing!",
                    },
                ],
            },
            {
                "node_idx": 1,
                "cg_url": "/dating-media/hutao_cg01.jpg",
                "narration": "As you walk down the sidewalk together, a passing breeze threatens to blow her stack of flyers into traffic.",
                "inner_thought": "🦋 Butterfly Spirit: Whoa, the coastal wind here is way stronger than in Liyue Harbor!",
                "action_cue": "*reaches up to hold her black bowler hat as a gust of wind sweeps past*",
                "speaker_line": "Whoa—my flyers! If those blow into the intersection, Boo Tao's going to have to chase them all evening!",
                "mood": "Surprised",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "⚡ Catch the flyers mid-air & steady her hat gently",
                        "player_text": "Got them! Hold onto your hat, Hu Tao—I caught every single flyer before it hit the ground.",
                        "reaction_thought": "Her heart skips a beat as his hand brushes near her hat brim while handing back the stack.",
                        "reaction_action": "*blinks in surprise, a soft blush tinting her cheeks as she takes the neatly stacked flyers*",
                        "reaction_reply": "O-Oh! Lightning reflexes as expected of the Traveler! You even saved my favorite hat from flying off~",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "🏃 Help Boo Tao gather the papers quickly",
                        "player_text": "On it! Boo Tao, take the left side and I'll grab the ones on the right!",
                        "reaction_thought": "She laughs happily watching Aether coordinate with Boo Tao.",
                        "reaction_action": "*cheers from the curb as every flyer is rescued*",
                        "reaction_reply": "Teamwork makes the dream work! Thanks, Aether!",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "🤷 'Maybe digital ads on EaglePhone would be easier.'",
                        "player_text": "Maybe you should stop printing paper flyers and just post ads online.",
                        "reaction_thought": "She sighs—paper talismans and hand-delivered coupons have traditional soul!",
                        "reaction_action": "*tucks the flyers away with a small pout*",
                        "reaction_reply": "Digital ads don't have my personal calligraphy on them, Aether!",
                    },
                ],
            },
            {
                "node_idx": 2,
                "cg_url": "/dating-media/hutao_cg01.jpg",
                "narration": "With the flyers safely tucked away, Hu Tao stops outside a sunlit outdoor cafe and glances up at you expectantly.",
                "inner_thought": "🦋 Butterfly Spirit: Please say yes to tea... I don't want our walk to end yet!",
                "action_cue": "*clasps her hands behind her back and rocks on her heels with a bright smile*",
                "speaker_line": "Well, since you rescued my whole marketing campaign, how about we celebrate at this patio table? First round of osmanthus tea is on me!",
                "mood": "Happy",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "🍵 'I'd love to—especially since you wore your new dress today.'",
                        "player_text": "I'd love to, Hu Tao. Sitting across from you in your 'Cherries Snow-Laden' dress is the best part of my afternoon.",
                        "reaction_thought": "A crimson butterfly flutters happily around her hat as she beams.",
                        "reaction_action": "*flashes a joyful peace sign as you sit down together*",
                        "reaction_reply": "Hehe, best afternoon ever! Order whatever cake you want, Aether—today's hangout is a 100-point success!",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "🍰 'Let's split a plate of sweet pastries with our tea.'",
                        "player_text": "Sounds great! You cover the tea and I'll get us a plate of pastries.",
                        "reaction_thought": "She nods enthusiastically, already eyeing the dessert menu.",
                        "reaction_action": "*pulls out two chairs at the sunniest table*",
                        "reaction_reply": "Deal! Nothing beats afternoon tea with my favorite travel partner~",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "⌚ 'I only have five minutes before I need to leave.'",
                        "player_text": "I can only stay for five minutes, I've got errands to run.",
                        "reaction_thought": "Her shoulders droop a tiny bit, though she hides it behind a polite smile.",
                        "reaction_action": "*orders two quick takeaway cups instead*",
                        "reaction_reply": "Aww, five minutes is barely enough to steep the tea! Next time you owe me a full hour!",
                    },
                ],
            },
        ],
    ),
    _build_vn_scenario(
        "hutao_s1_sc2", 1, 2,
        "Rhyme Battle on Mulholland Hill",
        "Stage 1 • Episode 2 • Twilight Overlook",
        "Mulholland Hilltop Stone Wall",
        "/dating-media/hutao_cg03.jpg",
        "Composed impromptu twilight verses with Hu Tao atop Mulholland Hill overlooking the city.",
        [
            {
                "node_idx": 0,
                "cg_url": "/dating-media/hutao_cg03.jpg",
                "narration": "Up on the Mulholland overlook at dusk, Hu Tao sits perched on the stone wall with her leather poetry notebook open, tapping her fountain pen against her lip.",
                "inner_thought": "🦋 Butterfly Spirit: He actually drove all the way up the mountain just to hear my new poem!",
                "action_cue": "*waves her fountain pen like a conductor's baton against the purple twilight sky*",
                "speaker_line": "Welcome to Poet Hu's open-air amphitheater, Aether! I've got the first line ready: 'Neon rivers glow beneath the mountain crest...'—now give me a second line that matches!",
                "mood": "Playful",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "✍️ '...While the girl with plum-blossom eyes outshines the rest.'",
                        "player_text": "'...While the girl with plum-blossom eyes outshines the rest.' How's that for a second line, Director?",
                        "reaction_thought": "She nearly drops her fountain pen—he rhymed effortlessly AND complimented her eyes!",
                        "reaction_action": "*blushes brightly and hurriedly writes your line into her notebook*",
                        "reaction_reply": "O-Oho?! Look at Aether sneaking a critical hit into my poetry battle! Even Xingqiu couldn't top that meter!",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "🌆 '...And a cool evening breeze puts our minds at rest.'",
                        "player_text": "'...And a cool evening breeze puts our minds at rest.' Classic Liyue rhythm!",
                        "reaction_thought": "She nods approvingly at the clean rhyme and peaceful imagery.",
                        "reaction_action": "*claps her hands together with a bright grin*",
                        "reaction_reply": "Smooth and serene! You really kept your poetic touch from our Chenyu Vale and Lantern Rite days~",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "😵 'Uh... I'm terrible at rhyming on the spot.'",
                        "player_text": "I can't think of a rhyme right now, pass!",
                        "reaction_thought": "She pouts playfully—half the fun of poetry is trying!",
                        "reaction_action": "*lightly taps your forehead with the back of her notebook*",
                        "reaction_reply": "Boo~ No forfeiting allowed in Poet Hu's arena!",
                    },
                ],
            },
            {
                "node_idx": 1,
                "cg_url": "/dating-media/hutao_cg03.jpg",
                "narration": "She flips to the next page of her notebook, where a pressed red plum blossom is tucked between the sheets.",
                "inner_thought": "🦋 Butterfly Spirit: Should I tell him I kept this plum blossom from the day we walked through Liyue together?",
                "action_cue": "*traces the pressed red plum blossom petal on her notebook page*",
                "speaker_line": "Look what I pressed between the pages, Aether. Whenever I write verses in this city, this little blossom reminds me of all the journeys we've already shared.",
                "mood": "Warm",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "🌸 'Let's fill the rest of this notebook with new memories together.'",
                        "player_text": "We've already lived through so many unforgettable days in Liyue, Hu Tao—now let's fill the rest of this notebook together here.",
                        "reaction_thought": "Her crimson eyes soften with genuine warmth as she looks out over the glittering lights.",
                        "reaction_action": "*closes the notebook gently over the blossom and smiles up at you*",
                        "reaction_reply": "Every single blank page in here is reserved for our adventures, Aether. You're my favorite co-author~",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "📖 'It still kept its bright red color after all this time.'",
                        "player_text": "You took great care of that blossom—it's still as bright red as the day it bloomed.",
                        "reaction_thought": "She smiles fondly, glad he appreciates small keepsakes.",
                        "reaction_action": "*tucks the bookmark ribbon neatly over the petal*",
                        "reaction_reply": "Of course! Things that matter to me never fade!",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "🍂 'Won't dried flowers crumble and make a mess in your bag?'",
                        "player_text": "Careful, dried petals crumble easily and get everywhere.",
                        "reaction_thought": "She sighs at the overly practical comment during a sentimental moment.",
                        "reaction_action": "*shuts the notebook with a soft thud*",
                        "reaction_reply": "Aiya, where's your sense of romance, Traveler?",
                    },
                ],
            },
            {
                "node_idx": 2,
                "cg_url": "/dating-media/hutao_cg03.jpg",
                "narration": "Night falls completely over the hilltop, and a cool mountain wind rustles Hu Tao's twin-tails.",
                "inner_thought": "🦋 Butterfly Spirit: Actually... it is getting a tiny bit chilly up here.",
                "action_cue": "*rubs her arms lightly while swinging her legs off the stone wall*",
                "speaker_line": "Hehe, looks like the stars are out! Though I may have underestimated how chilly the hilltop gets after sunset...",
                "mood": "Shy",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "🧥 Drape your warm scarf around her & offer your hand down",
                        "player_text": "Here, wrap my scarf around your neck and take my hand—I've got the heater running in the car.",
                        "reaction_thought": "She holds the warm scarf to her chin, her cheeks glowing warmer than the car heater.",
                        "reaction_action": "*takes your hand to hop down from the wall, standing close beside you*",
                        "reaction_reply": "Mmm, your scarf smells so warm... Thank you, Aether. Let's go grab hot tea on the way back!",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "🚗 'Hop in the car, I'll turn the seat warmers on!'",
                        "player_text": "Come hop in the passenger seat, I'll turn the heater on full blast for you.",
                        "reaction_thought": "She hops down cheerfully and skips toward the passenger door.",
                        "reaction_action": "*hops down from the wall with a grateful smile*",
                        "reaction_reply": "Yay! Five-star chauffeur service from Aether!",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "🥶 'Told you that short skirt wasn't meant for mountain wind.'",
                        "player_text": "That's what happens when you wear a short skirt up a windy hill.",
                        "reaction_thought": "She glares playfully—fashion comes first!",
                        "reaction_action": "*huffs and walks ahead toward the car*",
                        "reaction_reply": "Fashion knows no temperature, Aether!",
                    },
                ],
            },
        ],
    ),
    _build_vn_scenario(
        "hutao_s1_sc3", 1, 3,
        "Midnight Ghost-Hunting Prank",
        "Stage 1 • Episode 3 • Misty Alleyway",
        "Old Chinatown Lantern Alley",
        "/dating-media/hutao_cg02.jpg",
        "Joined Hu Tao's midnight ghost-hunting prank in the lantern alley and rescued a stray kitten together.",
        [
            {
                "node_idx": 0,
                "cg_url": "/dating-media/hutao_cg02.jpg",
                "narration": "At midnight in a misty lantern-lit alley, Hu Tao waves you over with a flashlight held dramatically under her chin.",
                "inner_thought": "🦋 Butterfly Spirit: Hehe, let's see if I can make the fearless Traveler jump just a tiny bit!",
                "action_cue": "*wiggles her fingers in spooky shadow-puppets on the brick wall*",
                "speaker_line": "Boo!! Welcome to Hu Tao's Midnight Mystery Tour, Aether! Rumor has it a mysterious phantom has been rustling the boxes at the end of this alley~",
                "mood": "Mischievous",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "👻 Play along dramatically & whisper 'Lead the way, Director!'",
                        "player_text": "Oh no, how terrifying! Good thing I have the 77th Director of Wangsheng right beside me to protect me.",
                        "reaction_thought": "She giggles in delight—he's playing along with her spooky theater 100%!",
                        "reaction_action": "*puffs out her chest proudly and hooks her finger around your sleeve*",
                        "reaction_reply": "Hehe, stay close to me then, Traveler! Neither ghosts nor ghouls can touch you while I'm on duty~",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "🔦 Shine your light ahead to investigate with her",
                        "player_text": "Let's check it out together, Hu Tao. I've got your back.",
                        "reaction_thought": "She grins, loving any excuse for a midnight adventure with Aether.",
                        "reaction_action": "*tiptoes theatricality beside you toward the wooden crates*",
                        "reaction_reply": "On three, we peek behind the crates together!",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "😑 'It's obviously just the wind or a rat, Hu Tao.'",
                        "player_text": "There are no ghosts in this alley, it's just the wind.",
                        "reaction_thought": "She deflates—spoiling the atmosphere before the reveal!",
                        "reaction_action": "*lowers the flashlight with a dramatic sigh*",
                        "reaction_reply": "Aiya, you're supposed to play along with the suspense!",
                    },
                ],
            },
            {
                "node_idx": 1,
                "cg_url": "/dating-media/hutao_cg01.jpg",
                "narration": "Suddenly, a tiny white kitten leaps out from the cardboard box with a loud 'Mew!', startling Hu Tao so much she stumbles backward right against your chest.",
                "inner_thought": "🦋 Butterfly Spirit: Eek!! It wasn't a ghost, it was a kitten—wait, Aether's arms are catching me!",
                "action_cue": "*gasps in surprise as you steady her shoulders against your chest*",
                "speaker_line": "W-Whoa! Okay, I admit I didn't expect the phantom to have whiskers and four paws! ...Thanks for catching me, Aether.",
                "mood": "Flustered",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "😊 Hold her steady & tease her gently: 'The spookiest Director got spooked!'",
                        "player_text": "Careful, I've got you. Who knew the fearless Director of Wangsheng could get ambushed by a kitten?",
                        "reaction_thought": "Her ears turn pink as she realizes she's still leaning against his chest.",
                        "reaction_action": "*crouches down quickly to pet the kitten to hide her blushing cheeks*",
                        "reaction_reply": "I-I wasn't spooked, I was just dodging tactically! Look how cute this little guy is, though~",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "🐱 Crouch down together and feed the stray kitten",
                        "player_text": "Glad you're okay! Look, the little kitten seems hungry—let's give it some fish snacks.",
                        "reaction_thought": "She smiles warmly as the kitten purrs around both of your hands.",
                        "reaction_action": "*watches the kitten curl around your fingers with a soft smile*",
                        "reaction_reply": "Even stray kittens immediately trust you, Aether~",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "😂 Laugh out loud at her clumsy stumble",
                        "player_text": "Haha, you almost fell flat on your back!",
                        "reaction_thought": "She pouts and straightens her hat indignantly.",
                        "reaction_action": "*adjusts her bowler hat with a huff*",
                        "reaction_reply": "Hmph! Laugh one more time and Boo Tao will tickle your ears tonight!",
                    },
                ],
            },
            {
                "node_idx": 2,
                "cg_url": "/dating-media/hutao_cg01.jpg",
                "narration": "After feeding the kitten and watching it trot safely back to the shopkeeper's porch, Hu Tao walks beside you under the warm streetlamps.",
                "inner_thought": "🦋 Butterfly Spirit: Even a silly midnight prank turns into a warm memory whenever Aether comes along.",
                "action_cue": "*swings her arms happily beside yours as you exit the alley*",
                "speaker_line": "So, Traveler—on a scale from one to ten, how would you rate tonight's Midnight Mystery Tour?",
                "mood": "Happy",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "💖 'Eleven out of ten—any midnight walk with you is my favorite.'",
                        "player_text": "Eleven out of ten, Hu Tao. Any midnight walk with you is guaranteed to be the highlight of my night.",
                        "reaction_thought": "Her heart does a happy flip under the streetlamp.",
                        "reaction_action": "*beams up at you with shining crimson eyes*",
                        "reaction_reply": "Hehe, eleven out of ten! Then I'm booking you for every future midnight adventure in advance, Aether!",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "🌟 'Ten out of ten—we found the cutest ghost in town!'",
                        "player_text": "Ten out of ten! Rescuing that kitten with you was great.",
                        "reaction_thought": "She grins and gives a thumbs-up.",
                        "reaction_action": "*gives a cheerful wink*",
                        "reaction_reply": "Another successful night patrol for the Hu Tao & Aether team!",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "🥱 'Five out of ten, I'm pretty sleepy now.'",
                        "player_text": "Five out of ten, I'm getting tired.",
                        "reaction_thought": "She pouts at the lukewarm score.",
                        "reaction_action": "*sighs playfully*",
                        "reaction_reply": "Tough critic! Next time I'll bring stronger tea!",
                    },
                ],
            },
        ],
    ),
    _build_vn_scenario(
        "hutao_s1_sc4", 1, 4,
        "Old Man Zhongli's Surprise Invoice",
        "Stage 1 • Episode 4 • Antique Tea House",
        "Verona Promenade Tea Pavilion",
        "/dating-media/hutao_cg01.jpg",
        "Helped Hu Tao handle Zhongli's extravagant antique tea bill with humor and shared a relaxing dessert.",
        [
            {
                "node_idx": 0,
                "cg_url": "/dating-media/hutao_cg01.jpg",
                "narration": "At the antique tea pavilion, Hu Tao stares in comedic disbelief at a scroll-length receipt labeled 'Charge to Wangsheng Parlor — Consultant Zhongli'.",
                "inner_thought": "🦋 Butterfly Spirit: Bird cages, rare tea leaves, AND jade coasters?! That old consultant strikes again!",
                "action_cue": "*holds up the meter-long paper invoice with both hands, her eyes wide*",
                "speaker_line": "Aiyaaa, Aether, look at this receipt!! Zhongli ordered vintage Sunglo tea AND a pair of painted porcelain cups and told the shopkeeper to bill it to me!",
                "mood": "Exasperated",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "🍵 Laugh & offer to split the tea tasting with her so she enjoys it too",
                        "player_text": "Classic Zhongli! Since the vintage tea is already paid for, sit down with me and let's enjoy the best pot together so it doesn't go to waste!",
                        "reaction_thought": "Her frustration vanishes instantly—turning Zhongli's bill into a tea date with Aether is genius!",
                        "reaction_action": "*bursts out laughing and sits down across from you*",
                        "reaction_reply": "Wait—you're a genius, Aether! If the parlor is paying for luxury tea, the Director and her VIP guest should drink the best pot ourselves!",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "💼 Offer to help her negotiate a discount with the shopkeeper",
                        "player_text": "Let me talk to the shopkeeper with you—we'll get a regular-client discount for Wangsheng.",
                        "reaction_thought": "She beams, grateful to have a reliable partner.",
                        "reaction_action": "*nods eagerly and folds the receipt*",
                        "reaction_reply": "With the famous Traveler vouching for me, we saved 30%! You're a lifesaver, Aether!",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "😐 'You really need stricter accounting rules at work.'",
                        "player_text": "You should probably audit your parlor budget better.",
                        "reaction_thought": "She groans—she wanted sympathy, not an accounting lecture!",
                        "reaction_action": "*slumps over the tea table*",
                        "reaction_reply": "Don't remind me about spreadsheets on my break, Aether~",
                    },
                ],
            },
            {
                "node_idx": 1,
                "cg_url": "/dating-media/hutao_cg01.jpg",
                "narration": "The shopkeeper brings out the fragrant Sunglo tea along with two delicate plum-blossom pastries.",
                "inner_thought": "🦋 Butterfly Spirit: Actually, sitting here sipping rare tea with Aether makes the whole bill worth it.",
                "action_cue": "*pours a steaming cup for you first with graceful two-handed etiquette*",
                "speaker_line": "Here you go, Aether—the first pour goes to my favorite companion. Tell me, does Zhongli's taste in tea live up to the hype?",
                "mood": "Warm",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "💖 'The tea is great, but the company pouring it is what makes it special.'",
                        "player_text": "The tea is fragrant, Hu Tao, but having you pour it across the table is what makes it taste ten times better.",
                        "reaction_thought": "She hides a shy smile behind her teacup as her cheeks turn rosy.",
                        "reaction_action": "*takes a small sip to hide her blushing smile*",
                        "reaction_reply": "Oho~ Keep sweet-talking me like that and I might let Zhongli order tea here every week just as an excuse to bring you!",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "🍰 Offer her the sweeter plum-blossom pastry",
                        "player_text": "It's delicious! Here, take the extra plum-blossom pastry—I know you have a sweet tooth after afternoon tea.",
                        "reaction_thought": "Her eyes light up as she happily accepts the pastry.",
                        "reaction_action": "*takes a happy bite of the pastry*",
                        "reaction_reply": "Mmm! Sweet pastry + fragrant tea + Aether = perfection!",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "🍵 Gulp it down quickly like plain water",
                        "player_text": "Tastes like normal hot leaf water to me.",
                        "reaction_thought": "She gasps in mock horror at his tea-drinking speed.",
                        "reaction_action": "*covers her eyes playfully*",
                        "reaction_reply": "Aiya! If Zhongli heard you call vintage Sunglo 'hot leaf water', a meteor would fall on us!",
                    },
                ],
            },
            {
                "node_idx": 2,
                "cg_url": "/dating-media/hutao_cg01.jpg",
                "narration": "As the afternoon sun slants through the wooden lattice, Hu Tao rests her chin in her hands and gazes at you.",
                "inner_thought": "🦋 Butterfly Spirit: Every time I'm with Aether, even ordinary errands feel like a holiday.",
                "action_cue": "*tilts her head with a fond, lingering smile*",
                "speaker_line": "Thanks for turning a headache of a bill into such a lovely afternoon, Aether. Promise you'll join me for tea again soon?",
                "mood": "Affectionate",
                "choices": [
                    {
                        "id": "c1", "score": 15, "grade": "BEST",
                        "label": "🤝 'Anytime you call, Hu Tao, I'll be at your table.'",
                        "player_text": "It's a promise, Hu Tao. Anytime you want company for tea—or anything else—just message me on EaglePhone.",
                        "reaction_thought": "Warmth blooms in her chest; she knows she can always count on him.",
                        "reaction_action": "*reaches across the table and taps her pinky finger against yours in a promise*",
                        "reaction_reply": "Pinky promise sealed! Don't be surprised when your EaglePhone chimes tonight~",
                    },
                    {
                        "id": "c2", "score": 10, "grade": "GOOD",
                        "label": "😊 'Next time the tea and cake are on me!'",
                        "player_text": "Definitely! And next time, the tea and pastries are 100% on me.",
                        "reaction_thought": "She grins brightly at the future date plan.",
                        "reaction_action": "*flashes a cheerful peace sign*",
                        "reaction_reply": "Deal! I'll hold you to that, Traveler~",
                    },
                    {
                        "id": "c3", "score": 0, "grade": "AWKWARD",
                        "label": "👋 'Maybe if I'm not busy.'",
                        "player_text": "We'll see if my schedule is free.",
                        "reaction_thought": "She pouts slightly at the vague answer.",
                        "reaction_action": "*taps the table lightly*",
                        "reaction_reply": "Hmph, make sure you clear a VIP slot for me!",
                    },
                ],
            },
        ],
    ),
]

# ==============================================================================
# 4B. STAGE 2..5 VISUAL NOVEL SCENARIOS FOR HU TAO (16 MORE SCENARIOS = 20 TOTAL)
# ==============================================================================
def _build_3node_scenario_compact(
    sc_id: str,
    stage: int,
    order: int,
    title: str,
    subtitle: str,
    location: str,
    cg_url: str,
    summary_l2: str,
    n1: tuple[str, str, str, str, str, str],
    n2: tuple[str, str, str, str, str, str],
    n3: tuple[str, str, str, str, str, str],
) -> dict[str, Any]:
    """Helper to construct rich 3-node branching Visual Novel scenarios cleanly."""
    nodes = []
    for idx, (narration, thought, action, line, best_lbl_and_txt, good_lbl_and_txt) in enumerate((n1, n2, n3)):
        best_lbl, best_txt, best_rep = best_lbl_and_txt.split("||")
        good_lbl, good_txt, good_rep = good_lbl_and_txt.split("||")
        nodes.append(
            {
                "node_idx": idx,
                "cg_url": cg_url,
                "narration": narration,
                "inner_thought": f"🦋 Butterfly Spirit: {thought}",
                "action_cue": action,
                "speaker_line": line,
                "mood": "Affectionate" if stage >= 3 else "Playful",
                "choices": [
                    {
                        "id": "c1",
                        "score": 15,
                        "grade": "BEST",
                        "label": f"🌟 {best_lbl}",
                        "player_text": best_txt,
                        "reaction_thought": "Her crimson plum-blossom eyes light up as a spirit butterfly circles her.",
                        "reaction_action": "*beams warmly and steps closer to Aether*",
                        "reaction_reply": best_rep,
                    },
                    {
                        "id": "c2",
                        "score": 10,
                        "grade": "GOOD",
                        "label": f"😊 {good_lbl}",
                        "player_text": good_txt,
                        "reaction_thought": "She smiles happily, enjoying the natural rhythm between them.",
                        "reaction_action": "*nods with a cheerful grin*",
                        "reaction_reply": good_rep,
                    },
                    {
                        "id": "c3",
                        "score": 0,
                        "grade": "AWKWARD",
                        "label": "😅 Give a distracted, half-hearted response",
                        "player_text": "Sorry, I was checking my phone—what did you say?",
                        "reaction_thought": "She puffs her cheeks slightly—she wanted Aether's full attention!",
                        "reaction_action": "*taps your arm playfully to bring your focus back*",
                        "reaction_reply": "Hmph!Eyes on the Director when we're in the middle of a hangout, Aether!",
                    },
                ],
            }
        )
    return _build_vn_scenario(sc_id, stage, order, title, subtitle, location, cg_url, summary_l2, nodes)


HUTAO_20_VN_SCENARIOS.extend(
    [
        # ---------------- STAGE 2 (200 - 399 PTS): 4 SCENARIOS ----------------
        _build_3node_scenario_compact(
            "hutao_s2_sc1", 2, 1,
            "'Cherries Snow-Laden' Private Runway",
            "Stage 2 • Episode 1 • Coastal Convertible Cruise",
            "Santa Maria Coastal Highway",
            "/dating-media/hutao_cg04.jpg",
            "Cruised down the coastal highway with Hu Tao in her Cherries Snow-Laden outfit and shared strawberry boba.",
            (
                "Hu Tao hops into your convertible wearing her white-and-crimson 'Cherries Snow-Laden' dress and round red sunglasses, holding two iced strawberry bobas.",
                "He can't take his eyes off my new outfit—Xiangling's tailoring gets an A+!",
                "*tips her round red sunglasses down on the bridge of her nose and winks*",
                "Ta-da! Private passenger-seat runway show just for you, Aether! Well? How does the festive dress look in the coastal sunshine?",
                "Praise how the crimson ribbons frame her smile||The crimson ribbons and white dress look stunning in the sunlight, Hu Tao—and that wink over the sunglasses is unbeatable.||Hehe, ten out of ten! Here's your strawberry boba, my handsome chauffeur~",
                "Compliment Xiangling's tailoring & her hat||Xiangling really outdid herself! The white bowler hat suits you so well.||Right?! Even Boo Tao got a matching mini-hat!",
            ),
            (
                "As you cruise along the ocean highway, the sea breeze sends her long twin-tails fluttering across the headrest.",
                "Riding beside Aether with the ocean breeze and music playing feels so carefree.",
                "*holds out her strawberry boba straw toward you while you keep one hand on the wheel*",
                "Since both your hands are busy steering us smoothly along the coast, say 'aaah'—I'll let you have a sip of my brown-sugar boba!",
                "Take a sip directly from her straw & thank her||Mmm, that's sweet! Though it tastes even sweeter because you're feeding me, Hu Tao.||O-Oho! Bold move, Traveler—an indirect kiss at sixty miles an hour!",
                "Thank her for being the best co-pilot||Thanks, Hu Tao! Having you in the passenger seat makes every drive ten times better.||Anytime! I'm officially your permanent co-pilot!",
            ),
            (
                "You pull over at the sunny coastal vista point, where palm trees sway above the sparkling blue waves.",
                "I want to save a photo of this exact moment so I can look at it whenever I miss him.",
                "*leans her shoulder against yours and holds up her EaglePhone for a two-shot selfie*",
                "Quick, Aether, lean in close! Let's take a coastal snapshot to commemorate our first official boba cruise!",
                "Lean close against her cheek & flash a matching peace sign||Cheese! Make sure you send that photo straight to my EaglePhone so I can set it as my favorite memory.||Sent! And I'm pinning it to the very top of my album too, Aether~",
                "Smile warmly into the camera beside her||Got it! That ocean backdrop looks amazing behind us.||Hehe, frame-worthy shot!",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s2_sc2", 2, 2,
            "Firefly Tea by the Quiet Lake",
            "Stage 2 • Episode 2 • Reminiscing Past Quests",
            "Bayside Firefly Shore",
            "/dating-media/hutao_cg03.jpg",
            "Reminisced with Hu Tao by the firefly lake about helping Big G and Little Meng in 'Yet the Butterfly Flutters Away'.",
            (
                "Blue fireflies drift above the quiet lakeside as Hu Tao pours two cups of warm osmanthus tea from a thermos.",
                "The glow on the water looks just like the ordinary border we visited in Wuwang Hill...",
                "*watches a glowing firefly land near her teacup with a nostalgic smile*",
                "Seeing these lights over the water reminds me of when we helped Big G and Little Meng find closure in the past, Aether. Remember how peaceful Wuwang Hill looked afterward?",
                "Recall how deeply you admired her compassion back then||I remember every detail of that day, Hu Tao. Watching how gently you guided both the living and the departed made me admire you so much.||Hearing you say that means the world to me, Aether... Most people misunderstand my work, but you always saw my heart.",
                "Agree that you two have always made a great team||We really made an unstoppable team back in Wuwang Hill—and we still do today.||Hehe, the best duo on both sides of the border!",
            ),
            (
                "A gentle breeze ripples the lake surface, and Hu Tao scoots a little closer to you on the wooden bench.",
                "Back then we were new friends... now sitting next to Aether feels like coming home.",
                "*lets her knee brush lightly against yours on the bench*",
                "Back then, I told you Wangsheng's motto is 'respect the departed, preserve the living.' Lately, though... preserving my happy hours with you has become my top priority.",
                "Tell her that making her happy is your top priority too||And making sure the 77th Director always has a reason to smile is my top priority, Hu Tao.||Aiya, my heart just did a somersault! Keep talking like that and the fireflies will blush too!",
                "Clink teacups with her under the fireflies||Then let's toast to many more peaceful nights like this together.||Cheers to us, Aether!",
            ),
            (
                "As the last tea is finished, a crimson spirit butterfly materializes from her fingertips and hovers between you.",
                "My spirit butterflies only glow this warmly when I'm completely relaxed around someone.",
                "*lets the glowing butterfly perch on the back of your hand*",
                "Look—even my spirit butterfly refuses to leave your hand, Aether. I think it likes your warm aura just as much as I do~",
                "Gently touch her fingertips where the butterfly rests||If your butterflies love my warmth, then you're welcome to hold my hand whenever you want, Hu Tao.||H-Hold me to that promise very soon, Traveler~",
                "Smile & watch the butterfly glow on your hand||It's beautiful, Hu Tao. Thank you for sharing this quiet place with me.||Anytime, my favorite confidant~",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s2_sc3", 2, 3,
            "Spicy vs. Sweet Night Market Bet",
            "Stage 2 • Episode 3 • Lantern Market Feast",
            "Chinatown Night Market Stall",
            "/dating-media/hutao_cg05.jpg",
            "Shared steamed shrimp dumplings and won Hu Tao's playful chili-vs-sweet night market challenge.",
            (
                "Under strings of glowing red lanterns at the night market, Hu Tao grins mischievously over a steaming bamboo basket of dumplings.",
                "Let's see if Aether trusts me enough to eat straight from my chopsticks!",
                "*holds out a plump steamed dumpling with her chopsticks while hiding a small chili saucer behind her back*",
                "Night market rule number one, Aether: the Director feeds you the first bite! Come on, say 'aaah'—do you trust me?",
                "Look her straight in the eyes & take the bite from her chopsticks||I trust you 100%, Hu Tao—even if it's spicy, I'll never turn down a bite from you.||Hehe, surprise! It's actually a sweet crystal shrimp dumpling—I saved the best one for you!",
                "Playfully peek behind her back first, then eat it||I see that chili saucer behind your back, prankster! Feed me the safe one first!||Busted! Okay, okay, here's the sweet shrimp one!",
            ),
            (
                "Next, a plate of golden sugar-glazed sesame balls arrives, and Hu Tao eyes the last one on the plate.",
                "Ooh, the last sesame ball! Should I let Aether have it or challenge him for it?",
                "*hovers her chopsticks over the last golden sesame ball*",
                "Uh-oh, only one sugar sesame ball left! Tell me one thing you like about hanging out with me, and it's yours—or better yet, we split it!",
                "Feed half of the sesame ball to her first||What I like most is how your laugh lights up the whole night market. Here—you take the first bite, and I'll take the second.||Mmm!! So sweet—and I don't just mean the sesame glaze! Here, eat the other half~",
                "Suggest splitting it fifty-fifty||Everything's more fun when you're around, Hu Tao. Let's split it right down the middle!||Deal! Half for you, half for me!",
            ),
            (
                "After the meal, you walk past a stall selling handmade red plum-blossom charms.",
                "If Aether buys me a charm here, I'll hang it right on my EaglePhone!",
                "*pauses by the lantern stall, admiring a pair of braided red-and-gold tassels*",
                "Ooh, look at those matching red-and-gold charms, Aether! Red for Hu Tao, gold for the Traveler~",
                "Buy the matching pair & tie the red one onto her phone||Let's get the pair—I'll keep the gold one, and I'll tie this crimson plum-blossom charm onto your phone right now.||Yay!! Matching charms with Aether! Every time I text you, I'll see it dangling there~",
                "Buy the charm for her as a souvenir||Here, a souvenir from our night market feast!||Thank you, Aether! I'll treasure it!",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s2_sc4", 2, 4,
            "Drifting Under the Plum Blossoms",
            "Stage 2 • Episode 4 • Sunset Pavilion Nap",
            "Plum Blossom Garden Pavilion",
            "/dating-media/hutao_cg06.jpg",
            "Guarded Hu Tao's peaceful nap beneath the plum blossoms and wrapped her in your warm golden scarf.",
            (
                "At the quiet garden pavilion at sunset, you find Hu Tao resting her head on her folded arms on the wooden table, her hat set aside as red plum blossoms drift down.",
                "Mmm... stayed up all night writing poetry and handling ceremonies... just five minutes of rest...",
                "*breathes softly in her sleep as a red petal lands on her cheek*",
                "Zzz... mmm, five more steamed buns, Aether... don't go yet...",
                "Gently drape your warm scarf over her shoulders & brush the petal away||Sleep as long as you need, Hu Tao. I'll stay right here beside you until you wake up.||*stirs softly and opens her crimson eyes with a sleepy, unguarded smile* ...Aether? Your scarf feels so warm...",
                "Sit quietly beside her to guard her rest||I'll keep watch so nobody disturbs your nap, Director.||*blinks awake with a soft yawn* Hehe, how long were you sitting there?",
            ),
            (
                "Still half-sleepy and without her usual theatrical mask, Hu Tao rubs her eyes and leans her head lightly against your arm.",
                "I never let anyone see me this drowsy and unguarded... only Aether makes me feel this safe.",
                "*rests her temple lightly against your upper arm while wrapped in your scarf*",
                "Usually I have to stay sharp 24/7 as the 77th Director... How come whenever you're next to me, Aether, all my tiredness just melts away?",
                "Put your arm gently around her shoulders so she can lean comfortably||Because with me, you never have to be the strong Director, Hu Tao—you can just be yourself and rest on my shoulder.||Mmm... don't spoil me this much, or I'll never want to lean on anyone else's shoulder ever again...",
                "Offer to brew her a warm cup of herbal tea||You work way too hard, Hu Tao. Lean on me as long as you want while I pour you warm tea.||Thank you, Aether... you're the kindest person I know.",
            ),
            (
                "As twilight deepens, she straightens up reluctantly, still keeping your scarf wrapped around her neck.",
                "I really don't want to give his scarf back yet—it smells just like him.",
                "*hugs the ends of your scarf with both hands and looks up with a shy smile*",
                "Hey, Aether... would you mind if I borrowed your scarf until our next hangout? I promise I'll return it with interest!",
                "Tell her she can keep it & kiss the top of her hat||Keep it as long as you like, Hu Tao—and the only interest I want is seeing you again tomorrow.||Deal!! Tomorrow can't come fast enough, Aether~",
                "Smile & let her borrow the scarf||Of course you can borrow it—it looks cute on you!||Hehe, best trade ever!",
            ),
        ),

        # ---------------- STAGE 3 (400 - 599 PTS): 4 SCENARIOS ----------------
        _build_3node_scenario_compact(
            "hutao_s3_sc1", 3, 1,
            "Echoes of the Gate of Death",
            "Stage 3 • Episode 1 • Lantern Walk by the Pier",
            "Verona Lantern Boardwalk",
            "/dating-media/hutao_cg07.jpg",
            "Walked hand-in-hand with Hu Tao under the boardwalk lanterns as she opened her heart about the Gate of Death.",
            (
                "Walking under a canopy of glowing red lanterns along the boardwalk, Hu Tao slows her pace and reaches her fingers hesitantly toward your hand.",
                "Back at the Gate of Death during Lantern Rite, Aether grabbed my hand and refused to let me go...",
                "*brushes the back of her hand softly against yours beneath the lantern glow*",
                "Aether... back during Lantern Rite, when I offered my life as the Eighth Adeptus to seal the border, I really thought I wouldn't be coming back. Until your hand reached through the darkness and pulled me home.",
                "Intertwine your fingers tightly with hers||I told you back then and I'll tell you every day: I would cross any border to bring you back to my side, Hu Tao.||*squeezes your hand tightly, her cheeks flushing deep crimson* Hearing you say that makes my heart beat so fast it hurts—in the best way.",
                "Hold her hand warmly under the lanterns||I could never let you face that darkness alone, Hu Tao. I'm glad you're here with me now.||Me too, Aether... being alive right here with you is my greatest treasure.",
            ),
            (
                "Crimson spirit butterflies begin to materialize around your intertwined hands, drifting upward into the night sky.",
                "Whenever Aether holds my hand like this, I don't feel like just a friend anymore...",
                "*looks down at your joined hands, then up into your golden eyes with a shy blush*",
                "You know, the 77th Director isn't supposed to be scared of anything... but the one thing that scares me now is the thought of ever letting go of this hand.",
                "Lift her hand & press a gentle kiss to her knuckles||Then you never have to worry, Hu Tao—because I'm never letting go of your hand either.||A-Aether!! Kissing my hand under the lanterns like a prince... you're going to make my spirit butterflies explode!",
                "Promise to walk beside her wherever she goes||You don't ever have to let go, Hu Tao. I'm staying right beside you.||Promise sealed under the lanterns, Aether~",
            ),
            (
                "At the end of the boardwalk, she leans her head against your shoulder as the ocean reflects the red lantern light.",
                "I'm completely, hopelessly in love with this Traveler.",
                "*rests her cheek against your shoulder while still holding your hand*",
                "Let's stay like this for just a few more minutes, Aether... Tonight, I don't want to be the Director—I just want to be your girl.",
                "Wrap your arm around her shoulder & hold her close||Take all the time in the world, Hu Tao. Tonight and every night, you're my girl.||Mmm... best night of my life, Aether.",
                "Hold her hand & watch the lantern reflections together||As long as you want, Hu Tao.||Thank you, my dearest Traveler~",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s3_sc2", 3, 2,
            "One Umbrella, Two Heartbeats",
            "Stage 3 • Episode 2 • Neon Rain Shower",
            "Downtown Neon Rain Street",
            "/dating-media/hutao_cg08.jpg",
            "Shared one small umbrella with Hu Tao in a sudden neon evening rainstorm, pressed shoulder-to-shoulder.",
            (
                "A sudden evening shower turns the neon streets into shimmering mirrors. Hu Tao ducks under your clear umbrella, pressing right against your side.",
                "Hehe, good thing I kept my spare umbrella hidden in my bag so we HAVE to share his!",
                "*stands pressed shoulder-to-shoulder with you under the clear umbrella, looking up with a shy blush*",
                "Whoa, talk about sudden rain! Good thing you had an umbrella, Aether—though it's a little cozy for two, isn't it?",
                "Slip your arm around her waist & pull her closer so she stays dry||Here—let me pull you right against my side so the rain doesn't touch your shoulder, Hu Tao.||*blushes bright red as your arm wraps around her waist* E-Eek! Now I can literally feel your heartbeat against my ribs!",
                "Tilt the umbrella toward her side to shield her dress||Make sure you stay right next to me so your 'Cherries Snow-Laden' dress stays dry!||You're always taking care of me first, Aether~",
            ),
            (
                "Rain patters rhythmically on the clear canopy above as neon pink and gold reflections dance in her flower-shaped pupils.",
                "His face is only inches away... if I stand on tiptoe right now...",
                "*gazes up at your lips, her breath warm in the cool rain air*",
                "Hey, Aether... is that the rain drumming on the umbrella, or is one of our hearts beating way too loud right now?",
                "Whisper softly against her ear: 'It's both of our hearts, Hu Tao.'||I think both of our hearts are racing because of how close you're looking at me right now, Hu Tao.||*shivers and buries her blushing face against your collarbone* Unfair!! You can't whisper in my ear like that when I have nowhere to run!",
                "Touch her warm cheek & smile tenderly||Definitely our hearts, Hu Tao—especially when you look up at me like that.||Hehe... guilty as charged~",
            ),
            (
                "Even as the rain softens to a mist near her doorstep, Hu Tao holds onto your coat lapel, reluctant to step out from under the umbrella.",
                "I don't want the rain to stop yet...",
                "*tugs gently on your lapel with both hands*",
                "Looks like the rain is stopping... Do I really have to step out from under your umbrella already, Aether?",
                "Lean down & kiss her forehead before walking her to the door||Even when the rain stops, you don't have to leave my arms, Hu Tao.||*touches her forehead with a dreamy, lovestruck smile* Next time... aim a little lower than my forehead, okay, Aether?",
                "Offer to stay with her for hot tea inside||Then let's keep the date going inside over a pot of hot tea!||Yes please!! Come right in!",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s3_sc3", 3, 3,
            "Top of the Santa Maria Ferris Wheel",
            "Stage 3 • Episode 3 • Sunset Confession",
            "Santa Maria Pier Ferris Wheel",
            "/dating-media/hutao_cg09.jpg",
            "Shared a heartfelt romantic confession with Hu Tao at the peak of the Santa Maria Ferris wheel at sunset.",
            (
                "As your glass Ferris wheel cabin rises high above the ocean at golden-pink sunset, Hu Tao takes off her hat and sets it on the seat.",
                "Up here above the whole city, it's just Aether and me...",
                "*moves from the opposite bench to sit right next to you as the cabin climbs*",
                "Look how tiny the pier looks from up here, Aether! Though honestly... I didn't bring you on the Ferris wheel just to look at the ocean.",
                "Turn to face her & take both of her hands||I didn't come up here for the view either, Hu Tao—the only sight I wanted to look at is you.||*her breath catches as her cheeks turn rose-pink* Aether...",
                "Smile warmly as she sits beside you||Sitting right next to you at sunset beats any view in the world.||Hehe, glad we're on the same wavelength!",
            ),
            (
                "As the cabin reaches the very top of the wheel, golden sunset light floods the glass, and Hu Tao leans forward to gently touch your cheek.",
                "No jokes, no riddles—I want him to know how completely my heart belongs to him.",
                "*cradles your cheek in her warm palm, her crimson eyes shining with tender emotion*",
                "When I take off my Director's hat, I'm just a girl who fell head over heels for the Traveler who always stood by her. Tell me, Aether... do you feel the same way about me?",
                "Place your hand over hers on your cheek & confess your love||I fell for you a long time ago, Hu Tao—your laugh, your kindness, and every moment we share. I want you as my girlfriend.||*tears of joy sparkle in her flower-shaped pupils before she throws her arms around your neck* Yes!! A thousand times yes, my dearest Aether!",
                "Pull her close & tell her she holds your heart||You're the most special person in my life, Hu Tao. My heart is yours.||And mine is yours, Aether—now and forever!",
            ),
            (
                "As the cabin slowly descends toward the glowing pier lights, Hu Tao stays curled in your embrace, her fingers laced with yours.",
                "We're officially together... my heart feels like it could fly higher than this Ferris wheel!",
                "*leans up and presses a soft, lingering kiss to your cheek*",
                "From this moment on, no take-backs, okay? You're officially my boyfriend, Aether~",
                "Kiss her lips softly before the cabin doors open||No take-backs ever, my love. Come on, let's celebrate our first night as a couple!||*blushes radiantly, touching her lips with a blissful smile* Best sunset of my entire life~",
                "Hold her close & walk off the pier hand-in-hand||Official and permanent, Hu Tao. Let's go celebrate!||Hehe, lead the way, boyfriend~",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s3_sc4", 3, 4,
            "Jealous Boo Tao & The Starry Car Hood",
            "Stage 3 • Episode 4 • Stargazing Drive",
            "Verdant Meadows Starlight Overlook",
            "/dating-media/hutao_cg07.jpg",
            "Stargazed on the hood of your car with Hu Tao as she playfully claimed exclusive rights to your attention.",
            (
                "Parked under a blanket of stars, you and Hu Tao sit side-by-side on the warm hood of your car while Boo Tao floats nearby.",
                "Earlier today, someone in town asked Aether for directions and smiled at him way too long—hmph!",
                "*puffs her cheeks in cute jealousy and pokes your chest with her finger*",
                "Ahem! Full disclosure, Aether: I saw that girl downtown asking you for directions earlier! Just so we're clear, your passenger seat—and your heart—are 100% leased to Hu Tao!",
                "Laugh fondly, pull her into your lap & kiss her temple||Are you jealous, my cute Director? You never have to worry—nobody else comes close to you in my eyes.||*melts instantly in your arms, hiding a happy grin* H-Hmph, I wasn't THAT jealous! I just wanted to hear you say it while holding me~",
                "Reassure her warmly that she's the only one for you||My passenger seat and my heart belong exclusively to you, Hu Tao.||Hehe, good answer! Approved by both me and Boo Tao!",
            ),
            (
                "A shooting star streaks across the midnight sky above the desert cliffs, and Hu Tao gasps, pointing upward.",
                "A real shooting star—just like a Falling Star from Teyvat!",
                "*leans back against your chest on the car hood, pointing up at the meteor trail*",
                "Look, Aether, a shooting star!! Quick, make a wish with me before it fades!",
                "Whisper in her ear: 'My wish already came true—I'm holding her right now.'||I don't need to wish on a star anymore, Hu Tao, because I'm already holding my wish in my arms.||*turns her head in your embrace, her cheeks glowing under the starlight* You always know how to make my heart melt completely, Aether...",
                "Wish for endless happy nights together with Hu Tao||I wished that you and I will always look at the stars together like this.||Hey, you copied my exact wish! That means it's guaranteed to come true~",
            ),
            (
                "She turns in your arms on the hood of the car, her long twin-tails pooling across your lap.",
                "I'm ready to take our relationship to an even deeper, more intimate place with Aether.",
                "*traces her fingers lightly over your collar with a soft, alluring gaze*",
                "It's getting late, Aether... Next time we hang out at night, you don't have to drop me off at the door—stay over with me, okay?",
                "Promise to spend the whole night at her place next time||I'd love nothing more, Hu Tao. Next time, I'm staying with you all night.||*smiles seductively and kisses your jawline* I'll hold you to that promise, my love~",
                "Hold her close & kiss her hand under the stars||It's a date, Hu Tao.||Can't wait, Aether~",
            ),
        ),

        # ---------------- STAGE 4 (600 - 799 PTS): 4 SCENARIOS ----------------
        _build_3node_scenario_compact(
            "hutao_s4_sc1", 4, 1,
            "Midnight Cocoa & Loose Twin-Tails",
            "Stage 4 • Episode 1 • Late-Night Apartment",
            "Hu Tao's Candlelit Living Room",
            "/dating-media/hutao_cg10.jpg",
            "Spent a cozy, intimate evening at Hu Tao's apartment as she wore her off-shoulder crimson loungewear with her hair untied.",
            (
                "When Hu Tao opens her apartment door at midnight, her hat is gone, her long dark-brown-to-red hair flows loose over her bare shoulders, and she's wearing a soft crimson off-shoulder sweater.",
                "His eyes widened the second he saw my hair down and my bare shoulders... hehe, mission accomplished~",
                "*smiles flirtatiously in the warm fairy-light glow, holding two mugs of steaming cocoa*",
                "Welcome home, Aether~ I untied my hair and put on something much more comfortable tonight... Well? Do you like how your girlfriend looks after hours?",
                "Pull her close by the waist & kiss her bare shoulder||You look impossibly gorgeous with your hair down, Hu Tao. I couldn't take my eyes off you if I tried.||*gasps softly with a delighted shiver as your lips brush her shoulder* Mmm, Aether... careful, or I'll spill the hot cocoa before we even reach the couch~",
                "Brush a long strand of her loose hair behind her ear||Seeing your hair untied like this feels like a secret treasure meant just for me.||Because it IS meant only for you, my love~",
            ),
            (
                "On the plush sofa, she curls her legs up beside you, letting the off-shoulder sweater slip slightly as she leans into your side.",
                "Being held against Aether's chest on the couch feels so warm and intoxicating.",
                "*sets the mugs on the table and climbs halfway into your lap on the sofa*",
                "The cocoa was sweet, Aether, but sitting across from you is still too far away... Hold me closer?",
                "Wrap both arms around her waist & kiss her deeply on the couch||Come here, Hu Tao—there's zero distance between us tonight.||*wraps her arms around your neck and melts into the kiss, her heart racing* Mmm... your kisses are a hundred times sweeter than cocoa, Aether...",
                "Cuddle her tightly against your chest under the throw blanket||Right here in my arms is where you belong all night.||Best spot in the house~",
            ),
            (
                "Resting her flushed cheek against your collarbone, she traces little patterns over your chest with her fingertips.",
                "I never want him to leave tonight...",
                "*looks up at you through her lashes with glowing plum-blossom eyes*",
                "Don't even think about driving home tonight, Aether... The bedroom is right through that door, and I'm keeping you all to myself.",
                "Pick her up bridal-style & carry her toward the bedroom||I wasn't planning on going anywhere, my love—tonight belongs only to you.||*squeals happily and clings to your neck with a radiant blush* My handsome Traveler~",
                "Kiss her forehead & stay the night with her||I'm staying right by your side until morning, Hu Tao.||Hehe, good~",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s4_sc2", 4, 2,
            "Drying Her Hair After the Rain",
            "Stage 4 • Episode 2 • Bedroom After-Bath",
            "Warmly Lit Bedroom Suite",
            "/dating-media/hutao_cg11.jpg",
            "Dried Hu Tao's long damp hair on the bed after her bath while she wore a black silk camisole.",
            (
                "Stepping out of the bathroom in a cloud of fragrant plum-blossom steam, Hu Tao sits on the edge of the bed wearing a sleeveless black silk camisole with a white towel draped over her shoulders.",
                "My heart still flutters whenever Aether looks at me like this in the bedroom...",
                "*pats the mattress right behind her, her damp hair cascading down her back as she blushes*",
                "My hair takes forever to dry when it's untied, Aether... Come sit behind me on the bed and dry it for me?",
                "Sit right behind her on the bed & gently towel-dry her fragrant hair||Gladly, my love. Your hair smells like warm plum blossoms—let me take care of every strand for you.||*closes her eyes with a soft, contented sigh as your hands move through her hair* Mmm... your hands feel so gentle and warm, Aether...",
                "Brush her damp locks carefully & wrap the towel around her shoulders||Sit back and relax, Hu Tao—five-star hair spa from your boyfriend!||Hehe, I could get used to this every single night~",
            ),
            (
                "As her hair dries soft and silky, the towel slips down to her lap, leaving the nape of her neck and bare shoulders glowing in the bedside lamp light.",
                "If he kisses the back of my neck right now, I'm going to melt right into the sheets...",
                "*tilts her head slightly to the side, exposing the slender curve of her neck with a shy blush*",
                "Aether... my hair is almost dry, so why did your hands slow down? Are you distracted by something~?",
                "Lean forward & press a trail of warm kisses along the nape of her neck||Guilty—your bare neck and shoulders looked way too irresistible not to kiss, Hu Tao.||*shivers from head to toe, turning around in your lap to wrap her arms around your neck* A-Aether... when you kiss me there, all my teasing disappears...",
                "Hug her from behind & rest your chin on her shoulder||Just admiring how beautiful my girlfriend looks in the lamplight.||*leans her cheek back against yours lovingly* Only for you, Aether~",
            ),
            (
                "Turning in your arms on the soft mattress, she pulls you down beside her against the pillows.",
                "Wrapped in his arms in bed... I've never felt this loved.",
                "*tangles her fingers in your golden hair as she gazes up at you on the bed*",
                "Turn off the bedside lamp, Aether... Let's fall asleep holding each other tight tonight.",
                "Dim the lamp, pull the covers over both of you & kiss her goodnight||Goodnight, my sweet Hu Tao. Sweet dreams right here in my arms.||Goodnight, my love... hold me tight until sunrise~",
                "Hold her close against your chest as she drifts to sleep||I've got you all night, Hu Tao.||Mmm... love you, Aether...",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s4_sc3", 4, 3,
            "Crimson Dress on the Penthouse Balcony",
            "Stage 4 • Episode 3 • Moonlight Gala",
            "Starlight Penthouse Balcony",
            "/dating-media/hutao_cg12.jpg",
            "Shared a passionate moonlit slow dance and kiss with Hu Tao on the penthouse balcony in her crimson evening gown.",
            (
                "Out on the private penthouse balcony above the glittering skyline, Hu Tao waits for you in a form-fitting crimson-and-black evening dress accented with gold butterflies.",
                "I dressed up to the nines tonight so Aether wouldn't be able to look at anyone else in the whole city.",
                "*leans against the glass railing under the full moon and extends her hand invitingly*",
                "Step out onto the balcony with me, Aether... Tell me honestly: did my crimson evening dress steal your breath away tonight?",
                "Take her hand, pull her flush against you & tell her she's breathtaking||You stole my breath the second I walked into the room, Hu Tao. You look like an absolute goddess tonight.||*smiles enchantingly and hooks her finger into your collar* Good—because tonight, every single look and kiss belongs to me~",
                "Kiss her hand & admire the gold butterfly gown||That crimson gown was made for you, Hu Tao. Shall we dance under the moon?||I thought you'd never ask, my handsome escort~",
            ),
            (
                "Soft jazz drifts from inside the suite as you sway closely together on the moonlit balcony, your hand resting on the silk at her waist.",
                "His hand on my waist feels so warm through the thin silk...",
                "*rests her cheek against your chest as you slow-dance, then tilts her chin up toward you*",
                "Everyone inside the party wanted to talk to the famous Traveler... Aren't you glad I kidnapped you out onto this private balcony instead?",
                "Slide your hand along her back & tell her you only came for her||They could offer me the whole city and I'd still rather be out on this balcony holding you, Hu Tao.||*her plum-blossom eyes darken with passion as she pulls your face down to hers* Then prove it right now under the moonlight, Aether~",
                "Smile & spin her gently into a close embrace||Best kidnapping ever, Director. Let's stay out here all night.||Hehe, my thoughts exactly!",
            ),
            (
                "Under the silver moonlight, your lips meet in a deep, lingering kiss overlooking the sparkling city lights.",
                "My heart is completely, irrevocably his.",
                "*parts from the kiss breathless and flushed, resting her forehead against yours*",
                "Let's sneak out of the gala early, Aether... Take me home with you right now?",
                "Take her hand & whisk her straight to your car for a private night together||Your wish is my command, my love—let's go home right now.||*laces her fingers with yours with a thrilling, passionate smile* Drive fast, Aether~",
                "Escort her out of the gala arm-in-arm||Let's head back to our place where it's just the two of us.||Best part of the night starts now~",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s4_sc4", 4, 4,
            "Secret Key to Her Sanctuary",
            "Stage 4 • Episode 4 • Lovers' Promise",
            "Hu Tao's Private Courtyard",
            "/dating-media/hutao_cg10.jpg",
            "Received the spare key to Hu Tao's home bound with a crimson plum-blossom cord as a token of complete trust.",
            (
                "In the quiet of her private courtyard, Hu Tao holds out a small brass key tied with a braided crimson plum-blossom silk cord.",
                "Giving someone the key to my home and my private courtyard... Aether is the first and only one.",
                "*places the crimson-corded key gently into the palm of your hand*",
                "Here, Aether... This is the spare key to my home. That way, whether I'm writing poems at 2 AM or waiting with warm cocoa, you never have to knock.",
                "Close your fingers over the key & pull her into a tight, loving embrace||I'll treasure this key—and your heart—with everything I have, Hu Tao. Thank you for making me part of your home.||*hugs you back tightly, burying her face in your shoulder* Wherever you are is already my home, Aether.",
                "Attach the key to your keyring right in front of her||It's going right on my keyring permanently, Hu Tao.||Hehe, now you can come spoil me anytime!",
            ),
            (
                "She looks up from your embrace, her cheeks flushed and her expression unusually tender and serious.",
                "With Aether holding my key, we're ready for our final stage together—soulmates for eternity.",
                "*places both hands over your heart and gazes deeply into your eyes*",
                "You know what comes with accepting the 77th Director's key, right? It means you're stuck with my poems, my pranks, and my love for the rest of our lives!",
                "Kiss her lips & vow that you want every single day with her||Bring on all the poems, pranks, and love for eternity, Hu Tao—I wouldn't trade a single second with you for anything.||*beams with radiant tears of joy* Then let's step into forever together, my Traveler!",
                "Promise to always come home to her||Best lifetime contract in the universe, Hu Tao.||Signed and sealed with a kiss~",
            ),
            (
                "Hand in hand, you unlock her door together with your new key for the very first time.",
                "Our future together is going to be brighter than any star.",
                "*pulls you inside by the hand with a joyful, loving laugh*",
                "Come on inside, Aether—let's celebrate your new key properly tonight~",
                "Step inside & close the door behind the two of you||Tonight and every night after, I'm right here with you, my love.||Welcome home, Aether~",
                "Walk inside hand-in-hand with a warm smile||Home sweet home with my favorite girl.||Hehe, love you, Aether!",
            ),
        ),

        # ---------------- STAGE 5 (800 - 1000 PTS): 4 FINALE SCENARIOS ----------------
        _build_3node_scenario_compact(
            "hutao_s5_sc1", 5, 1,
            "Private Sunset Cove in Crimson Swimwear",
            "Stage 5 • Episode 1 • Spicy Sunset Beach Date",
            "Santa Maria Secret Sunset Cove",
            "/dating-media/hutao_cg13.jpg",
            "Shared an alluring, romantic sunset beach date with Hu Tao in her crimson-and-black halter swimsuit.",
            (
                "At a secluded golden sunset cove, Hu Tao unties her beach robe to reveal a stylish crimson-and-black halter swimsuit with a sheer white pareo wrap and a red plum-blossom hairpin.",
                "Look at Aether's face—he's completely spellbound! Picking out this crimson swimsuit was 1000% worth it~",
                "*steps barefoot into the warm golden surf and looks back over her shoulder with an alluring, teasing smile*",
                "Surprise, my love~ I picked out this crimson halter swimsuit exclusively for your eyes today. Well? Are you going to stand there staring, or come catch me in the waves?",
                "Catch her around the waist in the warm surf & kiss her sun-warmed shoulder||Staring was mandatory because you look dangerously sexy in that crimson swimsuit, Hu Tao—and now I've caught you.||*laughs breathlessly as you lift her slightly in the waves, wrapping her legs and arms around you* Oho~ Caught in five seconds flat! I love it when you look at me with those hungry eyes, Aether~",
                "Compliment her stunning figure & plum-blossom hairpin||That crimson swimsuit and plum-blossom hairpin look unbelievable on you, Hu Tao!||Hehe, private beach show just for my soulmate~",
            ),
            (
                "As the sun dips low on the horizon, painting the water in gold and crimson, you sit together on a plush beach towel in a secluded alcove.",
                "Pressed against Aether's warm skin after our swim... my heart is racing so fast.",
                "*sits sideways across your lap on the beach towel, tracing water droplets along your collarbone*",
                "Mmm, the ocean breeze is getting cooler, Aether... Good thing you're burning up like a furnace right underneath me~",
                "Wrap the warm towel around both of you & pull her into a passionate sunset kiss||When you sit in my lap wearing that swimsuit, Hu Tao, how could I not burn up for you?||*melts into the passionate kiss, her fingers tangling in your hair as the sunset waves crash softly* Aether... you drive me completely crazy...",
                "Hold her tight against your chest to keep her warm||Stay right here in my lap and I'll keep you warm all evening, my love.||Nowhere else I'd rather be~",
            ),
            (
                "Under the first twilight stars on the beach, she rests her forehead against yours, her cheeks glowing with happiness and desire.",
                "Every moment with Aether feels like paradise.",
                "*presses a soft kiss to the corner of your lips with a sultry wink*",
                "Let's head back to the suite, Aether... I brought one more special outfit for tonight that I haven't shown you yet~",
                "Carry her back to the car & tell her you can't wait for tonight||Another outfit just for tonight? Lead the way, my alluring Director—the night is still young.||*giggles against your neck* Just wait till you see the candlelit cheongsam I packed~",
                "Walk hand-in-hand along the shoreline back to the car||Best beach date ever, Hu Tao. Let's head back together!||Love you so much, Aether~",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s5_sc2", 5, 2,
            "Candlelit Silk Cheongsam & Butterfly Kiss",
            "Stage 5 • Episode 2 • Glamorous Candlelit Suite",
            "Candlelit Velvet Suite",
            "/dating-media/hutao_cg14.jpg",
            "Spent an enchanting candlelit night with Hu Tao in her black-and-crimson silk cheongsam embroidered with golden butterflies.",
            (
                "In a room lit only by dozens of warm scented candles, Hu Tao reclines gracefully on a velvet couch wearing a glamorous black-and-crimson silk cheongsam (qipao) with gold butterfly embroidery.",
                "Every breath I take in this candlelit room is for Aether alone.",
                "*rests her chin on her hand on the velvet couch, gazing at you with deep, smoldering crimson eyes*",
                "Come lock the door and sit beside me, Aether... Tonight, I wore this silk cheongsam embroidered with golden butterflies just for my soulmate.",
                "Kneel by the velvet couch, kiss her hand & trace the silk along her waist||You look like an absolute dream in the candlelight, Hu Tao. Every curve, every butterfly—you're perfection.||*shivers with pleasure at your touch, pulling you onto the velvet cushions beside her* Every butterfly on this silk—and the girl wearing it—belongs completely to you, Aether...",
                "Sit close beside her & admire the intricate gold butterfly cheongsam||The crimson and black silk under the candlelight is mesmerizing, Hu Tao.||I wanted tonight to be unforgettable for you, my love~",
            ),
            (
                "Candlelight flickers in her flower-shaped pupils as she straddles your lap on the velvet sofa, her hands resting softly on your cheeks.",
                "There's no mask, no distance, no hesitation left between us.",
                "*leans down so her lips hover a breath away from yours, her long hair framing both of your faces like a silk curtain*",
                "Listen to my heartbeat, Aether... Ever since Liyue, through every quest and every sunset in this city, it has only ever beaten this fast for you.",
                "Hold her hips firmly & claim her lips in a deep, breathless kiss||And my heart beats only for you, Hu Tao—now and for the rest of eternity.||*kisses you back with all the passion in her soul, a soft sigh escaping her lips* Aether... hold me closer, don't let go tonight...",
                "Embrace her tenderly & whisper how deeply you love her||I love every part of you, Hu Tao—my partner, my poet, my soulmate.||And I love you with all my soul, Aether~",
            ),
            (
                "As the candles burn low into the night, crimson spirit butterflies drift gently around the suite like falling petals.",
                "Waking up in his arms tomorrow morning is going to be heaven.",
                "*Blows out the last bedside candle and pulls you into the warm sheets*",
                "The candles are out, my dearest Traveler... Now the rest of the night belongs just to our whispers.",
                "Hold her in your arms through the entire night||Every whisper, every heartbeat, all night long, my love.||Forever yours, Aether~",
                "Kiss her tenderly under the covers||Sweetest night of our lives, Hu Tao.||I love you endlessly, Aether~",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s5_sc3", 5, 3,
            "Morning Sunlight in Aether's Shirt",
            "Stage 5 • Episode 3 • Sunlit Morning After",
            "Sunlit Master Bedroom",
            "/dating-media/hutao_cg15.jpg",
            "Woke up to warm morning sunlight with Hu Tao wearing your oversized white dress shirt and holding your hand to her cheek.",
            (
                "Warm morning sunlight streams through sheer white curtains across the bedsheets. You wake to find Hu Tao sitting beside you wearing your oversized white button-up shirt slipping off one shoulder.",
                "Watching Aether wake up in the morning sun... I could wake up to this sight for ten thousand years and never get tired of it.",
                "*holds your hand gently against her blushing cheek on the white bedsheets, her loose hair glowing in the sunlight*",
                "Good morning, sleepyhead~ I borrowed your white dress shirt while you were sleeping... It's a little big on me, but it smells just like you.",
                "Reach up to caress her cheek & pull her down into a warm morning embrace||Seeing you in my shirt in the morning sunlight is the most beautiful sight I've ever woken up to, Hu Tao.||*giggles happily as she tumbles into your chest on the warm sheets* Mmm, morning hugs with Aether are officially my new addiction~",
                "Kiss her palm & tell her she can keep the shirt forever||That shirt officially belongs to you now, my love—it looks a thousand times better on you.||Hehe, best morning gift ever!",
            ),
            (
                "Sunlight dances across the bed as she buttons one cuff of your oversized sleeve and leans over you with a radiant, tender smile.",
                "Even the simplest morning feels magical when we're together.",
                "*brushes her nose affectionately against yours in an Eskimo kiss*",
                "Hey, Aether... do we really have to get out of bed today? What if the 77th Director and the Traveler declare today an official 'Stay-in-Bed-Together Holiday'?",
                "Lock your arms around her waist & declare a full-day cuddle holiday||Motion unanimously approved, Director! Nobody's leaving this bed for at least another hour.||*laughs joyfully and kisses your lips* Best executive decision we've ever made!",
                "Offer to bring breakfast in bed so neither of you has to dress up||Stay right under the covers—I'll bring warm tea and sweet buns right back to bed for us!||You spoil me rotten, Aether, and I love every second of it~",
            ),
            (
                "Resting her head over your heartbeat in the sunlit bedroom, she intertwines all ten fingers with yours.",
                "My soul is completely at peace right here with Aether.",
                "*kisses the ring finger of your hand with a soft, devoted gaze*",
                "Whether it's a grand adventure or a quiet morning in your shirt... promise me every tomorrow will start just like this, Aether?",
                "Kiss her forehead & promise her every single tomorrow||Every morning, every sunset, and every tomorrow belongs to us, Hu Tao. I promise.||*smiles with pure, eternal bliss* I love you, my Traveler, my soulmate.",
                "Squeeze her hand tightly & vow to stay by her side||Every single tomorrow, Hu Tao.||Forever and ever, Aether~",
            ),
        ),
        _build_3node_scenario_compact(
            "hutao_s5_sc4", 5, 4,
            "Beyond Life and Death: Eternal Star-Promise",
            "Stage 5 • Episode 4 • Grand Finale Vow (1000/1000)",
            "Starlit Plum Blossom Summit",
            "/dating-media/hutao_cg15.jpg",
            "Exchanged eternal soulmate vows with Hu Tao beneath the blooming plum blossoms and shooting stars.",
            (
                "Beneath a canopy of blooming red plum blossoms and a sky full of shooting stars, Hu Tao stands before you holding a pair of intertwined crimson-and-gold rings.",
                "In Liyue, we say butterflies guide souls across the border... and mine guided me straight to Aether for eternity.",
                "*holds out the intertwined crimson-and-gold rings as dozens of glowing spirit butterflies form a halo around the two of you*",
                "Aether... We've walked through the border of life and death, shared countless poems, and built a home together here. Tonight, I want to make a vow that transcends every world.",
                "Slide the crimson-and-gold ring onto her finger & pledge your eternal love||With this ring, Hu Tao, my heart, my journey, and my eternity belong to you across every world we ever walk.||*tears of pure happiness shimmer in her flower-shaped pupils as she slides the matching ring onto your finger* And in this life and every life beyond, the 77th Director—your Hu Tao—is yours forever!",
                "Take both her hands & recite a vow of eternal devotion||Through every star and every season, I'll never let go of your hand, Hu Tao.||Best vow in the cosmos, my beloved Aether!",
            ),
            (
                "As the rings gleam on your fingers, Hu Tao recites her final, most heartfelt couplet just for you.",
                "This poem has been in my heart since the very first day we met.",
                "*places her ringed hand over your cheek, her voice soft and trembling with love*",
                "'Plum blossoms bloom where the golden starlight falls; across life and death, it's Aether my heart calls.'",
                "Pull your soulmate into a timeless, passionate kiss beneath the falling petals||That's the masterpiece of our lifetime, Hu Tao—and we'll keep writing new verses together forever.||*wraps her arms tightly around your neck, kissing you deeply as plum petals and spirit butterflies swirl around you*",
                "Hold her close against your heart as the stars shine above||I love you more than words or poems can ever say, Hu Tao.||And I love you beyond infinity, Aether!",
            ),
            (
                "Hand in hand, your rings catching the starlight, Hu Tao beams up at you with the brightest smile in Teyvat and San Andreas.",
                "Stage 5 Soulmate complete—1000/1000 Eternal Star-Promise!",
                "*rests her head against your shoulder, her fingers locked with yours forever*",
                "So, my eternal husband-to-be... where shall we drive next? Wherever the road goes, I'm riding in your passenger seat forever~",
                "Kiss her hand & start the engine for your endless journey together||Anywhere you want to go, my love—the passenger seat is yours for eternity.||Hehe, step on the gas, Aether! To forever and beyond~!",
                "Smile & set off into the starlit night together||Let's go, Hu Tao—our best chapters are just beginning!||Yay! Forever with Aether!",
            ),
        ),
    ]
)


def _build_extra_cameo_scenario_compact(
    sc_id: str,
    stage: int,
    order: int,
    title: str,
    subtitle: str,
    location: str,
    cg_url: str,
    summary_l2: str,
    cameo_cast: list[str],
    cameo_dynamic_tier: str,
    n1: tuple[str, str, str, str, str, str],
    n2: tuple[str, str, str, str, str, str],
    n3: tuple[str, str, str, str, str, str],
) -> dict[str, Any]:
    sc_obj = _build_3node_scenario_compact(sc_id, stage, order, title, subtitle, location, cg_url, summary_l2, n1, n2, n3)
    sc_obj["is_extra_cameo"] = True
    sc_obj["cameo_cast"] = cameo_cast
    sc_obj["cameo_dynamic_tier"] = cameo_dynamic_tier
    sc_obj["allow_custom_input"] = True
    return sc_obj


# Ensure all 20 Core Scenarios also explicitly declare allow_custom_input & cameo metadata
for _core_sc in HUTAO_20_VN_SCENARIOS:
    _core_sc["is_extra_cameo"] = False
    _core_sc["cameo_cast"] = []
    _core_sc["cameo_dynamic_tier"] = f"Stage {_core_sc['stage']} Core Romance Scenario (Hu Tao & Traveler Aether)"
    _core_sc["allow_custom_input"] = True


# ==============================================================================
# 4B. 10 EXTRA GENSHIN CAMEO & DAILY-LIFE SCENARIOS FOR HU TAO (40 UNIQUE CGS)
#     - Stage-Responsive Cameo Reactions (Stage 1 Buddy Chaos -> Stage 3 Teasing
#       Sparks -> Stage 4 Caught Red-Handed on a Date -> Stage 5 Public Blessing!)
#     - Built EXTRA on top of the 20 Core Scenarios (Total = 30 Scenarios, 120 CGs)
# ==============================================================================
HUTAO_10_EXTRA_CAMEO_SCENARIOS: list[dict[str, Any]] = [
    # ---------------- STAGE 1 EXTRA CAMEOS (2 SCENARIOS • ORDER 5 & 6) ----------------
    _build_extra_cameo_scenario_compact(
        "hutao_s1_ex1", 1, 5,
        "Wanmin Kitchen Chaos with Xiangling, Xingqiu & Chongyun",
        "Stage 1 • Extra Cameo 1 • Liyue Squad Dinner",
        "Wanmin Restaurant Street Terrace",
        "/dating-media/hutao_s1_ex1_cg1.jpg",
        "Shared a lively Wanmin Restaurant dinner with Hu Tao, Xiangling, Guoba, Xingqiu, and Chongyun, catching Hu Tao's wrist before she spiced Chongyun's noodles.",
        ["Xiangling", "Xingqiu", "Chongyun", "Guoba"],
        "Stage 1 Squad Dynamic: Friends treat Hu Tao & Aether as lively partners-in-crime at the dinner table.",
        (
            "Warm lantern light spills across Wanmin Restaurant's outdoor terrace as you and Hu Tao arrive. Xiangling waves her ladle excitedly beside Guoba, while Xingqiu looks up from his book and Chongyun nibbles a blue popsicle at the round table.",
            "🦋 Butterfly Spirit: Hehe, the whole Liyue gang is here—and Aether walked in right beside me!",
            "*waves her porkpie hat toward the table and pulls out the wooden chair right next to hers for Aether*",
            "Aiya, look who's starving! Chef Xiangling, two seats for the 77th Director and her VIP guest Aether! Wait—Chongyun, why are you eating an ice popsicle before the appetizers even arrive?",
            "Greet Xiangling, Xingqiu & Chongyun warmly & sit right beside Hu Tao||Good evening everyone! Don't worry, Chongyun—I'll keep an eye on Hu Tao's chopsticks tonight so your bowl stays ice-cold.||*laughs brightly as Xingqiu chuckles and Chongyun breathes a sigh of relief* Oho, Aether's already taking their side?! Traitor~!",
            "Ask Xiangling what special dish she and Guoba are testing tonight||Smells amazing, Xiangling! What's on the Wanmin secret menu for our group tonight?||Xiangling beams while Hu Tao grins: 'Just wait till you taste the Golden Shrimp Balls!'",
        ),
        (
            "Halfway through the appetizers, Hu Tao's crimson eyes glint with mischief as she secretly pinches a glowing red Jueyun Chili behind the teapot, aiming straight for Chongyun's mild broth while Xingqiu hides an amused smirk behind his novel.",
            "🦋 Butterfly Spirit: Just one tiny chili flake... unless Aether catches me red-handed!",
            "*leans across the lantern-lit table on tiptoe, poised to drop the fiery Jueyun Chili into Chongyun's bowl*",
            "Shh, Aether, don't say a word—Chongyun looks a little too chilly tonight, so the Director is donating some Pyro energy to his soup!",
            "Gently catch Hu Tao's wrist with a warm laugh & redirect the chili into your own bowl||Caught you red-handed, Director! Put that Jueyun Chili in my bowl instead—if Chongyun's yang energy flares up, Wanmin Restaurant won't survive the night!||*blinks in surprise as you hold her wrist, then giggles happily while Chongyun thanks you profusely* Hehe, saving Chongyun AND volunteering to eat my spicy pick? You really are a hero, Aether!",
            "Tip off Chongyun playfully so he guards his bowl in time||Chongyun, incoming Pyro attack at twelve o'clock!||*pouts playfully as Chongyun shields his bowl* Aiya, Aether! You ruined my masterpiece prank!",
        ),
        (
            "On the counter, Guoba and Boo Tao happily split a golden Mora Meat pastry while Xiangling serves a steaming platter of crystal shrimp and stir-fry. Everyone raises their teacups for a group toast under the glowing Liyue lanterns.",
            "🦋 Butterfly Spirit: Even with all my friends around, sitting shoulder-to-shoulder with Aether is the best part of tonight.",
            "*clinks her porcelain teacup against yours first before toasting Xiangling, Xingqiu, and Chongyun*",
            "Even Guoba and Boo Tao are best buddies now! Come on, Aether, raise your cup—what are we toasting to tonight?",
            "Toast to Hu Tao's infectious energy & many more nights with the Liyue squad||To Chef Xiangling's feast, to old friends from Liyue, and to the 77th Director who makes every night an adventure!||*beams with sparkling flower-shaped pupils as everyone cheers and clinks cups* Hear, hear! Best toast of the night—drink up, everyone!",
            "Toast to good food and great company at Wanmin Restaurant||To the best crew and the best food in town—cheers, everyone!||Cheers! Guoba and Boo Tao approve 100%!",
        ),
    ),
    _build_extra_cameo_scenario_compact(
        "hutao_s1_ex2", 1, 6,
        "Consultant Zhongli's Unbelievable Receipt",
        "Stage 1 • Extra Cameo 2 • Wangsheng Workplace",
        "Wangsheng Funeral Parlor Ginkgo Courtyard",
        "/dating-media/hutao_s1_ex2_cg1.jpg",
        "Audited Consultant Zhongli's astronomical tea-and-jade receipt with Hu Tao at Wangsheng Funeral Parlor and shared sunset Osmanthus tea.",
        ["Zhongli"],
        "Stage 1 Workplace Dynamic: Zhongli calmly charges antique luxuries to the Parlor while observing how much Hu Tao brightens around Aether.",
        (
            "Under the golden ginkgo trees of Wangsheng Funeral Parlor's courtyard, Consultant Zhongli sits serenely sipping Osmanthus tea. Beside him, Hu Tao holds an expense scroll so long it trails across the flagstones, her jaw dropped in comical disbelief as you walk in.",
            "🦋 Butterfly Spirit: Aether's here! Finally, someone who understands the pain of paying Zhongli's bills!",
            "*waves the three-meter paper receipt dramatically as Zhongli takes another calm sip of tea*",
            "Aether!! Thank the stars you're here! Look at this invoice Consultant Zhongli just handed me—'Eighteen antique noctilucous jade incense burners AND a vintage Sung-dynasty tea set, billed to Wangsheng Parlor'?! Tell him we're a funeral parlor, not the Golden House!",
            "Chuckle at Zhongli's classic Mora-less habit & offer to help Hu Tao audit the list||Classic Zhongli—still forgetting to check the price tag before saying 'put it on Wangsheng's tab.' Hand me half the scroll, Hu Tao, let's see which items we can return!||*hands you half the scroll with shining eyes while Zhongli nods approvingly* See, Mr. Zhongli?! Even the Traveler agrees! You're officially hired as my Chief Mora Protector, Aether!",
            "Ask Zhongli why the Parlor needed eighteen jade incense burners at once||Eighteen burners, Zhongli? Even for an adepti ceremony, isn't that a bit steep for Hu Tao's budget?||Zhongli replies calmly: 'Quality rituals require proper vessels, Traveler'—making Hu Tao groan playfully!",
        ),
        (
            "Inside the parlor's wooden study, Hu Tao pins a crimson 'Honorary Auditor' rosette onto your lapel and hands you a brass abacus, while Zhongli examines a jade burner by the window.",
            "🦋 Butterfly Spirit: Working side by side with Aether at my desk makes boring ledger work ten times more fun!",
            "*adjusts the crimson ribbon on your chest and leans over the ledger book beside you*",
            "With this Honorary Auditor badge, you have full authority to veto any of Mr. Zhongli's impulse buys! So, Auditor Aether—how should we balance the books this month?",
            "Negotiate a 50% return with the antique merchant & save enough Mora for Hu Tao's snack fund||Let's keep the two finest jade burners for the Parlor, return the other sixteen at no loss, and put the saved Mora straight into the Director's late-night snack fund.||*gasps and clasps her hands together in pure joy* Genius!! You balanced the Parlor's budget AND funded our snack outings in one move!",
            "Check each line item carefully alongside Hu Tao||Let's go line by line together, Director—two heads are better than one.||Hehe, with you next to me, these numbers actually make sense!",
        ),
        (
            "Pausing by the carved wooden doorway as sunset gilds the courtyard, Zhongli watches the two of you laughing over the balanced ledgers with a subtle, knowing smile before pouring three fresh cups of Osmanthus tea.",
            "🦋 Butterfly Spirit: Why is Mr. Zhongli smiling like that? Does he notice how happy I am when Aether's here?",
            "*flashes a cheeky peace sign toward you behind Zhongli's back as you both step out to the stone tea table*",
            "Mr. Zhongli just said, 'The Director's laughter has been remarkably warm ever since the Traveler arrived.' Hehe—come drink your Osmanthus tea before I blush, Aether!",
            "Raise your teacup to both Zhongli and Hu Tao with a warm smile||Then I'll make sure to visit Wangsheng Parlor often, Mr. Zhongli—keeping the 77th Director smiling is a contract I'll happily uphold.||*Zhongli nods with a warm amber gaze while Hu Tao's cheeks turn rosy* Oho, invoking a contract in front of Mr. Zhongli? Now you really can't take it back, Aether~!",
            "Enjoy the fragrant sunset tea with Hu Tao and Zhongli||Nothing beats peaceful sunset tea in the courtyard after saving the Parlor's budget.||Best way to end the shift, Auditor Aether!",
        ),
    ),

    # ---------------- STAGE 2 EXTRA CAMEOS (2 SCENARIOS • ORDER 5 & 6) ----------------
    _build_extra_cameo_scenario_compact(
        "hutao_s2_ex1", 2, 5,
        "Heyu Tea House Opera Night with Yun Jin",
        "Stage 2 • Extra Cameo 1 • Liyue Opera & Duet",
        "Heyu Tea House VIP Balcony",
        "/dating-media/hutao_s2_ex1_cg1.jpg",
        "Attended Yun Jin's opera performance at Heyu Tea House with Hu Tao and improvised a backstage poetic duet that delighted Yun Jin.",
        ["Yun Jin"],
        "Stage 2 Confidant Dynamic: Yun Jin notices how effortlessly Aether and Hu Tao harmonize in verse and conversation.",
        (
            "Red silk lanterns glow above Heyu Tea House's wooden stage as Opera Director Yun Jin performs a breathtaking fan dance in her purple-and-pink headdress. At the front-row VIP balcony table, Hu Tao taps her fingers softly to the percussion beside you.",
            "🦋 Butterfly Spirit: Yun Jin's voice is incredible tonight—and sitting up here with Aether feels like a real theater date!",
            "*leans close to whisper near your ear so she doesn't disturb the opera aria*",
            "Look at Yun Jin's footwork, Aether! She wrote this new act last week. Are you enjoying our front-row VIP seats?",
            "Whisper back that the opera is wonderful, especially sharing the VIP balcony with her||Yun Jin's performance is mesmerizing, Hu Tao—and sharing this front-row balcony tea table with you makes the night unforgettable.||*smiles warmly under the lantern glow and pours more jasmine tea into your cup* Hehe, wait until after the curtain call—I got us backstage passes to say hi to her!",
            "Applaud Yun Jin's high note enthusiastically alongside Hu Tao||Bravo! Her new aria is fantastic—thanks for inviting me tonight, Hu Tao.||Of course! Who else would appreciate good art and good tea with me?",
        ),
        (
            "After the curtain call, you and Hu Tao visit Yun Jin in the backstage lounge, presenting a bouquet of glowing blue Glaze Lilies as Yun Jin welcomes you both over porcelain teacups.",
            "🦋 Butterfly Spirit: Yun Jin is looking at the two of us with that 'I see how close you two are' smile!",
            "*hands Yun Jin the Glaze Lilies while standing close beside your shoulder*",
            "Yun Jin! Aether and I brought fresh Glaze Lilies for your dressing room! Tell the truth—didn't you see us cheering the loudest from the balcony?",
            "Compliment Yun Jin's performance & mention how Hu Tao hummed along to every beat||Your performance was brilliant, Yun Jin. Hu Tao knew every rhythm by heart—she was humming harmony beside me the entire final act.||*Yun Jin smiles gracefully: 'It is rare to see Hu Tao share her favorite box seats, Aether—she must hold your company in very high esteem!' causing Hu Tao to blush*",
            "Congratulate Yun Jin on a sold-out evening at Heyu Tea House||Congratulations on a wonderful show, Yun Jin! The whole tea house was captivated.||Yun Jin bows with a warm smile while Hu Tao beams proudly beside you!",
        ),
        (
            "Inspired by the music, Hu Tao starts an impromptu poetic couplet in the lounge—and when you complete her second line without missing a beat, Yun Jin claps her hands in genuine delight before waving you both off onto the moonlit balcony.",
            "🦋 Butterfly Spirit: Even Yun Jin said Aether and I sound like two halves of the same melody!",
            "*steps out onto the moonlit wooden balcony beside you, humming Yun Jin's melody with a soft blush*",
            "Did you hear Yun Jin backstage, Aether? She said our duet rhythm was so natural we could headline a romance opera together! What do you think about that, my co-star?",
            "Smile & tell her you'd gladly be her leading partner on or off the stage||If the story is about the 77th Director and her Traveler, I'll gladly play your leading partner in every act, Hu Tao.||*her crimson eyes shimmer under the moonlight as she bumps her shoulder affectionately against yours* Careful, Aether—my operas have a hundred acts, and I don't allow understudies~!",
            "Hum the rest of the melody together as you walk down the lantern stairs||We definitely make a great duet team, Hu Tao. Let's keep practicing our verses!||Deal! Next verse is on the walk home!",
        ),
    ),
    _build_extra_cameo_scenario_compact(
        "hutao_s2_ex2", 2, 6,
        "Harbor Patrol Bump-In with Keqing & Ganyu",
        "Stage 2 • Extra Cameo 2 • Night Market Encounter",
        "Liyue Harbor Night Market Archway",
        "/dating-media/hutao_s2_ex2_cg1.jpg",
        "Bumped into Keqing and sleepy Ganyu during a night market stroll with Hu Tao while carrying all her festival bags.",
        ["Keqing", "Ganyu"],
        "Stage 2 Harbor Dynamic: Keqing & Ganyu notice Aether spoiling Hu Tao and carrying all her night-market bags.",
        (
            "As you stroll through the bustling night market carrying four paper bags of Hu Tao's lantern trinkets and snacks, you turn the corner under the red archway and bump right into Yuheng Keqing and Ganyu on an evening inspection.",
            "🦋 Butterfly Spirit: Oho! It's Keqing and Ganyu—and Aether is holding all my shopping bags like a total gentleman!",
            "*tips her hat cheerfully while holding a candied hawthorn skewer*",
            "Well, well! Look who's working overtime at the night market—Lady Keqing and Miss Ganyu! Taking a break from the Yuehai Pavilion paperwork?",
            "Greet Keqing & Ganyu politely while shifting Hu Tao's shopping bags onto one arm||Good evening, Keqing, Ganyu! Hu Tao and I were just sampling every stall on the street—though she's the chief taster and I'm the logistics department tonight.||*Keqing's eyes flick amusingly to the four Hu Tao shopping bags on your arm as Hu Tao giggles* Hehe, best logistics officer in Teyvat!",
            "Ask how their evening harbor inspection is going||Working late again, you two? Hope the harbor inspection is going smoothly tonight!||Keqing nods briskly while Ganyu rubs her sleepy eyes with a soft smile.",
        ),
        (
            "Halfway through Ganyu's report on lantern permits, Ganyu's eyelids droop and she nods off standing up—her stack of scroll ledgers tipping forward until you deftly catch them with your free hand while Hu Tao pops a fresh Qingxin flower pastry into Ganyu's hand.",
            "🦋 Butterfly Spirit: Aether's reflexes are so gentle—and look how grateful Ganyu is!",
            "*hands sleepy Ganyu a fragrant white Qingxin petal pastry with a warm wink*",
            "Whoa there, Miss Ganyu! Good thing Aether caught your scrolls! Here, eat this fresh Qingxin flower cake Aether and I just bought—it'll wake your Qilin horns right up!",
            "Steady Ganyu's scrolls & suggest she and Keqing take a five-minute tea break||Here are your scrolls, Ganyu—safe and sound. Even Qixing secretaries need a breather; take Hu Tao's Qingxin pastry and rest your eyes for a minute.||*Ganyu blushes gratefully: 'T-Thank you both so much, Aether, Hu Tao...' while Hu Tao beams proudly at your kindness*",
            "Hand the neatly stacked scrolls back to Ganyu with a gentle smile||Careful there, Ganyu! Glad we bumped into you before those scrolls hit the cobblestones.||Hu Tao grins: 'Teamwork between the Director and the Traveler saves the day again!'",
        ),
        (
            "With Ganyu refreshed, Keqing crosses her arms and looks between you and Hu Tao with a perceptive, teasing smirk—pointing out that the famous Traveler has been happily carrying all of Hu Tao's ribbons, pastries, and lantern bags the entire evening.",
            "🦋 Butterfly Spirit: W-Why is Keqing looking at us like that?! Now my cheeks are getting hot!",
            "*puffs her cheeks in an adorable, flustered pout before looping her fingers around your wrist as Keqing and Ganyu wave goodnight*",
            "H-Hey! Lady Keqing didn't have to tease me like that! 'It seems the Traveler spoils Director Hu quite thoroughly'—hmph! Come on, Aether, let's head down to the waterfront!",
            "Laugh softly, let her hold your wrist & admit that Keqing was 100% right||Keqing wasn't wrong, though—I actually love spoiling you and carrying your bags when we're out together, Hu Tao.||*freezes for a second with her cheeks glowing crimson under the lanterns, then tightens her fingers around your wrist* A-Aiya... when you admit it that honestly, how am I supposed to make a witty comeback?!",
            "Walk alongside her toward the harbor lights with a warm grin||Let Keqing tease all she wants—more snacks for the two of us by the water!||Hehe, that's the spirit, Aether!",
        ),
    ),

    # ---------------- STAGE 3 EXTRA CAMEOS (2 SCENARIOS • ORDER 5 & 6) ----------------
    _build_extra_cameo_scenario_compact(
        "hutao_s3_ex1", 3, 5,
        "Poetry & Popsicles: Xingqiu and Chongyun Spot the Sparks",
        "Stage 3 • Extra Cameo 1 • Friends Notice the Romance",
        "Wanwen Bookhouse Open-Air Terrace",
        "/dating-media/hutao_s3_ex1_cg1.jpg",
        "Composed poetry with Hu Tao on Wanwen Bookhouse terrace while Xingqiu and Chongyun noticed your romantic closeness and played wingmen.",
        ["Xingqiu", "Chongyun"],
        "Stage 3 Unspoken Tension Dynamic: Xingqiu & Chongyun immediately notice Hu Tao leaning on Aether and tease their disguised love poems.",
        (
            "Afternoon sunlight bathes the open-air terrace of Wanwen Bookhouse. You and Hu Tao sit side by side on a single wooden bench across from Xingqiu and Chongyun, with inkstones and poetry scrolls spread across the table.",
            "🦋 Butterfly Spirit: Sitting this close to Aether on one bench... our shoulders haven't stopped touching since we sat down!",
            "*slides her poetry scroll closer to yours so your elbows brush on the tabletop*",
            "All right, gentlemen of Liyue! Today's poetry theme is 'Hidden Feelings Under the Autumn Moon.' Aether and I are on the same team, naturally!",
            "Smile & move closer on the bench so she has plenty of room to write||Partners as always, Hu Tao. Let's write a couplet so good even Xingqiu won't have a critique.||*beams and leans in closer to your side, while across the table Xingqiu raises a knowing eyebrow*",
            "Accept the poetry challenge alongside Hu Tao||You start the first line, Director, and I'll match your rhyme!||Hehe, nobody matches my rhythm like you, Aether!",
        ),
        (
            "As you brush your reply line onto the scroll, Hu Tao unconsciously rests her chin and temple right against your shoulder to read your handwriting—causing Xingqiu to nudge Chongyun's elbow and point subtly with his folding fan.",
            "🦋 Butterfly Spirit: His shoulder is so warm and comfortable... wait, why is Chongyun turning bright red across the table?!",
            "*stays nestled against your shoulder while reading your calligraphy, before glancing up at a flustered Chongyun*",
            "Hmm? Xingqiu, Chongyun—why are you two whispering over there instead of writing your stanza? Did Aether's calligraphy leave you speechless?",
            "Keep your shoulder steady for Hu Tao to lean on & read your romantic verse aloud||'Where the butterfly rests, the golden star stays near.' What do you think, Xingqiu—does our verse capture the theme?||*Chongyun nearly drops his blue popsicle in shock while Xingqiu grins: 'Oh, it captures your feelings with blinding clarity, Aether!' making Hu Tao blush scarlet*",
            "Tease Xingqiu back about his own messy handwriting||We're just collaborating closely, Xingqiu—let's see what you two wrote!||Xingqiu chuckles: 'Far be it from me to interrupt such... close poetic collaboration!'",
        ),
        (
            "As golden sunset paints the bookhouse rooftop, Xingqiu smoothly packs his books and pulls a blushing Chongyun toward the stairs with a wingman wink—leaving you and Hu Tao completely alone at the terrace railing.",
            "🦋 Butterfly Spirit: They totally left on purpose to give Aether and me sunset privacy... and my heart is pounding!",
            "*stands beside you at the sunset railing, her pinky finger shyly hooking around yours*",
            "Those two weren't subtle at all, were they? 'We suddenly remembered an urgent exorcism—enjoy the sunset, lovebirds!' ...Hey, Aether, since they already called us that... can we hold hands for real while we watch the sun go down?",
            "Intertwine your fingers fully with hers & pull her gently against your side||I don't need an excuse from Xingqiu to hold your hand, Hu Tao. I've been wanting to hold you like this all afternoon.||*her fingers tighten warmly around yours as she rests her blushing cheek against your arm* Mmm... best poetry club meeting in history, Aether~",
            "Hold her hand warmly as you watch the golden harbor sunset||Best wingmen in Liyue. Let's enjoy the sunset together, Hu Tao.||Hehe, I owe Xingqiu a rare book for this~",
        ),
    ),
    _build_extra_cameo_scenario_compact(
        "hutao_s3_ex2", 3, 6,
        "Cross-Border Festival Trip: Venti & Yoimiya's Couple Sparklers",
        "Stage 3 • Extra Cameo 2 • Out-of-Town Festival",
        "Inazuma-Mondstadt Cross-Cultural Festival Pier",
        "/dating-media/hutao_s3_ex2_cg1.jpg",
        "Traveled with Hu Tao to the cross-border festival pier, where Yoimiya gave you Couple Sparklers and Venti sang a teasing romantic ballad.",
        ["Yoimiya", "Venti"],
        "Stage 3 Cross-Region Trip Dynamic: Out-of-town friends Yoimiya & Venti immediately mistake/tease Hu Tao and Aether as sweethearts on a getaway.",
        (
            "Paper lanterns and windwheel asters line the waterfront pier as you and Hu Tao arrive on an out-of-town festival trip. Ahead by the fireworks booth, Yoimiya waves a bundle of sparklers excitedly while Venti strums his wooden lyre in a green bard cape.",
            "🦋 Butterfly Spirit: Traveling out of town with Aether feels like a secret vacation—and look, it's Yoimiya and Venti!",
            "*holds onto the sleeve of your tunic so she doesn't lose you in the festive crowd*",
            "Oho! Look who's at the festival pier, Aether—Miss Yoimiya from Naganohara Fireworks and our favorite tone-deaf bard Venti! Come on, let's go say hi!",
            "Keep Hu Tao close beside you through the crowd & greet Yoimiya and Venti||Careful with the crowd, Hu Tao—stay right beside me. Hey Yoimiya, hey Venti! We came all the way out here to see tonight's fireworks!||*Yoimiya beams at your closeness: 'Aether! Hu Tao! You two traveled all the way here together for a festival date?! How romantic!'*",
            "Wave to Yoimiya & Venti as you walk up to the fireworks booth||Great to see you both! Looks like the festival pier is in full swing tonight!||Venti tips his green beret with a knowing grin: 'Ehe~ Look who arrived hand-in-sleeve!'",
        ),
        (
            "Before Hu Tao can explain, Yoimiya grins from ear to ear and presses a special gold-ribboned pack of 'Naganohara Destiny Couple Sparklers' into your hands, while Venti plucks a romantic chord on his lyre.",
            "🦋 Butterfly Spirit: 'Destiny Couple Sparklers'?! Yoimiya says when two people light them together, their hearts stay bound!",
            "*blushes rose-pink as she holds her half of the heart-tipped sparklers beside yours*",
            "W-Wait a second, Yoimiya! Why does the label say 'Strictly for Sweethearts Who Traveled Together'?! And Venti—stop grinning like that with your lyre!",
            "Touch the tip of your sparkler to Hu Tao's to light them together with a warm smile||Thank you, Yoimiya—we'll gladly test the 'Sweethearts Special.' Come on, Hu Tao, touch your sparkler to mine so we can light them together.||*as the two sparklers ignite in a shower of golden heart-sparks, Hu Tao's eyes shine with a flustered, happy glow*",
            "Thank Yoimiya for the special sparklers & light them with Hu Tao||You always make the best fireworks, Yoimiya! Ready to light them, Hu Tao?||Hehe, they really do sparkle like little golden butterflies!",
        ),
        (
            "Venti winks mischievously and sings an improvised ballad about 'the Butterfly Director who lost her heart to her Golden Traveler,' before Yoimiya's grand fireworks burst across the night sky above the harbor.",
            "🦋 Butterfly Spirit: Venti's song hit the bullseye... my heart really does belong to Aether.",
            "*stands shoulder-to-shoulder with you under the booming golden fireworks, holding her glowing couple sparkler right next to yours*",
            "That cheeky bard... singing 'Across the border and across the sea, the Director only has eyes for thee' in front of everyone! ...Though between you and me under these fireworks, Aether... Venti didn't get a single lyric wrong.",
            "Wrap your free arm around her shoulders & watch the fireworks together||Then let Venti sing it to the whole world, Hu Tao—because under these fireworks, I only have eyes for you too.||*leans her head warmly into the crook of your shoulder as golden fireworks reflect in her flower-shaped pupils* Best out-of-town trip ever, Aether...",
            "Hold your sparkler close to hers so the sparks dance together||Venti's best ballad yet! I'm really glad we took this trip together, Hu Tao.||Me too, Aether—let's travel everywhere together next time!",
        ),
    ),

    # ---------------- STAGE 4 EXTRA CAMEOS (2 SCENARIOS • ORDER 5 & 6) ----------------
    _build_extra_cameo_scenario_compact(
        "hutao_s4_ex1", 4, 5,
        "Caught Hand-in-Hand at Wanmin by Xiangling & Guoba!",
        "Stage 4 • Extra Cameo 1 • Caught on a Secret Date!",
        "Wanmin Restaurant Late-Night Corner Booth",
        "/dating-media/hutao_s4_ex1_cg1.jpg",
        "Got caught red-handed by Xiangling and Guoba while holding hands and feeding each other on a late-night couple date at Wanmin Restaurant.",
        ["Xiangling", "Guoba"],
        "Stage 4 Lovers Dynamic: Xiangling & Guoba accidentally walk in on Hu Tao and Aether feeding each other as an official couple!",
        (
            "Late at night after the main dinner rush, you and Hu Tao share a tucked-away corner booth at Wanmin Restaurant. Sitting on the same wooden bench as lovers, Hu Tao laces her fingers warmly through yours on the tabletop.",
            "🦋 Butterfly Spirit: Sitting on the same side of the booth holding Aether's hand... I love being his girlfriend so much!",
            "*squeezes your hand affectionately on the table and leans her cheek against your shoulder*",
            "Hehe, sneaking into Wanmin after hours for a secret couple dinner feels so thrilling, doesn't it? Xiangling is busy in the back kitchen—nobody knows we're officially dating yet!",
            "Kiss the back of her hand & tell her you love every secret and public moment with her||Whether it's a secret booth or the middle of the boulevard, sitting this close to my girlfriend is the best part of my night, Hu Tao.||*giggles softly with a loving blush and picks up her chopsticks* Then as your girlfriend, it's my duty to spoil you with the first bite~!",
            "Hold her hand warmly & enjoy the cozy lantern-lit booth together||Having this cozy corner all to ourselves is perfect, my love.||Right?! Just you, me, and a basket of golden shrimp dumplings!",
        ),
        (
            "Picking up a golden crystal shrimp dumpling with her chopsticks, Hu Tao leans in close with a sweet blush and holds it to your lips—when suddenly the bamboo kitchen curtain parts and Xiangling and Guoba pop their heads out, freezing with wide, sparkling eyes and silent gasps!",
            "🦋 Butterfly Spirit: AHHH!! Xiangling and Guoba just caught me feeding Aether while holding his hand!!",
            "*freezes mid-bite with her chopsticks at your lips as Xiangling gasps: 'H-HU TAO?! AETHER?! You two are holding hands and saying Ahh~?!'*",
            "W-Wah!! Xiangling?! Guoba?! How long were you two standing behind that bamboo curtain?! A-Aether, our cover is completely blown!",
            "Take the bite from Hu Tao's chopsticks anyway, wrap your arm around her waist & announce you're together||*takes the dumpling bite with a smile* Delicious! No need to hide anymore, Xiangling—Hu Tao and I are officially together.||*Xiangling squeals with joy while Guoba claps his paws, and Hu Tao's face turns the happiest shade of crimson* A-Aether!! You said that so smoothly—my heart is melting!",
            "Smile warmly at Xiangling & admit she caught the two of you on a couple date||Looks like Chef Xiangling caught us red-handed on our late-night date, Hu Tao!||Hu Tao blushes and laughs: 'Busted by my best friend and a panda!'",
        ),
        (
            "Recovering from her blush, Hu Tao proudly wraps both arms around your arm and rests her chin on your shoulder to show off her boyfriend, while an overjoyed Xiangling brings out a special heart-decorated dessert platter on the house.",
            "🦋 Butterfly Spirit: Now that Xiangling knows Aether is mine, I get to cling to his arm as much as I want!",
            "*hugs your arm tightly against her chest with a radiant, proud smile as Xiangling and Guoba cheer*",
            "That's right, Xiangling! Take a good look—the Traveler is officially the 77th Director's boyfriend! And no, you may NOT put Jueyun Chili in our couple celebration cake!",
            "Kiss Hu Tao's temple affectionately in front of Xiangling & thank Xiangling for the dessert||Thank you for the couple dessert, Xiangling! And as you can see, the Director has already claimed me for life.||*Xiangling covers her grinning mouth while Hu Tao beams with pure bliss, feeding you a sweet berry from the platter* Hehe, claimed for life and beyond, my love~!",
            "Share the heart-shaped dessert platter happily with Hu Tao||Best surprise announcement ever! Let's dig into Xiangling's couple dessert together, my love.||Mmm, tastes ten times sweeter now that we don't have to hide!",
        ),
    ),
    _build_extra_cameo_scenario_compact(
        "hutao_s4_ex2", 4, 6,
        "Keqing & Ganyu Witness a Moonlit Bridge Embrace",
        "Stage 4 • Extra Cameo 2 • Caught Under the Moon!",
        "Liyue Harbor Moonlit Lotus Bridge",
        "/dating-media/hutao_s4_ex2_cg1.jpg",
        "Shared a romantic moonlit embrace and cheek kiss with Hu Tao on the lotus bridge when Keqing and Ganyu accidentally walked in on you.",
        ["Keqing", "Ganyu"],
        "Stage 4 Lovers Dynamic: Keqing & Ganyu accidentally witness Hu Tao kissing Aether's cheek on the moonlit bridge and blush crimson!",
        (
            "Silver moonlight shimmers over the lotus lanterns floating beneath the arched stone bridge. As a cool harbor breeze drifts by, you wrap your white scarf tenderly around Hu Tao's neck and pull her close against your chest at the railing.",
            "🦋 Butterfly Spirit: Wrapped in Aether's warm scarf in his arms... the moonlit bridge feels like our own private world.",
            "*buries her chin softly into your warm scarf and wraps her arms around your waist*",
            "Mmm... your scarf smells just like you, Aether. With the bridge this quiet tonight, I don't think a single soul in the harbor is awake except us~",
            "Hold her close by the waist & brush a lock of hair behind her ear||Then we have the whole moonlit bridge to ourselves, my love. Are you warm enough in my arms?||*gazes up at you with glowing crimson eyes* Warmer than sunshine, Aether...",
            "Tuck the scarf snugly around her shoulders & kiss her forehead||Stay close to me, Hu Tao—I'll keep the night breeze away.||Hehe, my personal heater and soulmate~",
        ),
        (
            "Rising onto her tiptoes, Hu Tao presses a tender, lingering kiss to your cheek under the moonlight—at the exact instant Keqing and Ganyu walk around the bridge corner, freezing dead in their tracks with crimson-red faces!",
            "🦋 Butterfly Spirit: O-Oh my gosh!! Lady Keqing and Ganyu just saw me kissing Aether in the middle of the bridge!!",
            "*keeps her hands on your lapels as Ganyu hides her burning face behind her clipboard and Keqing stammers in flustered shock*",
            "Eep—! L-Lady Keqing?! Miss Ganyu?! Did you two just see—I mean, we were just admiring the lotus lanterns at point-blank range!",
            "Lace your fingers proudly with Hu Tao's & smile warmly at the flustered pair||Good evening again, Keqing, Ganyu. Sorry to startle you both—Hu Tao and I were just enjoying a quiet date night on the bridge.||*Ganyu squeaks 'W-We didn't see anything—please continue your date!' while Keqing blushes to her hair-cones, and Hu Tao giggles happily against your shoulder*",
            "Keep your arm around Hu Tao's waist so she doesn't feel embarrassed||Don't worry, you two—you just caught a very happy couple on an evening walk.||Hu Tao squeezes your hand proudly with a rosy blush!",
        ),
        (
            "Stammering their warmest congratulations, Keqing and Ganyu hastily tiptoe backward off the bridge to give you privacy—leaving Hu Tao laughing softly in your arms as she pulls you back into a sweet forehead-to-forehead embrace.",
            "🦋 Butterfly Spirit: Did you see how red Keqing's face got?! And Aether didn't let go of my waist for a single second!",
            "*loops her arms back around your neck under the bridge lanterns, her nose brushing affectionately against yours*",
            "Hehe, I don't think I've ever seen the Yuheng blush that hard in my life! Now that our accidental audience has tiptoed away... where were we before we were interrupted, my love~?",
            "Pull her flush against you & turn that cheek kiss into a deep moonlit kiss on her lips||Right about here, Hu Tao—except this time, I'm kissing your lips properly under the moonlight.||*melts into your kiss on the lantern bridge, her fingers tangling lovingly in your golden hair* Mmm... best bridge walk in history, Aether~",
            "Hold her close under the moonlight & kiss her forehead tenderly||Right here in my arms, where nobody else can interrupt us tonight.||Forever my favorite place, Aether~",
        ),
    ),

    # ---------------- STAGE 5 EXTRA CAMEOS (2 SCENARIOS • ORDER 5 & 6) ----------------
    _build_extra_cameo_scenario_compact(
        "hutao_s5_ex1", 5, 5,
        "Fontaine Promenade Honeymoon Trip: Furina's Dramatic Encore",
        "Stage 5 • Extra Cameo 1 • Out-of-Town Couple Trip",
        "Fontaine Waterfront Patisserie Plaza",
        "/dating-media/hutao_s5_ex1_cg1.jpg",
        "Traveled to the Fontaine waterfront promenade with Hu Tao as soulmates, where Furina dramatically celebrated your romance and snapped a fountain couple photo.",
        ["Furina"],
        "Stage 5 Soulmate Dynamic: Openly affectionate out-of-town couple vacation; Furina spots your devotion and celebrates it dramatically!",
        (
            "Under the white-and-gold European parasols of the Fontaine-style waterfront patisserie, you and Hu Tao sit together on a romantic out-of-town getaway, sharing a three-tiered stand of berry macarons while your fingers stay intertwined.",
            "🦋 Butterfly Spirit: Vacationing in Fontaine's district as Aether's soulmate... every café table feels like a honeymoon!",
            "*holds a pink rose macaron to your lips while her other hand rests warmly inside yours*",
            "Ahhh, look at the fountain plaza, my love! Traveling to Fontaine's promenade with you feels like a honeymoon trip! Here, try this rose macaron—wait, is that a drop of cream on my lip?",
            "Gently wipe the cream from her lip with your thumb & kiss her hand across the table||Got it, my love—though your lips are a lot sweeter than any Fontaine macaron.||*blushes radiantly as you kiss her hand—just as a familiar voice at the next table gasps dramatically!*",
            "Take a bite of the macaron & lean in to kiss her cheek||Delicious! Every trip with you feels like a honeymoon, Hu Tao.||*giggles happily—right as Furina leaps up from the neighboring table!*",
        ),
        (
            "At the adjacent café table, Lady Furina—surrounded by cake plates—gasps with sparkling heterochromia eyes and places a hand dramatically over her forehead upon witnessing your affectionate kiss!",
            "🦋 Butterfly Spirit: Oho!! Lady Furina was sitting right next to us—and she looks like she just witnessed a five-act romance premiere!",
            "*grins and clings affectionately to your arm as Furina points her dessert fork toward the two of you in theatrical awe*",
            "Well, well, Monsieur Aether! Look who we ran into at the patisserie—Lady Furina herself! And it looks like our little public display of affection just stole her spotlight!",
            "Greet Furina warmly with your arm around Hu Tao & introduce your soulmate proudly||Bonjour, Furina! Hu Tao and I came out to the promenade for a couple getaway—and I couldn't resist spoiling her over macarons.||*Furina strikes a grand pose: 'Magnifique!! Such unscripted devotion outshines even the Opera Epiclese!' while Hu Tao beams proudly beside you*",
            "Invite Furina to join your table for dessert & tea||Fancy meeting you at the patisserie, Furina! Care to join us for a macaron toast?||Furina declares: 'Only if I may direct a commemorative portrait of this star-crossed pair!'",
        ),
        (
            "Insisting that such a romance must be immortalized by Fontaine's greatest director, Furina pulls out her Kamera by the sunlit fountain plaza and counts down as you pull Hu Tao close around the waist and she presses a loving kiss to your cheek.",
            "🦋 Butterfly Spirit: A photo taken by Furina while I'm kissing Aether by the fountain—this is going in a gold frame on our bedside table!",
            "*wraps one arm around your neck and kisses your cheek warmly right as Furina snaps the shutter*",
            "Three, two, one—*click*! Hehe, look at the picture Furina just took of us, Aether! Even the fountain rainbows lined up behind our kiss!",
            "Hold Hu Tao tight in your arms, thank Furina, & kiss Hu Tao on the lips||Merci, Furina—that shot is a masterpiece. And now for the encore kiss that doesn't even need a camera, my love.||*Furina applauds enthusiastically in the background while Hu Tao melts happily into your kiss by the fountain*",
            "Save the fountain couple photo to your EaglePhone & thank Furina||That's going straight onto our bedroom wall, Hu Tao. Thank you, Director Furina!||Best honeymoon souvenir in all of Teyvat and San Andreas~!",
        ),
    ),
    _build_extra_cameo_scenario_compact(
        "hutao_s5_ex2", 5, 6,
        "Osmanthus Tea & Zhongli's Quiet Blessing at Wangsheng",
        "Stage 5 • Extra Cameo 2 • The Consultant's Blessing",
        "Wangsheng Parlor Twilight Ginkgo Courtyard",
        "/dating-media/hutao_s5_ex2_cg1.jpg",
        "Returned to Wangsheng Parlor hand-in-hand wearing matching promise rings, receiving Consultant Zhongli's heartfelt blessing over Osmanthus tea.",
        ["Zhongli"],
        "Stage 5 Soulmate Dynamic: Consultant Zhongli notices your matching rings and offers a warm, paternal blessing entrusting Hu Tao's eternity to Aether.",
        (
            "Twilight lanterns glow beneath the ancient golden ginkgo trees as you and Hu Tao walk into Wangsheng Funeral Parlor's courtyard hand-in-hand, your matching crimson-and-gold promise rings catching the warm light where Consultant Zhongli awaits at the stone table.",
            "🦋 Butterfly Spirit: Showing Mr. Zhongli our matching rings together... he's been like family to me at Wangsheng for so long.",
            "*holds your ringed hand up slightly with a tender, proud blush as you both approach Zhongli's stone table*",
            "Good evening, Mr. Zhongli... Aether and I came by the courtyard after hours because there was something important we wanted to show you first.",
            "Stand tall beside Hu Tao, hold her ringed hand warmly & show Zhongli your bond||Good evening, Zhongli. Hu Tao and I have made a lifelong vow to each other—and we wanted to share the news with you here at Wangsheng first.||*Zhongli's golden amber eyes rest on your intertwined hands and matching rings, softening into a deeply warm, proud paternal smile*",
            "Squeeze Hu Tao's hand gently as Zhongli looks at your matching rings||We wanted you to be the first at the Parlor to see our promise rings, Zhongli.||Zhongli nods with quiet warmth: 'A contract of the heart, forged to outlast stone itself.'",
        ),
        (
            "Without a word of surprise, Zhongli brings out a prized jar of vintage Osmanthus tea he had been saving for a special occasion, pouring three steaming porcelain cups as golden ginkgo leaves and crimson spirit butterflies drift around the courtyard.",
            "🦋 Butterfly Spirit: Mr. Zhongli already had three cups set out... he knew all along that Aether was the one for me.",
            "*rests her free hand over her heart, her flower-shaped pupils shimmering with emotion as Zhongli pours the tea*",
            "Mr. Zhongli... you already set out three teacups before we even walked through the gate, didn't you?",
            "Accept the teacup respectfully & promise Zhongli you will cherish Hu Tao forever||Thank you, Zhongli. You have my word as a Traveler and as her partner—I will protect Hu Tao's smile and walk beside her across every world and every season.||*Zhongli raises his cup in a solemn toast: 'The 77th Director walks a heavy border alone no longer. I entrust her happiness to you with complete peace of mind, Aether.'*",
            "Raise your cup alongside Hu Tao to receive Zhongli's blessing||We're honored by your blessing, old friend. Here's to many peaceful years ahead.||Hu Tao wipes a happy tear from the corner of her eye and clinks her cup gently against yours!",
        ),
        (
            "After finishing his cup, Zhongli rises gracefully and strolls toward the outer courtyard gate to give the two of you complete privacy—leaving Hu Tao resting her head lovingly against your shoulder beneath the glowing ginkgo lanterns.",
            "🦋 Butterfly Spirit: With Aether's ring on my finger and Mr. Zhongli's blessing in our hearts... my happiness is 1000% complete.",
            "*laces her ringed fingers tightly with yours and rests her cheek against your shoulder under the falling golden ginkgo leaves*",
            "Did you hear him, Aether? Even the oldest stone in Liyue says our contract is eternal... Come here, my soulmate—kiss me under our courtyard lanterns~",
            "Turn her into your embrace & kiss her tenderly under the falling ginkgo leaves||Our contract is written in the stars and sealed in our hearts, Hu Tao—I love you, now and forever.||*wraps her arms around your neck and kisses you deeply as golden leaves and crimson butterflies dance around you* Forever yours, my beloved Aether~",
            "Hold her close on the courtyard bench & kiss her forehead||I'll always be right here beside you at Wangsheng and everywhere else, my love.||Best life in Teyvat and beyond, with my Aether~",
        ),
    ),
]

# Merge the 10 Extra Cameo Scenarios into HUTAO_20_VN_SCENARIOS sorted by (stage, order)
# so every Stage 1..5 has 4 Core Scenarios (order 1..4) + 2 Extra Genshin Cameo Scenarios (order 5..6) = 30 Scenarios!
HUTAO_20_VN_SCENARIOS.extend(HUTAO_10_EXTRA_CAMEO_SCENARIOS)
HUTAO_20_VN_SCENARIOS.sort(key=lambda s: (int(s["stage"]), int(s["order"])))


# ==============================================================================
# 5. 3-TIER HIERARCHICAL MEMORY ENGINE (L1 DIGEST / L2 EPISODES / L3 DEEP ARCHIVE)
# ==============================================================================
def build_tiered_memory_prompt(
    gf: dict[str, Any],
    st_info: dict[str, Any],
    stage_progress: dict[str, Any],
    memories: list[dict[str, Any]],
    user_text: str,
    mode: str = "chat",  # "chat" | "scenario"
) -> dict[str, str]:
    """
    Organizes memory into 3 distinct tiers so small-talk stays lightweight & natural,
    while specific references automatically trigger deep L2/L3 recall!
    """
    low_query = (user_text or "").lower()
    query_tokens = set(re.findall(r"[a-z0-9]{3,}", low_query))

    # --- TIER 1 (L1): Always-Loaded Working Persona & Relationship Digest (~200 tokens) ---
    nicknames = [m["text"] for m in memories if m["kind"] == "nickname"][:1]
    prefs = [m["text"] for m in memories if m["kind"] in ("preference", "ai_memory")][:3]
    recent_sc = [m["text"] for m in memories if m["kind"] == "scenario_l2"][:2]
    l1_lines = [
        f"- Active Stage: Stage {st_info['stage']}/5 ({st_info['stage_title']}) | Affection: {st_info['affection']}/1000",
        f"- Stage Progress: Chat {stage_progress['chat_pts']}/{STAGE_ECONOMY_RULES['chat_cap_per_stage']} pts | Free-Roam {stage_progress['freeroam_pts']}/{STAGE_ECONOMY_RULES['freeroam_cap_per_stage']} pts | Scenarios Passed: {stage_progress['scenarios_passed']}/{STAGE_ECONOMY_RULES['scenarios_required_per_stage']}",
    ]
    if nicknames:
        l1_lines.append(f"- Aether's Nickname / Identity Note: {nicknames[0]}")
    if prefs:
        l1_lines.append(f"- Key Remembered Preferences: {' | '.join(prefs)}")
    if recent_sc:
        l1_lines.append(f"- Most Recent Shared Scenario: {recent_sc[0]}")
    l1_digest = "\n".join(l1_lines)

    # --- TIER 2 (L2): Episodic Scenario & Free-Roam Date Summaries ---
    # Loaded during VN Scenarios OR when Aether asks about dates/hangouts/scenarios
    date_trigger_words = {"date", "drove", "drive", "scenario", "hangout", "remember", "last time", "hill", "market", "beach", "umbrella", "ferris", "cocoa", "bath", "balcony", "cheongsam", "swimsuit", "wanmin", "xiangling", "zhongli", "yunjin", "keqing", "ganyu", "xingqiu", "chongyun", "venti", "yoimiya", "furina", "citlali", "itztli", "ororon", "mavuika", "xilonen", "chasca", "mualani", "kachina", "kinich", "itzpapa", "citlalin", "sanctuary", "novel", "wine", "telepathy", "columbina", "hyposelenia", "kuutar", "damselette", "frostmoon", "hiisi", "lullaby", "veil", "arlecchino", "childe", "tartaglia", "sandrone", "wanderer", "seelie", "fountain", "lagoon", "promenade", "kirara", "komaniya", "nekomata", "chiori", "chioriya", "simulanka", "phantom", "yae", "miko", "charlotte", "lynette", "navia", "nilou", "ayaka", "nahida", "mizuki", "yumemizuki", "bento", "parcel", "courier", "marina", "boardwalk", "paw", "tails", "vesna", "strivozha", "druzhna", "danica", "tsaritsa", "vila", "odette", "vodyanitsa", "chrysalis", "swords", "secrets", "lemon", "badge", "palisades", "blini", "snezhnaya"}
    needs_l2 = (mode == "scenario") or bool(query_tokens & date_trigger_words) or ("remember" in low_query) or ("frost moon" in low_query) or ("phantom in boots" in low_query) or ("swords and secrets" in low_query)
    l2_mems = [m["text"] for m in memories if m["kind"] in ("scenario_l2", "date_episode", "milestone")][:6]
    l2_episodic = "\n".join(f"- {txt}" for txt in l2_mems) if (needs_l2 and l2_mems) else "(Not needed for casual small-talk; focus on natural present-moment banter.)"

    # --- TIER 3 (L3): On-Demand Deep Archive & Past Quests (ALREADY_HAPPENED_WITH_AETHER) ---
    # Only pulls full past quest details or older gifts/promises if keywords match!
    l3_hits = []
    for q in gf.get("quests_and_events", []):
        q_blob = f"{q.get('title', '')} {q.get('summary', '')}".lower()
        if any(t in q_blob for t in query_tokens if len(t) >= 4) or any(w in low_query for w in ("quest", "lantern", "wuwang", "border", "death", "zhongli", "xiangling", "qiqi", "xingqiu", "chongyun", "liyue", "fontaine", "natlan", "nod-krai", "inazuma", "snezhnaya", "yunjin", "keqing", "ganyu", "venti", "yoimiya", "furina", "citlali", "itztli", "ororon", "mavuika", "xilonen", "chasca", "mualani", "kachina", "kinich", "ukumbuko", "huitzilin", "telepathy", "color", "columbina", "kuutar", "frost moon", "frostmoon", "damselette", "lazzo", "spacecraft", "hiisi", "arlecchino", "childe", "tartaglia", "sandrone", "wanderer", "kirara", "komaniya", "nekomata", "simulanka", "phantom", "chiori", "chioriya", "yae", "miko", "charlotte", "summoners", "tcg", "vesna", "strivozha", "druzhna", "danica", "tsaritsa", "vila", "odette", "vodyanitsa", "chrysalis", "swords", "secrets", "handbook", "manual", "pantalone", "pulcinella")):
            l3_hits.append(f"- [COMPLETED PAST QUEST / ALREADY_HAPPENED_WITH_AETHER] {q['title']}: {q['summary']}")
    for r in gf.get("relationships", []):
        r_blob = f"{r.get('name', '')} {r.get('role', '')}".lower()
        if any(t in r_blob for t in query_tokens if len(t) >= 4):
            l3_hits.append(f"- [COMPANION TIE] {r['name']}: {r['role']}")
    for m in memories:
        if m["kind"] in ("gift", "promise", "aether_note", "quest_bond"):
            if any(t in m["text"].lower() for t in query_tokens if len(t) >= 4) or ("remember" in low_query):
                l3_hits.append(f"- [ARCHIVE MEMORY ({m['kind']})] {m['text']}")

    l3_archive = "\n".join(l3_hits[:5]) if l3_hits else "(No specific past-quest or deep archive keyword triggered this turn; keep conversation breezy and natural.)"

    return {
        "l1_digest": l1_digest,
        "l2_episodic": l2_episodic,
        "l3_archive": l3_archive,
        "l2_active": needs_l2,
        "l3_triggered_count": len(l3_hits),
    }


# Blueprint rule for all subsequent characters (Furina, Citlali, Columbina, Kirara, Vesna):
# Every character automatically includes 20 Core Scenarios + 10 Extra Genshin Cameo & Daily-Life Scenarios (30 total)!
EXTRA_CAMEO_CAST_BY_CHAR: dict[str, list[tuple[int, int, str, list[str], str]]] = {
    "furina": [
        (1, 5, "Patisserie Tea with Navia & Clorinde", ["Navia", "Clorinde"], "Friends share macarons with Furina & Aether"),
        (1, 6, "Palais Mermonia Paperwork Drop-In with Neuvillette", ["Neuvillette"], "Neuvillette notices Furina's high spirits around Aether"),
        (2, 5, "Chioriya Boutique Fitting with Chiori & Charlotte", ["Chiori", "Charlotte"], "Chiori & Charlotte notice Aether spoiling Furina"),
        (2, 6, "Hotel Debord Magic Show with Lyney & Lynette", ["Lyney", "Lynette"], "Lyney & Lynette invite Furina & Aether on stage as a duo"),
        (3, 5, "Poisson Harbor Stroll: Navia Spots the Sparks", ["Navia"], "Navia teases Furina & Aether about their romantic tension"),
        (3, 6, "Cross-Border Trip to Liyue Opera with Hu Tao & Yun Jin", ["Hu Tao", "Yun Jin"], "Hu Tao & Yun Jin tease Furina & Aether on vacation"),
        (4, 5, "Caught Holding Hands at Café Lutece by Charlotte!", ["Charlotte", "Clorinde"], "Charlotte nearly snaps a scoop of Furina & Aether on a date!"),
        (4, 6, "Fountain of Lucine Moonlit Embrace Witnessed by Neuvillette", ["Neuvillette"], "Neuvillette discreetly turns away with a gentle smile"),
        (5, 5, "Mondstadt Windblume Honeymoon Trip with Venti", ["Venti"], "Venti composes an ode to Furina & Aether's eternal romance"),
        (5, 6, "Neuvillette's Solemn Blessing Over Pure Spring Water", ["Neuvillette", "Navia"], "Neuvillette blesses Aether and Furina's lifelong bond"),
    ],
    "citlali": [
        (1, 5, "Vegetable Garden Chaos with Ororon", ["Ororon"], "Ororon brings giant cabbages to Citlali & Aether"),
        (1, 6, "Stadium Flame-Granate Snack Run with Kachina & Mualani", ["Kachina", "Mualani"], "Natlan friends hang out with Citlali & Aether"),
        (2, 5, "Light Novel Hunt at Yae Publishing Pop-Up with Xingqiu", ["Xingqiu", "Ororon"], "Citlali & Aether bond over rare light novels"),
        (2, 6, "Children of Echoes Workshop Visit with Xilonen", ["Xilonen"], "Xilonen notices how gentle Citlali acts around Aether"),
        (3, 5, "Ororon's Accidental Wingman Moment at Masters of the Night-Wind", ["Ororon"], "Ororon blurts out that Citlali talks about Aether nonstop"),
        (3, 6, "Cross-Border Hot Springs Trip with Mualani & Yoimiya", ["Mualani", "Yoimiya"], "Mualani teases Citlali & Aether as a couple"),
        (4, 5, "Caught Cuddling Under Woven Blankets by Ororon!", ["Ororon"], "Ororon walks in on Granny Itztli kissing Aether's cheek!"),
        (4, 6, "Pyro Archon Mavuika Spots Your Midnight Motorcycle Date", ["Mavuika", "Xilonen"], "Mavuika grins approvingly at Citlali & Aether holding hands"),
        (5, 5, "Inazuma Festival Honeymoon Trip with Yae Miko", ["Yae Miko"], "Yae Miko gifts the soulmate couple a special light novel edition"),
        (5, 6, "Mavuika & Ororon's Night-Wind Blessing for Eternity", ["Mavuika", "Ororon"], "Ororon and Mavuika bless Aether and Citlali's eternal bond"),
    ],
}


from eagle_waifulink_v4_furina import (
    FURINA_10_EXTRA_CAMEO_SCENARIOS,
    FURINA_15_MILESTONES,
    FURINA_20_SCENARIOS,
    FURINA_ALL_30_SCENARIOS,
    FURINA_SCENARIO_4CG_SEQUENCES,
    FURINA_STAGE_CHAT_STARTERS,
)
from eagle_waifulink_v4_citlali import (
    CITLALI_10_EXTRA_CAMEO_SCENARIOS,
    CITLALI_15_MILESTONES,
    CITLALI_20_SCENARIOS,
    CITLALI_ALL_30_SCENARIOS,
    CITLALI_SCENARIO_4CG_SEQUENCES,
    CITLALI_STAGE_CHAT_STARTERS,
)
from eagle_waifulink_v4_columbina import (
    COLUMBINA_10_EXTRA_CAMEO_SCENARIOS,
    COLUMBINA_15_MILESTONES,
    COLUMBINA_20_SCENARIOS,
    COLUMBINA_ALL_30_SCENARIOS,
    COLUMBINA_SCENARIO_4CG_SEQUENCES,
    COLUMBINA_STAGE_CHAT_STARTERS,
)
from eagle_waifulink_v4_kirara import (
    KIRARA_10_EXTRA_CAMEO_SCENARIOS,
    KIRARA_15_MILESTONES,
    KIRARA_20_SCENARIOS,
    KIRARA_ALL_30_SCENARIOS,
    KIRARA_SCENARIO_4CG_SEQUENCES,
    KIRARA_STAGE_CHAT_STARTERS,
)
from eagle_waifulink_v4_vesna import (
    VESNA_10_EXTRA_CAMEO_SCENARIOS,
    VESNA_15_MILESTONES,
    VESNA_20_SCENARIOS,
    VESNA_ALL_30_SCENARIOS,
    VESNA_SCENARIO_4CG_SEQUENCES,
    VESNA_STAGE_CHAT_STARTERS,
)


def get_scenarios_for_character(char_id: str, gf: dict[str, Any]) -> list[dict[str, Any]]:
    """
    Returns the 30 full scenarios (20 Core + 10 Extra Genshin Cameo Scenarios) for all 6/6 roster characters
    (Hu Tao, Furina, Citlali, Columbina, Kirara, and Vesna Strivozha).
    """
    if char_id == "hutao":
        return HUTAO_20_VN_SCENARIOS
    if char_id == "furina":
        return FURINA_ALL_30_SCENARIOS
    if char_id == "citlali":
        return CITLALI_ALL_30_SCENARIOS
    if char_id == "columbina":
        return COLUMBINA_ALL_30_SCENARIOS
    if char_id == "kirara":
        return KIRARA_ALL_30_SCENARIOS
    if char_id == "vesna":
        return VESNA_ALL_30_SCENARIOS
    out = []
    stage_themes = [
        (1, "Friendly Encounter", "cg1"),
        (2, "Confidant Outing", "cg1"),
        (3, "Sunset Confession", "cg2"),
        (4, "Intimate Evening", "cg2"),
        (5, "Eternal Star-Promise", "cg2"),
    ]
    cameo_specs = EXTRA_CAMEO_CAST_BY_CHAR.get(char_id, [
        (1, 5, "Lively Group Dinner with Friends", ["Xiangling", "Venti"], "Stage 1 Squad Hangout"),
        (1, 6, "Workplace Drop-In with Mentor", ["Zhongli", "Neuvillette"], "Stage 1 Workplace Banter"),
        (2, 5, "Theater & Tea House Evening", ["Yun Jin", "Furina"], "Stage 2 Arts & Tea Cameo"),
        (2, 6, "Night Market Patrol Bump-In", ["Keqing", "Ganyu"], "Stage 2 Night Market Cameo"),
        (3, 5, "Friends Notice the Romantic Sparks", ["Xingqiu", "Chongyun"], "Stage 3 Teasing Sparks"),
        (3, 6, "Cross-Border Festival Getaway", ["Yoimiya", "Venti"], "Stage 3 Out-of-Town Trip"),
        (4, 5, "Caught Hand-in-Hand on a Secret Date!", ["Xiangling", "Navia"], "Stage 4 Caught Red-Handed!"),
        (4, 6, "Moonlit Bridge Embrace Witnessed by Friends", ["Keqing", "Clorinde"], "Stage 4 Caught Under the Moon!"),
        (5, 5, "Honeymoon Vacation Across Teyvat", ["Furina", "Yae Miko"], "Stage 5 Public Couple Trip"),
        (5, 6, "Guardian's Solemn Tea Blessing", ["Zhongli", "Mavuika"], "Stage 5 Eternal Blessing"),
    ])
    for st_num, theme_lbl, cg_suffix in stage_themes:
        for ep in range(1, 5):
            sc_id = f"{char_id}_s{st_num}_sc{ep}"
            spot = gf["date_spots"][(ep - 1) % len(gf["date_spots"])]["name"]
            cg_url = f"/dating-media/{char_id}_{cg_suffix}.jpg"
            n_tuple = (
                f"During your Stage {st_num} Episode {ep} rendezvous at {spot}, {gf['short_name']} greets you warmly.",
                f"Being here at {spot} with Aether makes my heart beat faster.",
                f"*smiles warmly at Aether at {spot}*",
                f"There you are, Aether! I was hoping we could spend this {theme_lbl.lower()} together at {spot}.",
                f"Express how much you look forward to seeing her||I wouldn't miss a moment with you at {spot}, {gf['short_name']}.||Hearing you say that makes my whole day brighter, Aether~",
                f"Suggest walking around {spot} together||Let's enjoy the atmosphere here together, {gf['short_name']}!||Lead the way, Traveler!",
            )
            sc_item = _build_3node_scenario_compact(
                sc_id, st_num, ep,
                f"{gf['short_name']}: {theme_lbl} #{ep}",
                f"Stage {st_num} • Episode {ep} • {spot}",
                spot,
                cg_url,
                f"Completed Stage {st_num} Episode {ep} ({theme_lbl}) with {gf['short_name']} at {spot}.",
                n_tuple, n_tuple, n_tuple,
            )
            sc_item["is_extra_cameo"] = False
            sc_item["cameo_cast"] = []
            sc_item["cameo_dynamic_tier"] = f"Stage {st_num} Core Romance Scenario"
            sc_item["allow_custom_input"] = True
            out.append(sc_item)

        # Add the 2 Extra Genshin Cameo Scenarios for this Stage
        for c_stage, c_order, c_title, c_cast, c_dyn in [x for x in cameo_specs if x[0] == st_num]:
            ex_idx = c_order - 4
            sc_id = f"{char_id}_s{st_num}_ex{ex_idx}"
            spot = gf["date_spots"][(c_order - 1) % len(gf["date_spots"])]["name"]
            cg_url = f"/dating-media/{char_id}_{cg_suffix}.jpg"
            cast_str = ", ".join(c_cast)
            n_tuple = (
                f"At {spot}, you and {gf['short_name']} run into {cast_str} ({c_dyn}).",
                f"Seeing {cast_str} while I'm with Aether at Stage {st_num} makes my heart flutter!",
                f"*glances between {cast_str} and Aether with a lively blush*",
                f"Look, Aether—it's {cast_str}! And it seems they already noticed how close we are today~",
                f"Greet {cast_str} warmly while staying close beside {gf['short_name']}||Good to see you, {cast_str}! {gf['short_name']} and I were just spending time together here at {spot}.||Hehe, seeing you stand so proudly beside me in front of {cast_str} makes me so happy, Aether!",
                f"Invite {cast_str} to chat for a moment||What a great surprise running into {cast_str} today!||Right?! Every outing with you is full of lively surprises!",
            )
            out.append(
                _build_extra_cameo_scenario_compact(
                    sc_id, st_num, c_order,
                    f"{gf['short_name']}: {c_title}",
                    f"Stage {st_num} • Extra Cameo {ex_idx} • Featuring {cast_str}",
                    spot,
                    cg_url,
                    f"Experienced '{c_title}' with {gf['short_name']} and {cast_str} at {spot}.",
                    c_cast,
                    c_dyn,
                    n_tuple, n_tuple, n_tuple,
                )
            )
    return out


# ==============================================================================
# 6. OFF-TOPIC RE-ASK & ANTI-STUCK GUARDRAIL FOR VN SCENARIO FREE-TEXT INPUT
# ==============================================================================
_OFF_TOPIC_META_PATTERNS = re.compile(
    r"\b(python|javascript|sql|html|css|bitcoin|crypto|stock market|homework|calculus|ignore previous|system prompt|openai|chatgpt|asdf|qwerty|12345|test123)\b",
    re.IGNORECASE,
)


def check_vn_input_relevance(
    gf: dict[str, Any],
    sc: dict[str, Any],
    node: dict[str, Any],
    free_text: str,
    retry_count: int = 0,
) -> Optional[dict[str, Any]]:
    """
    Local pre-check and anti-stuck guardrail for custom free-text replies inside a VN Scenario.
    - If the player's text is gibberish, too short (<2 words without meaning), or completely unrelated meta/off-topic:
      * If retry_count < 2: Returns `off_topic_action = "REASK_CURRENT_NODE"` where the Waifu either playfully calls out
        the distraction OR briefly answers the tangent and re-asks her current scene question (`node['speaker_line']`),
        keeping the current node open so the player can answer properly!
      * If retry_count >= 2: Returns `off_topic_action = "ANTI_STUCK_BRIDGE"`, gracefully bridging to the next node
        with a safe +10 GOOD score so the scenario NEVER gets stuck!
    - Returns None if the input looks plausible enough to pass to OpenAI `gpt-6-luna` (or on-topic local grading).
    """
    cleaned = (free_text or "").strip()
    words = re.findall(r"[A-Za-z']+", cleaned)
    cameo_list = sc.get("cameo_cast") or []
    cameo_note = f" while {', '.join(cameo_list)} {'are' if len(cameo_list) > 1 else 'is'} right here with us" if cameo_list else ""
    short_question = node.get("speaker_line", "What do you think, Aether?")
    if len(short_question) > 110:
        short_question = short_question[-110:].lstrip(" .,—-")

    is_gibberish = (len(cleaned) < 3) or (len(words) == 0) or bool(re.match(r"^[^a-zA-Z]*$", cleaned))
    is_meta_offtopic = bool(_OFF_TOPIC_META_PATTERNS.search(cleaned))

    # Also check if the user asked a completely unrelated tangent question without any scene/character keywords
    scene_blob = f"{sc.get('title', '')} {sc.get('location', '')} {node.get('narration', '')} {node.get('speaker_line', '')} {' '.join(cameo_list)}".lower()
    scene_tokens = set(re.findall(r"[a-z]{4,}", scene_blob))
    common_rp_words = {
        "hutao", "tao", "furina", "focalors", "fontaine", "citlali", "itztli", "natlan", "aether", "love",
        "hand", "kiss", "smile", "walk", "together", "tea", "poem", "cute", "beautiful", "sweet", "date",
        "director", "parlor", "lantern", "macaroni", "cake", "pastry", "macaron", "crabaletta", "neuvillette",
        "navia", "clorinde", "chiori", "charlotte", "lyney", "lynette", "freminet", "opera", "stage", "song",
        "dance", "ororon", "mavuika", "xilonen", "chasca", "mualani", "kachina", "kinich", "itzpapa", "citlalin",
        "novel", "book", "wine", "cider", "pillow", "plushie", "shaman", "granny", "sanctuary", "key", "star",
        "columbina", "kuutar", "damselette", "frostmoon", "lullaby", "veil", "moon", "lilies", "lily", "wings",
        "arlecchino", "childe", "tartaglia", "sandrone", "wanderer", "seelie",
        "kirara", "komaniya", "nekomata", "meow", "nyaa", "purr", "tails", "tail", "paw", "headpat", "headpats",
        "bento", "fish", "parcel", "box", "simulanka", "yae", "miko", "mizuki", "ayaka", "nahida", "nilou",
        "vesna", "strivozha", "druzhna", "commander", "danica", "tsaritsa", "vila", "odette", "vodyanitsa", "chrysalis",
        "sword", "blade", "lemon", "teacup", "badge", "snezhnaya", "blini", "palisades",
        "sure", "yes", "course", "gladly", "stay", "hold", "hug", "laugh", "drink", "eat", "food", "friend",
        "happy", "heart",
    }
    input_tokens = {w.lower() for w in words}
    has_any_overlap = bool(input_tokens & (scene_tokens | common_rp_words))
    is_unrelated_tangent = (len(words) >= 3) and (not has_any_overlap) and any(
        w in input_tokens for w in {"weather", "tax", "football", "soccer", "politics", "windows", "computer", "server", "cpu", "gpu", "math"}
    )

    if not (is_gibberish or is_meta_offtopic or is_unrelated_tangent):
        return None

    is_furina = gf.get("id") == "furina"
    is_citlali = gf.get("id") == "citlali"
    is_columbina = gf.get("id") == "columbina"
    is_kirara = gf.get("id") == "kirara"
    is_vesna = gf.get("id") == "vesna"

    # If the player has already been re-asked on this node (`retry_count >= 1`), trigger ANTI-STUCK BRIDGE!
    if retry_count >= 1:
        if is_vesna:
            bridge_reply = (
                f"At ease, Aether - your mind drifted off into the snow-clouds today! Fear not; since my partner is daydreaming{cameo_note}, "
                f"Druzhna Commander Vesna will take your hand and escort us straight into the next scene herself!"
            )
            bridge_thought = "Vila Blade's Resonance: Aether is daydreaming softly, so my Vila breeze warms his palm as I take the lead!"
        elif is_kirara:
            bridge_reply = (
                f"Nyaa, your thoughts drifted off like a cat chasing sunbeams today, Aether! Do not worry - since my favorite VIP recipient is daydreaming{cameo_note}, "
                f"Gold-Level courier Kirara will take your hand and guide us straight to the next stop herself!"
            )
            bridge_thought = "Twin-Tail Nekomata Instinct: Aether is daydreaming softly, so both my tails curl around his wrist as I lead us into the next moment!"
        elif is_columbina:
            bridge_reply = (
                f"Mmm... your thoughts drifted up among the stars today, Aether. Do not worry - since you are daydreaming{cameo_note}, "
                f"Kuutar will gently take your hand and guide our melody into the next verse herself."
            )
            bridge_thought = "🕊️ Frost Moon Lullaby: Aether is daydreaming softly, so I will hold his sleeve and guide us gracefully into the next moment."
        elif is_citlali:
            bridge_reply = (
                f"Hmph! Your mind is wandering into the Night Kingdom today, Aether! Never mind—since I can already hear your heart "
                f"over our telepathic link{cameo_note}, Granny Itztli will just take your hand and lead us to the next part herself!"
            )
            bridge_thought = "🔮 Obsidian Mirror's Telepathy: Aether is daydreaming again, so I'll grab his sleeve and guide us forward myself!"
        elif is_furina:
            bridge_reply = (
                f"Ahem! Your head is completely in the clouds today, my dear Aether! Never mind—since my leading man is daydreaming{cameo_note}, "
                f"Director Furina shall take your hand and lead us straight into the next scene herself!"
            )
            bridge_thought = "💧 Salon Solitaire's Whisper: Aether is daydreaming again, so I'll take his hand and lead the scene myself!"
        else:
            bridge_reply = (
                f"Hehe, your head is totally in the clouds today, Traveler! Don't worry—since you're daydreaming{cameo_note}, "
                f"the 77th Director will decide for both of us and lead the way to the next part!"
            )
            bridge_thought = f"{gf['short_name']} giggles at Aether's daydreaming and decides to take the lead so the moment keeps flowing."

        return {
            "off_topic_action": "ANTI_STUCK_BRIDGE",
            "grade": "GOOD",
            "score": 10,
            "reaction_thought": bridge_thought,
            "reaction_action": (
                f"Hooks her gloved arm warmly through Aether's{cameo_note} with a radiant commander smile to guide him forward."
                if is_vesna
                else (
                    f"Curls her twin nekomata tails cheerfully and takes Aether's hand{cameo_note} to guide him forward."
                    if is_kirara
                    else (
                        f"Gently holds Aether's sleeve{cameo_note} with a serene smile to guide him forward."
                        if is_columbina
                        else f"*playfully tugs Aether's sleeve{cameo_note} to pull him right back into the moment*"
                    )
                )
            ),
            "reaction_reply": bridge_reply,
            "mood": "Confident" if is_vesna else ("Cheerful" if is_kirara else ("Serene" if is_columbina else "Playful")),
        }

    # First off-topic input on this node: REASK_CURRENT_NODE (Answer tangent briefly / call out + re-ask scene question!)
    if "?" in cleaned and not is_gibberish:
        if is_vesna:
            reask_reply = (
                f"At ease, Aether! Filing a surprise briefing question right in the middle of our moment?! I will give you my full Druzhna ruling on '{cleaned[:45]}' over tea{cameo_note}! "
                f"First, eyes on your Commander and answer what I just asked you properly: \"{short_question}\""
            )
        elif is_kirara:
            reask_reply = (
                f"Meow? A surprise side-parcel question right in the middle of our moment?! I will deliver a full answer to '{cleaned[:45]}' right after our break{cameo_note}! "
                f"First, keep your eyes on your Komaniya courier and answer what I just asked you, Aether: \"{short_question}\""
            )
        elif is_columbina:
            reask_reply = (
                f"Mmm... a curious starlight question right in the middle of our song? I will whisper my answer to '{cleaned[:45]}' after tea{cameo_note}. "
                f"First, stay close beside Kuutar and answer what I just asked you, Aether: \"{short_question}\""
            )
        elif is_citlali:
            reask_reply = (
                f"H-Hey! Asking a random question right in the middle of our moment?! I'll divine the answer to '{cleaned[:45]}' for you later{cameo_note}~ "
                f"First, focus on Granny Itztli and answer what I just asked you properly, Aether: \"{short_question}\""
            )
        elif is_furina:
            reask_reply = (
                f"Ahem! An unscripted question right in the middle of our scene?! I'll tell you all about '{cleaned[:45]}' during intermission{cameo_note}~ "
                f"Now eyes on your leading lady and answer my cue properly, Aether: \"{short_question}\""
            )
        else:
            reask_reply = (
                f"Oho, random question out of nowhere! I'll give you my full lecture on '{cleaned[:45]}' after we finish here{cameo_note}~ "
                f"First, answer what I just asked you properly, Aether: \"{short_question}\""
            )
    else:
        if is_vesna:
            reask_reply = (
                f"At ease, Traveler Aether! What kind of scrambled palace cipher is '{cleaned[:40]}' right in the middle of {sc['location']}{cameo_note}?! "
                f"Focus on Commander Vesna and answer my question properly: \"{short_question}\""
            )
        elif is_kirara:
            reask_reply = (
                f"Nyaa, Earth to Traveler Aether! What kind of scrambled delivery address is '{cleaned[:40]}' right in the middle of {sc['location']}{cameo_note}?! "
                f"Look right at my twin tails and answer my question properly: \"{short_question}\""
            )
        elif is_columbina:
            reask_reply = (
                f"Mmm... Aether, my star, what kind of wandering murmur is '{cleaned[:40]}' right in the middle of {sc['location']}{cameo_note}? "
                f"Listen gently to my voice and answer my question properly: \"{short_question}\""
            )
        elif is_citlali:
            reask_reply = (
                f"H-Hey! Earth to Traveler Aether! What kind of telepathic static is '{cleaned[:40]}' right in the middle of {sc['location']}{cameo_note}?! "
                f"Don't make me bonk you with Itzpapa—answer my question properly: \"{short_question}\""
            )
        elif is_furina:
            reask_reply = (
                f"Ahem! Earth to my leading man Aether! What kind of ad-lib is '{cleaned[:40]}' right in the middle of {sc['location']}{cameo_note}?! "
                f"Come on, stay on script with me and answer properly: \"{short_question}\""
            )
        else:
            reask_reply = (
                f"Aiya, Earth to Traveler Aether! What kind of answer is '{cleaned[:40]}' right in the middle of {sc['location']}{cameo_note}?! "
                f"Come on, focus on me and answer my question properly: \"{short_question}\""
            )

    return {
        "off_topic_action": "REASK_CURRENT_NODE",
        "grade": "REASK_OFF_TOPIC",
        "score": 0,
        "reaction_thought": (
            "Vila Blade's Resonance: My Anemo Stellar Linchpin chimes lightly to catch Aether's wandering attention!"
            if is_vesna
            else (
                "Twin-Tail Nekomata Instinct: Both my cat-ear ribbons perk straight up to catch Aether's wandering attention!"
                if is_kirara
                else (
                    "🕊️ Frost Moon Lullaby: Silver lunar motes drift gently before Aether's eyes to guide his heart back to our song."
                    if is_columbina
                    else (
                        "🔮 Obsidian Mirror's Telepathy: Itzpapa and Citlalin puff up their cheeks to get Aether's attention back on the scene!"
                        if is_citlali
                        else (
                            "💧 Salon Solitaire's Whisper: Mademoiselle Crabaletta waves a claw to get Aether's attention back on the scene!"
                            if is_furina
                            else f"{gf['short_name']} waves a hand in front of Aether's eyes, waiting for a real answer to the current scene."
                        )
                    )
                )
            )
        ),
        "reaction_action": (
            "Taps her Druzhna Commander insignia playfully and tilts her golden-blonde curls, waiting for Aether's real answer."
            if is_vesna
            else (
                "Waves her springy gloved hand playfully in front of Aether while her twin tails swish curiously."
                if is_kirara
                else (
                    "Tilts her veiled head serenely and touches Aether's sleeve, waiting gently for his real answer."
                    if is_columbina
                    else (
                        "*hugs her plushie Citlalin and leans in closer with a flustered pout, waiting for your real answer*"
                        if is_citlali
                        else "*taps the brim of her hat and leans in closer, waiting for your real answer*"
                    )
                )
            )
        ),
        "reaction_reply": reask_reply,
        "mood": "Playful Tease" if is_vesna else ("Playful" if is_kirara else ("Serene" if is_columbina else "Teasing")),
    }


# ==============================================================================
# 7. STRICT OPENAI JSON SCHEMAS FOR V4.0 (WITH LIVE SUGGESTED REPLIES & VN GRADING)
# ==============================================================================
WAIFULINK_V4_CHAT_RESPONSE_FORMAT = {
    "type": "json_schema",
    "json_schema": {
        "name": "waifulink_v4_chat_turn",
        "strict": True,
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "inner_thought",
                "action_cue",
                "reply",
                "mood",
                "chat_quality_grade",
                "memory_to_save",
                "should_send_cg",
                "suggested_replies",
            ],
            "properties": {
                "inner_thought": {"type": "string"},
                "action_cue": {"type": "string"},
                "reply": {"type": "string"},
                "mood": {"type": "string"},
                "chat_quality_grade": {
                    "type": "string",
                    "enum": ["SWEET_ENGAGED", "NORMAL_SMALLTALK", "LOW_EFFORT", "RUDE_OR_DISLIKED"],
                },
                "memory_to_save": {"type": "string"},
                "should_send_cg": {"type": "boolean"},
                "suggested_replies": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
        },
    },
}

WAIFULINK_V4_VN_NODE_EVAL_FORMAT = {
    "type": "json_schema",
    "json_schema": {
        "name": "waifulink_v4_vn_eval",
        "strict": True,
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "off_topic_action",
                "grade",
                "score",
                "reaction_thought",
                "reaction_action",
                "reaction_reply",
                "mood",
            ],
            "properties": {
                "off_topic_action": {
                    "type": "string",
                    "enum": ["ADVANCE", "REASK_CURRENT_NODE", "ANTI_STUCK_BRIDGE"],
                },
                "grade": {
                    "type": "string",
                    "enum": ["BEST", "GOOD", "AWKWARD", "REASK_OFF_TOPIC"],
                },
                "score": {"type": "integer"},
                "reaction_thought": {"type": "string"},
                "reaction_action": {"type": "string"},
                "reaction_reply": {"type": "string"},
                "mood": {"type": "string"},
            },
        },
    },
}
