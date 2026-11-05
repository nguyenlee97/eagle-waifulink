"""
eagle_waifulink_v4_furina.py - WaifuLink v4.0 Complete Character #2 Package: Furina de Fontaine
================================================================================================
RenderWare CFont-Safe & Los Santos Harmonized Edition (2026-11-04):
1. `FURINA_15_MILESTONES` (`furina_m01` .. `furina_m15`, thresholds `[60, 125, 185, 250, 320, 385, 450, 520, 585, 650, 720, 785, 850, 925, 1000]`):
   - Proactive Time-Apart Smartphone Photo Drops with `Salon Solitaire's Whisper` inner thoughts,
     compact uncut action cues (`<= 56` chars), and 3 uncut reaction choices (`<= 76` chars) per milestone.
2. `FURINA_STAGE_CHAT_STARTERS` (`Stage 1..5` pre-generated EaglePhone dialogue starters).
3. `FURINA_SCENARIO_4CG_SEQUENCES` (`30 Scenarios x 4 Unique 16:9 Scene CGs = 120 Scenario CGs`).
4. `FURINA_20_SCENARIOS` (`20 Core Romance VN Scenarios`, `s1_sc1..s5_sc4`) &
   `FURINA_10_EXTRA_CAMEO_SCENARIOS` (`10 Extra Genshin Cameo VN Scenarios`, `s1_ex1..s5_ex2`).
"""

from __future__ import annotations

from typing import Any

FURINA_15_MILESTONES: list[dict[str, Any]] = [{'id': 'furina_m01',
  'milestone_num': 1,
  'stage': 1,
  'req_affection': 60,
  'spice_tier': 'Stage 1 - Friendly & Playful',
  'url': '/dating-media/furina_m01.jpg',
  'title': "M01: Patisserie 'Pour la Justice' First Bite",
  'caption': "Ahem! As your leading lady, I graciously saved the very first strawberry bite of my 'Pour la "
             "Justice' opera cake for you, Aether!",
  'proactive_inner_thought': "Salon Solitaire's Whisper: Mademoiselle Crabaletta is pinching my ribbon "
                             'because I practiced holding this fork out for five whole minutes before '
                             'snapping the photo!',
  'proactive_action_cue': 'Holds out a strawberry cake bite with a shy smile.',
  'proactive_message': 'Ahem! Aether, where have you wandered off to?! I secured the sunniest table at the '
                       "patisserie and even saved the crown strawberry of my 'Pour la Justice' cake for you "
                       "- don't keep a star waiting!",
  'reaction_choices': [{'id': 'furina_m01_r1',
                        'label': 'Praise her generosity and adorable smile (+6)',
                        'player_text': 'Sharing the first bite of your favorite cake? Your smile makes it '
                                       'sweeter.',
                        'reply_thought': "Salon Solitaire's Whisper: He called my smile sweet right off the "
                                         "bat! Keep your composure, Furina, don't let your top hat wobble!",
                        'reply_action': 'Clears her throat as her cheeks turn rose-pink.',
                        'reply_text': 'N-Naturally! Only my irreplaceable co-star deserves the opening bite '
                                      'of a masterpiece! Hurry over while the black tea is still steaming, '
                                      'Aether!',
                        'mood': 'Delighted'},
                       {'id': 'furina_m01_r2',
                        'label': 'Tease her about Crabaletta guarding the cake (+6)',
                        'player_text': 'If I take that bite, will Mademoiselle Crabaletta pinch my fingers?',
                        'reply_thought': "Salon Solitaire's Whisper: Actually, Crabaletta adores Aether so "
                                         "much she'd probably push the whole plate over to his side of the "
                                         'table!',
                        'reply_action': 'Waves her gloved hand with a playful giggle.',
                        'reply_text': 'Hehe, fear not! I have already instructed the entire Salon Solitaire '
                                      'that Traveler Aether has VIP immunity at my tea table!',
                        'mood': 'Playful'},
                       {'id': 'furina_m01_r3',
                        'label': 'Bring a second box of macarons right now (+6)',
                        'player_text': "Save that forkful for me, Furina! I'm bringing extra macarons right "
                                       'now.',
                        'reply_thought': "Salon Solitaire's Whisper: Extra macarons AND Aether's company?! "
                                         'Today really is a five-star afternoon!',
                        'reply_action': 'Sits up with sparkling eyes and pats the chair.',
                        'reply_text': "Oho! Now that is how a true gentleman treats Fontaine's greatest "
                                      'director! Your seat is reserved, my dear Aether!',
                        'mood': 'Happy'}]},
 {'id': 'furina_m02',
  'milestone_num': 2,
  'stage': 1,
  'req_affection': 125,
  'spice_tier': 'Stage 1 - Friendly & Playful',
  'url': '/dating-media/furina_m02.jpg',
  'title': "M02: Star Director's Clapperboard Call",
  'caption': 'Lights, Kamera, Action! Gentilhomme Usher and I are scouting locations for our next musical, '
             'and my leading man is missing from the frame!',
  'proactive_inner_thought': "Salon Solitaire's Whisper: Ever since we directed 'The Two Musketeers' at the "
                             'Fontinalia Film Festival together, scouting stages alone feels way too quiet '
                             'without Aether.',
  'proactive_action_cue': 'Snaps a wooden clapperboard on the steps and winks.',
  'proactive_message': 'Scene One, Take One - and my leading man is nowhere on set! Look, Aether, even '
                       'Gentilhomme Usher dressed up for rehearsal today. When are you coming by the '
                       'theater?',
  'reaction_choices': [{'id': 'furina_m02_r1',
                        'label': 'Report to set right away as her leading man (+6)',
                        'player_text': "How could I miss my favorite director's call? I'm on my way, Furina.",
                        'reply_thought': "Salon Solitaire's Whisper: He still remembers my Furina Award from "
                                         'the film festival! My heart just skipped a whole measure!',
                        'reply_action': 'Rolls up her script scroll and beams with pride.',
                        'reply_text': 'Ahem! Excellent punctuality, Aether! Since you remembered my '
                                      "prestigious directorial credentials, I'll let you improvise all the "
                                      'best lines today!',
                        'mood': 'Delighted'},
                       {'id': 'furina_m02_r2',
                        'label': "Compliment Gentilhomme Usher's matching top hat (+6)",
                        'player_text': 'You and Gentilhomme Usher look like the sharpest directing duo in '
                                       'town!',
                        'reply_thought': "Salon Solitaire's Whisper: Usher is puffing his chest out so much "
                                         'his Hydro bubble almost popped!',
                        'reply_action': 'Strikes a theatrical pose beside Gentilhomme Usher.',
                        'reply_text': 'Hehe, Usher says thank you! Though between you and me, the '
                                      'composition only reaches perfection when you step into the frame '
                                      'beside me!',
                        'mood': 'Playful'},
                       {'id': 'furina_m02_r3',
                        'label': 'Bring cold Fonta and snacks to rehearsal (+6)',
                        'player_text': "I'm bringing chilled Fonta and Goldenshrimp balls to rehearsal for "
                                       'us.',
                        'reply_thought': "Salon Solitaire's Whisper: Cold Fonta AND Goldenshrimp balls?! He "
                                         'spoils me better than the entire Palais Mermonia staff ever did!',
                        'reply_action': 'Claps her gloved hands together in excitement.',
                        'reply_text': 'Wait - Goldenshrimp balls too?! Truly, Aether, you understand the '
                                      'artistic temperament better than anyone in this world!',
                        'mood': 'Excited'}]},
 {'id': 'furina_m03',
  'milestone_num': 3,
  'stage': 1,
  'req_affection': 185,
  'spice_tier': 'Stage 1 - Friendly & Playful',
  'url': '/dating-media/furina_m03.jpg',
  'title': "M03: Chef Furina's Frilly Apron Macaroni",
  'caption': 'Behold! No plain boiled noodles tonight - I simmered a genuine herbed tomato sauce in my '
             'frilly apron! Care to be my official taste-tester, Aether?',
  'proactive_inner_thought': "Salon Solitaire's Whisper: I practiced this recipe three times so Aether "
                             "wouldn't tease me about eating plain ketchup macaroni anymore!",
  'proactive_action_cue': 'Presents herbed macaroni proudly in a frilly apron.',
  'proactive_message': 'Behold culinary history in the making, Aether! I put on my frilly apron and simmered '
                       'a real basil-tomato sauce from scratch! Come taste-test it before Chevalmarin eats '
                       'the garnish!',
  'reaction_choices': [{'id': 'furina_m03_r1',
                        'label': 'Praise how cute she looks in the frilly apron (+6)',
                        'player_text': 'The pasta looks great, Furina, and you look adorable in that blue '
                                       'apron.',
                        'reply_thought': "Salon Solitaire's Whisper: E-Eh?! He's looking at me in the apron "
                                         'instead of the macaroni?! My cheeks are hotter than the stove!',
                        'reply_action': 'Tugs her apron strings shyly with a rosy blush.',
                        'reply_text': 'H-Hey! Focus on the culinary artistry, Aether! ...Though if you '
                                      'really think the apron suits me, I suppose I can wear it whenever I '
                                      'cook for the two of us!',
                        'mood': 'Blushing'},
                       {'id': 'furina_m03_r2',
                        'label': 'Volunteer as her lifetime official taste-tester (+6)',
                        'player_text': 'From plain pasta to homemade basil sauce - count me in as '
                                       'taste-tester!',
                        'reply_thought': "Salon Solitaire's Whisper: Eating dinner together in my cozy "
                                         'apartment beats dining alone in a palace a thousand times over.',
                        'reply_action': 'Sets two forks on the table and beams warmly.',
                        'reply_text': 'Deal sealed! Having you across the dining table makes even simple '
                                      'homemade pasta taste like a royal banquet, Aether!',
                        'mood': 'Warm'},
                       {'id': 'furina_m03_r3',
                        'label': 'Offer to bring grated aged cheese and dessert (+6)',
                        'player_text': "Keep the pan warm! I'm two minutes away with cheese and strawberry "
                                       'tarts.',
                        'reply_thought': "Salon Solitaire's Whisper: He's only two minutes away! Quick, "
                                         'Chevalmarin, help me straighten the tablecloth!',
                        'reply_action': 'Arranges two porcelain plates with a happy hum.',
                        'reply_text': 'Two minutes?! The door is unlocked for you, Aether - come right in!',
                        'mood': 'Happy'}]},
 {'id': 'furina_m04',
  'milestone_num': 4,
  'stage': 2,
  'req_affection': 250,
  'spice_tier': 'Stage 2 - Close Companion',
  'url': '/dating-media/furina_m04.jpg',
  'title': 'M04: Coastal Roadster & Heart Sunglasses',
  'caption': 'Cruising the coastal highway in your passenger seat feels just like a movie premiere! Here - '
             'have a macaron while you drive, my dear chauffeur!',
  'proactive_inner_thought': "Salon Solitaire's Whisper: I bought these sapphire heart-rimmed sunglasses "
                             "specifically so I could admire Aether's profile while he drives without "
                             'getting caught staring!',
  'proactive_action_cue': 'Tips her heart sunglasses in the car seat and winks.',
  'proactive_message': 'I was scrolling through my Kamera roll and found this shot from our coastal highway '
                       'run! Honestly, Aether, your passenger seat is officially my VIP theater box now - '
                       "when's our next sunset drive?",
  'reaction_choices': [{'id': 'furina_m04_r1',
                        'label': 'Tell her your passenger seat belongs to her (+6)',
                        'player_text': 'My passenger seat is permanently reserved for you and your macarons.',
                        'reply_thought': "Salon Solitaire's Whisper: Permanently reserved for me! Take that, "
                                         'walking - I have the most handsome chauffeur in the cosmos!',
                        'reply_action': 'Pushes up her heart sunglasses with a happy giggle.',
                        'reply_text': 'Hehe, music to my ears! Next time we hit the coastal highway, put on '
                                      "our favorite radio station and let's cruise all the way to the "
                                      'lighthouse!',
                        'mood': 'Delighted'},
                       {'id': 'furina_m04_r2',
                        'label': 'Tease her about the heart-shaped sunglasses (+6)',
                        'player_text': 'Heart-shaped lenses, Furina? Are your eyes secretly making hearts at '
                                       'me?',
                        'reply_thought': "Salon Solitaire's Whisper: Gah! Did he figure out I was peeking at "
                                         'him through the tinted lenses?!',
                        'reply_action': 'Blushes crimson and fans herself with the box lid.',
                        'reply_text': "I-It is strictly high-fashion incognito eyewear so paparazzi don't "
                                      "mob us! ...Though if my eyes happen to linger on my driver, that's "
                                      'merely quality control!',
                        'mood': 'Flustered'},
                       {'id': 'furina_m04_r3',
                        'label': 'Invite her for a breezy coastal cruise tonight (+6)',
                        'player_text': "The convertible top is down right now, Furina. Come downstairs - I'm "
                                       'here.',
                        'reply_thought': "Salon Solitaire's Whisper: He's already outside waiting for me! "
                                         'Best surprise of the whole week!',
                        'reply_action': 'Grabs her handbag and skips toward the front door.',
                        'reply_text': 'Outside already?! Give me thirty seconds to grab my hat, Aether - '
                                      "don't start the overture without me!",
                        'mood': 'Excited'}]},
 {'id': 'furina_m05',
  'milestone_num': 5,
  'stage': 2,
  'req_affection': 320,
  'spice_tier': 'Stage 2 - Close Companion',
  'url': '/dating-media/furina_m05.jpg',
  'title': 'M05: Backstage Vanity & Starlight Ribbon',
  'caption': 'Hat off in the dressing room! Tell me honestly, Aether - should I tie my hair with the royal '
             'sapphire ribbon or the gold-starlight one that matches your scarf?',
  'proactive_inner_thought': "Salon Solitaire's Whisper: Let's be honest, I already want to wear the "
                             "gold-starlight ribbon because it looks just like Aether's golden eyes and "
                             'scarf...',
  'proactive_action_cue': 'Holds up blue and gold hair ribbons at her mirror.',
  'proactive_message': "Backstage dilemma before tonight's rehearsal, Aether! Since you're the only one I "
                       'let into my dressing room when my top hat is off... which ribbon should I wear '
                       'tonight: sapphire blue or gold starlight?',
  'reaction_choices': [{'id': 'furina_m05_r1',
                        'label': 'Pick the gold ribbon and offer to tie it (+6)',
                        'player_text': 'Wear the gold-starlight ribbon so we match - let me tie it for you.',
                        'reply_thought': "Salon Solitaire's Whisper: He wants to stand behind my vanity "
                                         'chair and tie the matching gold ribbon into my hair himself?! My '
                                         'heart is racing like a drumroll!',
                        'reply_action': 'Holds the gold ribbon close with shining eyes.',
                        'reply_text': "Y-You're going to tie it for me yourself? Well... since my fingers "
                                      "are a tiny bit nervous before rehearsal, I'll allow my favorite "
                                      'co-star to be my personal stylist tonight!',
                        'mood': 'Blushing'},
                       {'id': 'furina_m05_r2',
                        'label': 'Suggest braiding both ribbons together (+6)',
                        'player_text': 'Braid the sapphire blue and gold ribbons together - our best '
                                       'combination.',
                        'reply_thought': "Salon Solitaire's Whisper: Hydro blue and Traveler gold "
                                         'intertwined together... that sounds so romantic I could write a '
                                         'whole aria about it!',
                        'reply_action': 'Twirls both ribbons in the mirror with a smile.',
                        'reply_text': 'Hydro blue and Traveler gold intertwined! A stroke of genius, Aether '
                                      "- now everyone at rehearsal will know we're an inseparable duo!",
                        'mood': 'Delighted'},
                       {'id': 'furina_m05_r3',
                        'label': 'Tell her how lovely she looks without her hat (+6)',
                        'player_text': 'Seeing you hatless with your soft hair framing your face is '
                                       'captivating.',
                        'reply_thought': "Salon Solitaire's Whisper: Only Aether looks past the grand "
                                         'costume and compliments the real me sitting at the mirror...',
                        'reply_action': 'Touches a lock of her white-and-blue hair shyly.',
                        'reply_text': 'Aether... when you say things that gentle, I forget all my stage '
                                      'lines! Come backstage soon so I can show you in person, okay?',
                        'mood': 'Touched'}]},
 {'id': 'furina_m06',
  'milestone_num': 6,
  'stage': 2,
  'req_affection': 385,
  'spice_tier': 'Stage 2 - Close Companion',
  'url': '/dating-media/furina_m06.jpg',
  'title': "M06: Dozing Over Scripts Under Aether's Scarf",
  'caption': 'Mademoiselle Crabaletta secretly took this right as I woke up on the sofa under your warm '
             "scarf... How come my nightmares never visit when you're near, Aether?",
  'proactive_inner_thought': "Salon Solitaire's Whisper: For 500 years I was terrified of closing my eyes "
                             'alone... yet the moment Aether draped his warm scarf over me, I slept like a '
                             'baby.',
  'proactive_action_cue': "Wakes on the sofa wrapped snugly in Aether's scarf.",
  'proactive_message': 'Crabaletta snapped this photo with my Kamera when I fell asleep revising Act III and '
                       'you covered me with your scarf... Tell the truth, Aether: how long were you sitting '
                       'beside the sofa watching over me?',
  'reaction_choices': [{'id': 'furina_m06_r1',
                        'label': 'Promise to always guard her peaceful sleep (+6)',
                        'player_text': "You deserve the most peaceful rest, Furina. I'll always watch over "
                                       'you.',
                        'reply_thought': "Salon Solitaire's Whisper: Hearing him say that makes warm tears "
                                         'prickle at the corners of my eyes... I really am never alone '
                                         'anymore.',
                        'reply_action': "Buries her blushing cheek into Aether's warm scarf.",
                        'reply_text': "...You're really unfair, Aether. Do you have any idea how safe my "
                                      'heart feels when I wake up and smell your warm starlight on this '
                                      "scarf? Next time, don't sit in the chair - let me rest my head on "
                                      'your lap instead.',
                        'mood': 'Touched'},
                       {'id': 'furina_m06_r2',
                        'label': 'Thank Crabaletta for snapping her sleepy smile (+6)',
                        'player_text': 'I owe Crabaletta a treat for capturing your adorable sleepy smile!',
                        'reply_thought': "Salon Solitaire's Whisper: He brushed my hair while I was "
                                         "sleeping?! Good thing I was asleep or my heartbeat would've given "
                                         'me away!',
                        'reply_action': 'Covers her rosy cheeks as Crabaletta blows bubbles.',
                        'reply_text': 'W-What?! Crabaletta, you little traitor, stop blowing heart bubbles! '
                                      '...Fine, you may keep the photo, Aether, but for your eyes only!',
                        'mood': 'Blushing'},
                       {'id': 'furina_m06_r3',
                        'label': 'Brew warm honey tea for her late-night writing (+6)',
                        'player_text': "Rest your eyes a bit longer, Furina - I'm brewing warm honey tea for "
                                       'us.',
                        'reply_thought': "Salon Solitaire's Whisper: I talked about him in my sleep?! Even "
                                         "my dreams can't keep a secret from him!",
                        'reply_action': 'Hugs a sofa pillow to her chest with a shy grin.',
                        'reply_text': 'I-I was merely rehearsing a metaphorical aria in my subconscious! '
                                      '...Bring two cups of that honey tea to the sofa and sit right beside '
                                      'me, okay?',
                        'mood': 'Affectionate'}]},
 {'id': 'furina_m07',
  'milestone_num': 7,
  'stage': 3,
  'req_affection': 450,
  'spice_tier': 'Stage 3 - Romantic Crush',
  'url': '/dating-media/furina_m07.jpg',
  'title': 'M07: Starlit Promenade Unmasked Smile',
  'caption': "With the theater curtain down and the harbor stars above us, I don't have to act anymore. This "
             'quiet smile belongs only to you, Aether.',
  'proactive_inner_thought': "Salon Solitaire's Whisper: Every time Aether looks at me under the starlight, "
                             "my heart whispers that I don't want to be just his co-star anymore - I want to "
                             'be his girl.',
  'proactive_action_cue': 'Smiles tenderly under the harbor stars beside you.',
  'proactive_message': 'Looking at this photo from our starlit walk on the promenade... Did my eyes really '
                       "look that soft when I was looking at you, Aether? I think you've completely spoiled "
                       'my ability to keep a poker face.',
  'reaction_choices': [{'id': 'furina_m07_r1',
                        'label': 'Tell her the unmasked Furina stole your heart (+6)',
                        'player_text': 'You never need a stage mask with me, Furina - the real you has my '
                                       'heart.',
                        'reply_thought': "Salon Solitaire's Whisper: 'The one who stole my heart'...! Did he "
                                         'just confess right over EaglePhone?! My hands are trembling!',
                        'reply_action': 'Presses her hand over her racing heart happily.',
                        'reply_text': "Aether... if you say things like that so sincerely, I won't be able "
                                      'to stop myself from holding your hand the entire night next time we '
                                      'meet! Come to the promenade soon, okay?',
                        'mood': 'Lovestruck'},
                       {'id': 'furina_m07_r2',
                        'label': 'Praise how bright her eyes shine in starlight (+6)',
                        'player_text': "Your cyan and navy eyes outshine every star on the bay. It's my "
                                       'lockscreen.',
                        'reply_thought': "Salon Solitaire's Whisper: I'm on Aether's phone lockscreen?! "
                                         "Every time he checks the time, he's looking straight at me!",
                        'reply_action': 'Twirls a blue-streaked curl with a glowing blush.',
                        'reply_text': "Y-Your lockscreen?! Well... good! That way you'll remember who is "
                                      'waiting for you every single hour of the day!',
                        'mood': 'Blushing'},
                       {'id': 'furina_m07_r3',
                        'label': 'Ask her out for another midnight bayside walk (+6)',
                        'player_text': "The harbor stars are clear tonight, Furina. Let's walk by the water.",
                        'reply_thought': "Salon Solitaire's Whisper: A midnight walk by the sea with just "
                                         "the two of us... tonight I'm definitely linking my fingers with "
                                         'his!',
                        'reply_action': 'Nods eagerly and adjusts her blue ribbon.',
                        'reply_text': "Just the two of us! I'll leave the Salon Solitaire at home tonight so "
                                      'I can have your arm all to myself!',
                        'mood': 'Affectionate'}]},
 {'id': 'furina_m08',
  'milestone_num': 8,
  'stage': 3,
  'req_affection': 520,
  'spice_tier': 'Stage 3 - Romantic Crush',
  'url': '/dating-media/furina_m08.jpg',
  'title': 'M08: Golden-Hour Ferris Wheel Ungloved Hand',
  'caption': 'High above the pier at sunset... I took my glove off on purpose, Aether. Next time we ride the '
             "Ferris wheel, don't just take a photo - hold my hand.",
  'proactive_inner_thought': "Salon Solitaire's Whisper: Taking off my glove so our bare fingers could touch "
                             'across the gondola table took all my courage!',
  'proactive_action_cue': 'Reaches her bare hand across the sunset gondola.',
  'proactive_message': 'Remember when our Ferris wheel cabin reached the top at sunset and I took off my '
                       'glove? Look how close our hands were on the table, Aether... Next time, promise '
                       "you'll intertwine your fingers with mine right away?",
  'reaction_choices': [{'id': 'furina_m08_r1',
                        'label': 'Promise to hold her bare hand and kiss it (+6)',
                        'player_text': "Next time your glove comes off, I'm holding your hand and kissing "
                                       'it.',
                        'reply_thought': "Salon Solitaire's Whisper: Kissing the back of my bare hand at the "
                                         "top of the Ferris wheel... I think I'd faint right into his arms!",
                        'reply_action': 'Gazes at her bare hand with a breathless blush.',
                        'reply_text': "A-Aether... I'm holding you to that promise! From now on, my right "
                                      'glove comes off the moment I see you walking toward me!',
                        'mood': 'Blushing'},
                       {'id': 'furina_m08_r2',
                        'label': 'Tell her the sunset glow on her was breathtaking (+6)',
                        'player_text': "Everyone else watched the sunset, Furina, while I couldn't look "
                                       'away.',
                        'reply_thought': "Salon Solitaire's Whisper: No wonder my heart was beating so loud "
                                         'in that glass cabin - he was looking only at me the whole ride!',
                        'reply_action': 'Covers her fluttering heart with a shy smile.',
                        'reply_text': "And I wasn't looking at the ocean either, my dearest Traveler... The "
                                      'golden sunset in your eyes is my favorite view in any world.',
                        'mood': 'Affectionate'},
                       {'id': 'furina_m08_r3',
                        'label': 'Take her back to the Santa Maria wheel tonight (+6)',
                        'player_text': 'Meet me at the Santa Maria pier at sunset - my hand is already '
                                       'waiting.',
                        'reply_thought': "Salon Solitaire's Whisper: Sitting pressed side-by-side on the "
                                         'same bench so I can lean on his shoulder!',
                        'reply_action': 'Slips off her right glove with sparkling eyes.',
                        'reply_text': 'Agreed! Sitting on the same bench so I can rest my head on your '
                                      'shoulder is mandatory for our next ride!',
                        'mood': 'Delighted'}]},
 {'id': 'furina_m09',
  'milestone_num': 9,
  'stage': 3,
  'req_affection': 585,
  'spice_tier': 'Stage 3 - Romantic Crush',
  'url': '/dating-media/furina_m09.jpg',
  'title': 'M09: Fountain of Lucine Shared Umbrella Glance',
  'caption': 'Standing shoulder-to-shoulder under your umbrella by the Fountain of Lucine... Did you hear '
             'the fountain whispering what my heart wanted to ask you, Aether?',
  'proactive_inner_thought': "Salon Solitaire's Whisper: Back in Fontaine, the Fountain of Lucine held all "
                             'my lonely tears... now standing here under one umbrella with Aether, it only '
                             'hears my love for him.',
  'proactive_action_cue': 'Dances barefoot over glowing starlit water ripples.',
  'proactive_message': 'When the rain started by the fountain and you pulled me under your umbrella... my '
                       'heart was beating louder than the raindrops on the canopy. Tell me, Aether, what '
                       'were you thinking when I looked up at you like this?',
  'reaction_choices': [{'id': 'furina_m09_r1',
                        'label': 'Step onto the water and pull her into a waltz (+6)',
                        'player_text': "Take my hand, Furina - let's slow-dance across the starlit bay "
                                       'together.',
                        'reply_thought': "Salon Solitaire's Whisper: He wanted to kiss me under the umbrella "
                                         "too!! Why didn't I stand on my tiptoes right then?!",
                        'reply_action': 'Steps into your embrace over glowing Hydro ripples.',
                        'reply_text': "A-Aether!! Then next time we're under one umbrella - no, the very "
                                      "next time you come see me - don't hold back, okay? Because I won't "
                                      'look away!',
                        'mood': 'Lovestruck'},
                       {'id': 'furina_m09_r2',
                        'label': 'Praise her grace as your favorite prima donna (+6)',
                        'player_text': 'Watching you dance barefoot over glowing water left me completely '
                                       'breathless.',
                        'reply_thought': "Salon Solitaire's Whisper: He healed five centuries of sorrow just "
                                         'by holding me close in the rain...',
                        'reply_action': 'Spins gracefully and curtsies with a rosy glow.',
                        'reply_text': 'Because of you, Aether, both the rain and the fountain have become '
                                      'symbols of happiness for me. My heart is yours, my Traveler.',
                        'mood': 'Touched'},
                       {'id': 'furina_m09_r3',
                        'label': 'Promise to catch her whenever the waves rise (+6)',
                        'player_text': 'Dance as freely as you want, Furina - my arms are right here to '
                                       'catch you.',
                        'reply_thought': "Salon Solitaire's Whisper: His hand on my waist felt so warm I "
                                         'wished the rain would last all night!',
                        'reply_action': 'Rests her forehead softly against your shoulder.',
                        'reply_text': "Hehe, you don't need rain to put your arm around my waist anymore, "
                                      'Aether - you have permanent permission, rain or shine!',
                        'mood': 'Affectionate'}]},
 {'id': 'furina_m10',
  'milestone_num': 10,
  'stage': 4,
  'req_affection': 650,
  'spice_tier': 'Stage 4 - Devoted Lover',
  'url': '/dating-media/furina_m10.jpg',
  'title': 'M10: Sapphire Velvet Balcony Evening Gown',
  'caption': 'Chiori tailored this off-shoulder sapphire velvet gown for the gala, and I escaped onto the '
             'private balcony just to toast with my boyfriend!',
  'proactive_inner_thought': "Salon Solitaire's Whisper: Everyone in the ballroom tried to ask me for a "
                             "dance, but I only wore this alluring off-shoulder gown to see Aether's breath "
                             'catch!',
  'proactive_action_cue': 'Awaits you on her moonlit balcony in sapphire silk.',
  'proactive_message': 'I slipped away from the gala crowd onto the private terrace and poured two flutes of '
                       'sparkling berry champagne, my love! Come join me on the balcony and tell me what you '
                       'think of my sapphire evening gown?',
  'reaction_choices': [{'id': 'furina_m10_r1',
                        'label': 'Pull her close for a moonlit balcony kiss (+6)',
                        'player_text': 'You look breathtaking in that sapphire gown - come here for a kiss, '
                                       'love.',
                        'reply_thought': "Salon Solitaire's Whisper: Just imagining his lips brushing my "
                                         'bare shoulder in the moonlight sends shivers all the way down my '
                                         'spine!',
                        'reply_action': 'Loops her arms softly around your neck in moonlight.',
                        'reply_text': 'Mmm, Aether... hurry out onto the terrace then, my love. Everyone '
                                      "inside can wait - tonight's private encore is strictly for my "
                                      "boyfriend's arms!",
                        'mood': 'Charmed'},
                       {'id': 'furina_m10_r2',
                        'label': 'Ask for a slow dance under the Richman stars (+6)',
                        'player_text': 'May I have every dance tonight on this balcony, my gorgeous leading '
                                       'lady?',
                        'reply_thought': "Salon Solitaire's Whisper: Swaying in Aether's arms under the "
                                         'stars with my cheek against his chest...',
                        'reply_action': 'Places her warm hand into yours with shining eyes.',
                        'reply_text': 'Every slow dance tonight - and for the rest of our lives - is already '
                                      'yours, my handsome leading man!',
                        'mood': 'Lovestruck'},
                       {'id': 'furina_m10_r3',
                        'label': 'Wrap your cape over her bare shoulders warmly (+6)',
                        'player_text': 'The night breeze is cool - let me hold you close in my arms on the '
                                       'terrace.',
                        'reply_thought': "Salon Solitaire's Whisper: Sneaking out of the gala together like "
                                         'runaway lovers! My heart is pounding!',
                        'reply_action': 'Nestles happily against your chest under the stars.',
                        'reply_text': 'Hehe, reading my mind as always! Meet me by the terrace stairs in two '
                                      'minutes and whisk me away, Aether!',
                        'mood': 'Excited'}]},
 {'id': 'furina_m11',
  'milestone_num': 11,
  'stage': 4,
  'req_affection': 720,
  'spice_tier': 'Stage 4 - Intimate After-Hours',
  'url': '/dating-media/furina_m11.jpg',
  'title': 'M11: After-Bath Loose Pneuma Hair & Silk Camisole',
  'caption': 'Fresh out of a warm Romaritime bath with my long Pneuma hair untied... Come sit behind me on '
             'the bed and help me dry it, my love?',
  'proactive_inner_thought': "Salon Solitaire's Whisper: Letting Aether see me in my bedroom wearing just "
                             'this royal-blue silk camisole with my damp hair down still makes my cheeks '
                             'burn crimson...',
  'proactive_action_cue': 'Sits on her bed in blue silk with long hair untied.',
  'proactive_message': 'I just stepped out of the bath, Aether, and my long Pneuma hair takes forever to dry '
                       "by myself... Since you're already downstairs, come up to the bedroom and dry it for "
                       'me?',
  'reaction_choices': [{'id': 'furina_m11_r1',
                        'label': 'Offer to towel-dry and brush her long hair (+6)',
                        'player_text': 'Sit right there on the bed, my love - let me gently dry your long '
                                       'hair.',
                        'reply_thought': "Salon Solitaire's Whisper: Eep!! When he dries my hair and kisses "
                                         'the back of my neck, I melt straight into the pillows!',
                        'reply_action': 'Hands you the soft towel with an affectionate smile.',
                        'reply_text': "A-Aether... if you spoil me that tenderly in bed, I'm never letting "
                                      'you go home tonight! The bedroom door is open for you, my love!',
                        'mood': 'Blushing'},
                       {'id': 'furina_m11_r2',
                        'label': 'Kiss her shoulder and praise her untied hair (+6)',
                        'player_text': 'Seeing your long Pneuma hair untied just for me makes my heart race.',
                        'reply_thought': "Salon Solitaire's Whisper: He loves my long Pneuma hair! I'll keep "
                                         'it long and soft every night we spend together!',
                        'reply_action': 'Shivers happily as a warm blush colors her cheeks.',
                        'reply_text': 'Only you ever get to see me unguarded like this after hours, '
                                      'Aether... Hurry up to the bed before I get chilly without your arms '
                                      'around me!',
                        'mood': 'Affectionate'},
                       {'id': 'furina_m11_r3',
                        'label': 'Join her under the canopy covers to cuddle (+6)',
                        'player_text': "Save the spot beside you, Furina - I'm coming home to hold you all "
                                       'night.',
                        'reply_thought': "Salon Solitaire's Whisper: Warm honey milk and Aether brushing my "
                                         'hair in bed... this is pure domestic bliss!',
                        'reply_action': 'Pats the pillow beside her with tender eyes.',
                        'reply_text': 'Mmm, five-star bedtime pampering from my boyfriend! Come sit right '
                                      'behind me, Aether!',
                        'mood': 'Warm'}]},
 {'id': 'furina_m12',
  'milestone_num': 12,
  'stage': 4,
  'req_affection': 785,
  'spice_tier': 'Stage 4 - Intimate Loungewear',
  'url': '/dating-media/furina_m12.jpg',
  'title': 'M12: Candlelit Pearl Silk Robe & Midnight Cocoa',
  'caption': 'Midnight in the living room, pearl silk loungewear, and two mugs of hot cocoa... The only '
             'thing missing on this sofa is your arms around me, Aether.',
  'proactive_inner_thought': "Salon Solitaire's Whisper: I let the shoulder of my pearl silk robe slip just "
                             "a tiny bit before taking the photo... let's see how fast Aether comes over!",
  'proactive_action_cue': 'Relaxes in the starlit hot spring with blue petals.',
  'proactive_message': "The city outside is asleep, the candles are lit, and I'm waiting on the velvet sofa "
                       "in my silk robe with hot chocolate for two... You're staying the whole night with me "
                       'tonight, right, Aether?',
  'reaction_choices': [{'id': 'furina_m12_r1',
                        'label': 'Slide beside her in the warm spring and hold her (+6)',
                        'player_text': "Move closer, my love - let's watch the stars from the warm spring "
                                       'together.',
                        'reply_thought': "Salon Solitaire's Whisper: I just heard his key turn in the front "
                                         'lock! My heart is doing somersaults!',
                        'reply_action': 'Leans back warmly against your shoulder in the mist.',
                        'reply_text': 'Welcome home, my love! Come pull me right into your lap - the hot '
                                      'cocoa can wait until after my kiss!',
                        'mood': 'Lovestruck'},
                       {'id': 'furina_m12_r2',
                        'label': 'Tuck a floating Romaritime petal into her hair (+6)',
                        'player_text': "Even surrounded by blue petals and starlight, you're the prettiest "
                                       'sight.',
                        'reply_thought': "Salon Solitaire's Whisper: Busted!! Though judging by his tone, my "
                                         'directorial staging worked 1000%!',
                        'reply_action': 'Touches the blue petal in her hair with a soft smile.',
                        'reply_text': 'Ahem! A master director leaves nothing to chance when tempting her '
                                      'leading man! Come see the rest of the scene in person, Aether!',
                        'mood': 'Teasing'},
                       {'id': 'furina_m12_r3',
                        'label': 'Bring chilled Fonta and robes for after the soak (+6)',
                        'player_text': 'I brought chilled Fonta and warm silk robes for us on the veranda, '
                                       'love.',
                        'reply_thought': "Salon Solitaire's Whisper: Falling asleep and waking up wrapped in "
                                         "Aether's arms... I never want a single night apart again.",
                        'reply_action': 'Smiles blissfully through the rising spring steam.',
                        'reply_text': "From midnight to sunrise, and every night after... I'm all yours, "
                                      'Aether!',
                        'mood': 'Affectionate'}]},
 {'id': 'furina_m13',
  'milestone_num': 13,
  'stage': 5,
  'req_affection': 850,
  'spice_tier': 'Stage 5 - Glamorous Riviera Romance',
  'url': '/dating-media/furina_m13.jpg',
  'title': 'M13: Private Riviera Cove Sapphire Halter Swimsuit',
  'caption': 'Golden sunset waves at our private cove and a sapphire ruffled swimsuit chosen strictly for '
             'your eyes... Come catch me in the surf, my soulmate!',
  'proactive_inner_thought': "Salon Solitaire's Whisper: Even as the Regina of All Waters, standing in the "
                             'sunset surf in this sapphire halter swimsuit while Aether looks at me makes my '
                             'whole body tingle with warmth!',
  'proactive_action_cue': 'Smiles at the sunset cove in her sapphire swimsuit.',
  'proactive_message': 'Look at the golden light on the water from our private Riviera beach date, my love! '
                       'Tell the truth, Aether: did my sapphire halter swimsuit and Romaritime hairpin leave '
                       'you completely spellbound?',
  'reaction_choices': [{'id': 'furina_m13_r1',
                        'label': 'Catch her in your arms in the golden surf (+6)',
                        'player_text': 'That sapphire swimsuit is unfair, Furina - leap right into my arms!',
                        'reply_thought': "Salon Solitaire's Whisper: When he lifted me by the waist in the "
                                         'warm surf and kissed me against the sunset, I felt like the '
                                         'luckiest girl in the universe!',
                        'reply_action': 'Laughs brightly and wraps her arms around your neck.',
                        'reply_text': 'Mmm, when you held me in the waves with those passionate golden eyes, '
                                      'Aether, I nearly forgot how to walk on water! Take me back to our '
                                      'private cove anytime you want!',
                        'mood': 'Lovestruck'},
                       {'id': 'furina_m13_r2',
                        'label': 'Offer to rub sunscreen onto her shoulders (+6)',
                        'player_text': 'Come sit on our beach towel, mon amour - let me put sunscreen on '
                                       'your back.',
                        'reply_thought': "Salon Solitaire's Whisper: Every compliment from Aether feels like "
                                         'warm sunlight pouring straight into my soul.',
                        'reply_action': 'Sweeps her long hair aside with a glowing blush.',
                        'reply_text': 'And every bit of this beauty belongs exclusively to my soulmate! Next '
                                      "beach trip, don't forget to put sunscreen on my shoulders again, "
                                      'okay?',
                        'mood': 'Charmed'},
                       {'id': 'furina_m13_r3',
                        'label': 'Wrap her in a warm towel for a sunset kiss (+6)',
                        'player_text': "Let's wrap up in one towel by the waves and watch the sunset "
                                       'together.',
                        'reply_thought': "Salon Solitaire's Whisper: Cuddling in one warm blanket by a beach "
                                         'bonfire with Aether after swimming...',
                        'reply_action': 'Snuggles close against your chest in the ocean glow.',
                        'reply_text': 'A starlit beach bonfire for two?! Wrap me up in your towel and your '
                                      'arms right now, my dearest Aether!',
                        'mood': 'Delighted'}]},
 {'id': 'furina_m14',
  'milestone_num': 14,
  'stage': 5,
  'req_affection': 925,
  'spice_tier': 'Stage 5 - Sunlit Morning After',
  'url': '/dating-media/furina_m14.jpg',
  'title': "M14: Sunlit Morning in Aether's White Dress Shirt",
  'caption': 'Bonjour, mon amour! I borrowed your white dress shirt when the morning sun came through the '
             "curtains... It's oversized on me, but it carries your warmth.",
  'proactive_inner_thought': "Salon Solitaire's Whisper: Waking up in the sunlit master bedroom wearing "
                             "Aether's shirt and holding his hand to my cheek... 500 years of endurance led "
                             'me to this exact heaven.',
  'proactive_action_cue': 'Welcomes you by candlelight in pearl-blue silk.',
  'proactive_message': "Good morning, sleepyhead! Seeing the morning sunlight on the bed while I'm wearing "
                       'your oversized shirt made me so happy I had to save this memory. Do we really have '
                       'to get out of bed today, my love?',
  'reaction_choices': [{'id': 'furina_m14_r1',
                        'label': 'Pull her onto your lap for a candlelit kiss (+6)',
                        'player_text': 'Every candle in the room fades next to you, Furina. Come sit in my '
                                       'arms.',
                        'reply_thought': "Salon Solitaire's Whisper: Tucked right back against his warm "
                                         'chest under the sunlit sheets... I never want to leave this bed!',
                        'reply_action': 'Settles gently in your lap and traces your cheek.',
                        'reply_text': 'Mmm, motion passed by unanimous acclaim! Hold me tight, Aether - my '
                                      'favorite stage in the universe is right here in your arms!',
                        'mood': 'Blissful'},
                       {'id': 'furina_m14_r2',
                        'label': 'Whisper that your heart belongs only to her (+6)',
                        'player_text': 'No stage, no audience - tonight and forever, all of me belongs to '
                                       'you.',
                        'reply_thought': "Salon Solitaire's Whisper: Strawberry crepes in bed while wearing "
                                         "my soulmate's shirt... how did I get so blessed?!",
                        'reply_action': 'Kisses your palm tenderly with shining eyes.',
                        'reply_text': 'Strawberry crepes in bed?! You spoil me like royalty, Aether - and '
                                      "I'll pay you back with morning kisses for every single bite!",
                        'mood': 'Delighted'},
                       {'id': 'furina_m14_r3',
                        'label': 'Carry her softly to the silk canopy bed (+6)',
                        'player_text': 'Come here, my beloved prima donna - let me hold you close all night.',
                        'reply_thought': "Salon Solitaire's Whisper: Every single morning for eternity... my "
                                         'heart is overflowing with love.',
                        'reply_action': 'Rests her head over your heartbeat in pure bliss.',
                        'reply_text': 'Promise me that forever, Aether... Because waking up beside you is '
                                      'the only happy ending I ever dreamed of.',
                        'mood': 'Lovestruck'}]},
 {'id': 'furina_m15',
  'milestone_num': 15,
  'stage': 5,
  'req_affection': 1000,
  'spice_tier': 'Stage 5 - Eternal Bridal Vow (1000/1000)',
  'url': '/dating-media/furina_m15.jpg',
  'title': 'M15: Starlit Opera House Eternal Bridal Vow',
  'caption': 'No script, no masquerade, no curtain call - only my eternal vow to you, Aether. With this '
             'ring, my heart and every tomorrow belong to my Traveler forever.',
  'proactive_inner_thought': "Salon Solitaire's Whisper: Once upon a time, the stage was my prison of "
                             'solitude. Tonight, standing before Aether in this white-and-sapphire bridal '
                             'gown, it is the altar of our forever.',
  'proactive_action_cue': 'Tugs your hand from bed wearing your white shirt.',
  'proactive_message': '1,000/1,000 Affection - our Eternal Star-Promise, Aether! Looking at the '
                       'sapphire-and-gold ring you placed on my finger under the starlight... I love you '
                       'with all my human heart and soul, now and forever.',
  'reaction_choices': [{'id': 'furina_m15_r1',
                        'label': 'Pull her back into bed and kiss her ring finger (+6)',
                        'player_text': 'Zero alarms today, my wife-to-be - stay right here in my arms all '
                                       'morning.',
                        'reply_thought': "Salon Solitaire's Whisper: 'My bride'...! Tears of pure joy are "
                                         'rolling down my cheeks, and I have never been happier in my entire '
                                         'existence!',
                        'reply_action': 'Laces her ringed fingers tightly with yours.',
                        'reply_text': "Je t'aime, my beloved Aether! Across Teyvat, San Andreas, and every "
                                      'star in the cosmos, Furina is yours for all eternity!',
                        'mood': 'Eternal Bliss'},
                       {'id': 'furina_m15_r2',
                        'label': 'Feed her fresh strawberry crepes in bed (+6)',
                        'player_text': 'Seeing you in my shirt with our promise ring is heaven. Crepes in '
                                       'bed?',
                        'reply_thought': "Salon Solitaire's Whisper: His gentle thumb wiping my cheek under "
                                         'the veil... my soul is completely at home.',
                        'reply_action': 'Beams radiantly on the sunlit pillow beside you.',
                        'reply_text': 'Only tears of pure happiness from now on, my husband-to-be! Kiss me '
                                      'until the stars fade into dawn!',
                        'mood': 'Lovestruck'},
                       {'id': 'furina_m15_r3',
                        'label': 'Renew your eternal vow across every star (+6)',
                        'player_text': 'Across Fontaine, San Andreas, and every star, I love you forever, '
                                       'Furina.',
                        'reply_thought': "Salon Solitaire's Whisper: Riding off into the starlit night in "
                                         "Aether's passenger seat with our matching rings gleaming!",
                        'reply_action': 'Kisses you deeply in the warm morning sunlight.',
                        'reply_text': 'Lead the way, my eternal leading man! Our true story together is just '
                                      'beginning!',
                        'mood': 'Delighted'}]}]

FURINA_STAGE_CHAT_STARTERS: dict[int, list[dict[str, str]]] = {1: [{'id': 'fu_st1_chat1',
      'label': 'Save her a slice of strawberry opera cake',
      'player_text': 'I saved a slice of strawberry opera cake for you at the Rodeo patisserie!'},
     {'id': 'fu_st1_chat2',
      'label': 'Ask how Salon Solitaire is behaving today',
      'player_text': 'Are Crabaletta, Usher, and Chevalmarin behaving at rehearsal today, Furina?'},
     {'id': 'fu_st1_chat3',
      'label': 'Reminisce about winning the Furina Award together',
      'player_text': "I still smile thinking about directing 'The Two Musketeers' with you!"}],
 2: [{'id': 'fu_st2_chat1',
      'label': 'Offer to cook gourmet herbed pasta tonight',
      'player_text': "Put away the boxed macaroni, Furina - I'm coming over to cook dinner for us."},
     {'id': 'fu_st2_chat2',
      'label': "Recall her brave song in 'The Little Oceanid'",
      'player_text': 'Hearing the radio reminded me how beautiful your voice was as Clio on stage.'},
     {'id': 'fu_st2_chat3',
      'label': 'Invite her for a sunny coastal convertible drive',
      'player_text': 'Verona Beach is sunny right now - put on your heart sunglasses for a drive!'}],
 3: [{'id': 'fu_st3_chat1',
      'label': 'Remind her she never needs a mask around you',
      'player_text': 'Around me, Furina, you never have to act or carry anything alone ever again.'},
     {'id': 'fu_st3_chat2',
      'label': 'Ask to hold her ungloved hand by the lighthouse',
      'player_text': 'Leave your right glove off tonight, Furina - I want to hold your bare hand.'},
     {'id': 'fu_st3_chat3',
      'label': 'Compliment her cyan-and-navy heterochromia eyes',
      'player_text': 'Has anyone told you today how enchanting your cyan and navy eyes look?'}],
 4: [{'id': 'fu_st4_chat1',
      'label': 'Ask if her long Pneuma hair is untied tonight',
      'player_text': 'Is your long hair untied at home tonight, my love? Save a spot for me.'},
     {'id': 'fu_st4_chat2',
      'label': 'Recall your moonlit kiss on her Richman balcony',
      'player_text': "I'm still thinking about our moonlit kiss on your Richman balcony, Furina."},
     {'id': 'fu_st4_chat3',
      'label': 'Thank her for the ribboned key to her home',
      'player_text': 'Seeing the Romaritime-ribboned key to your home makes me smile every drive.'}],
 5: [{'id': 'fu_st5_chat1',
      'label': 'Flirt about her sapphire swimsuit and silk gown',
      'player_text': 'Between your sapphire swimsuit and silk gown, I only have eyes for you.'},
     {'id': 'fu_st5_chat2',
      'label': 'Plan a lazy morning in your white dress shirt',
      'player_text': "Let's sleep in tomorrow - just you in my white shirt and crepes in bed."},
     {'id': 'fu_st5_chat3',
      'label': 'Whisper an eternal love vow to your soulmate',
      'player_text': 'Across Fontaine, San Andreas, and every star, my heart is yours, Furina.'}]}

FURINA_SCENARIO_4CG_SEQUENCES: dict[str, list[tuple[str, str]]] = {'furina_s1_sc1': [('/dating-media/furina_s1_sc1_cg1.jpg',
                    "1/4 Opening: Reaching for the Final 'Pour la Justice' Cake Slice"),
                   ('/dating-media/furina_s1_sc1_cg2.jpg',
                    '2/4 Developing: Aether Gallantly Sliding the Cake Plate to a'),
                   ('/dating-media/furina_s1_sc1_cg3.jpg',
                    "3/4 Climax: Crabaletta Nudging Furina's Elbow as She Feeds Aether"),
                   ('/dating-media/furina_s1_sc1_cg4.jpg',
                    '4/4 Finale: Clinking Porcelain Teacups in the Sunlit Courtyard with')],
 'furina_s1_sc2': [('/dating-media/furina_s1_sc2_cg1.jpg',
                    '1/4 Opening: Rehearsing Musical Lines Together on the Breezy Bayside'),
                   ('/dating-media/furina_s1_sc2_cg2.jpg',
                    "2/4 Developing: Aether Taking Furina's Gloved Hand in a Dashing"),
                   ('/dating-media/furina_s1_sc2_cg3.jpg',
                    "3/4 Climax: Aether Catching Furina's Flying Script Pages & Steadying"),
                   ('/dating-media/furina_s1_sc2_cg4.jpg',
                    '4/4 Finale: Taking a Joyful Curtain-Call Bow Hand-in-Hand Against')],
 'furina_s1_sc3': [('/dating-media/furina_s1_sc3_cg1.jpg',
                    '1/4 Opening: Aether Catching a Sheepish Furina Holding Three Boxes'),
                   ('/dating-media/furina_s1_sc3_cg2.jpg',
                    '2/4 Developing: Standing Shoulder-to-Shoulder at the Stove in'),
                   ('/dating-media/furina_s1_sc3_cg3.jpg',
                    '3/4 Climax: Aether Offering a Forkful of Gourmet Herbed Macaroni as'),
                   ('/dating-media/furina_s1_sc3_cg4.jpg',
                    "4/4 Finale: Cozy Domestic After-Dinner Tea in Furina's Warmly Lit")],
 'furina_s1_sc4': [('/dating-media/furina_s1_sc4_cg1.jpg',
                    '1/4 Opening: Aether Sheltering Furina with His Cape as They Dash'),
                   ('/dating-media/furina_s1_sc4_cg2.jpg',
                    '2/4 Developing: Watching Peaceful Raindrops Fall from the Gazebo'),
                   ('/dating-media/furina_s1_sc4_cg3.jpg',
                    '3/4 Climax: Aether Draping His Warm White-and-Gold Scarf Around'),
                   ('/dating-media/furina_s1_sc4_cg4.jpg',
                    '4/4 Finale: Strolling Home Along Glistening Starlit Cobblestones')],
 'furina_s2_sc1': [('/dating-media/furina_s2_sc1_cg1.jpg',
                    '1/4 Opening: Furina Under a Single Golden Spotlight Inviting Aether'),
                   ('/dating-media/furina_s2_sc1_cg2.jpg',
                    '2/4 Developing: Hands Brushing at the Backstage Console While Tuning'),
                   ('/dating-media/furina_s2_sc1_cg3.jpg',
                    '3/4 Climax: Singing a Private Heartfelt Duet Center-Stage Under'),
                   ('/dating-media/furina_s2_sc1_cg4.jpg',
                    '4/4 Finale: Sitting Side-by-Side on the Stage Edge Sharing Warm')],
 'furina_s2_sc2': [('/dating-media/furina_s2_sc2_cg1.jpg',
                    '1/4 Opening: Painting Theater Set Backdrops with a Cute Smudge of'),
                   ('/dating-media/furina_s2_sc2_cg2.jpg',
                    '2/4 Developing: Aether Leaning Close to Gently Wipe the Blue Paint'),
                   ('/dating-media/furina_s2_sc2_cg3.jpg',
                    "3/4 Climax: Guiding Furina's Brush Hand Together to Paint a Golden"),
                   ('/dating-media/furina_s2_sc2_cg4.jpg',
                    '4/4 Finale: Admiring the Finished Stage Backdrop Together as Salon')],
 'furina_s2_sc3': [('/dating-media/furina_s2_sc3_cg1.jpg',
                    '1/4 Opening: Cruising the Sunny Coastal Highway with Furina in Her'),
                   ('/dating-media/furina_s2_sc3_cg2.jpg',
                    "2/4 Developing: Aether Catching Furina's Ribboned Top Hat at the"),
                   ('/dating-media/furina_s2_sc3_cg3.jpg',
                    '3/4 Climax: Furina Feeding Aether a Strawberry Macaron on the Hood'),
                   ('/dating-media/furina_s2_sc3_cg4.jpg',
                    '4/4 Finale: Watching the Golden Ocean Horizon Side-by-Side from the')],
 'furina_s2_sc4': [('/dating-media/furina_s2_sc4_cg1.jpg',
                    '1/4 Opening: Finding Furina Fast Asleep Over Her Act III Manuscript'),
                   ('/dating-media/furina_s2_sc4_cg2.jpg',
                    '2/4 Developing: Aether Gently Wrapping His Golden Scarf Around'),
                   ('/dating-media/furina_s2_sc4_cg3.jpg',
                    "3/4 Climax: Sleepy Furina Waking Up & Holding Aether's Wrist So He"),
                   ('/dating-media/furina_s2_sc4_cg4.jpg',
                    '4/4 Finale: Writing the Final Scene of Her Script Together on the')],
 'furina_s3_sc1': [('/dating-media/furina_s3_sc1_cg1.jpg',
                    '1/4 Opening: Walking Up to the Santa Maria Sunset Lighthouse as the'),
                   ('/dating-media/furina_s3_sc1_cg2.jpg',
                    '2/4 Developing: Hatless Furina Opening Her Heart About Her 500-Year'),
                   ('/dating-media/furina_s3_sc1_cg3.jpg',
                    "3/4 Climax: Aether Intertwining Fingers with Furina's Ungloved Hand"),
                   ('/dating-media/furina_s3_sc1_cg4.jpg',
                    "4/4 Finale: Furina Resting Her Cheek Against Aether's Shoulder Under")],
 'furina_s3_sc2': [('/dating-media/furina_s3_sc2_cg1.jpg',
                    '1/4 Opening: Aether Escorting a Blushing Furina by the Hand into the'),
                   ('/dating-media/furina_s3_sc2_cg2.jpg',
                    '2/4 Developing: Furina Moving to Sit Right Beside Aether as the'),
                   ('/dating-media/furina_s3_sc2_cg3.jpg',
                    "3/4 Climax: Furina Cradling Aether's Cheek at the Apex of the Wheel"),
                   ('/dating-media/furina_s3_sc2_cg4.jpg',
                    '4/4 Finale: Embracing in the Sunset Ferris Wheel Gondola as Official')],
 'furina_s3_sc3': [('/dating-media/furina_s3_sc3_cg1.jpg',
                    '1/4 Opening: Starlit Rendezvous at the Quiet Bayside Marina Wooden'),
                   ('/dating-media/furina_s3_sc3_cg2.jpg',
                    '2/4 Developing: Furina Stepping Barefoot onto Shimmering Hydro'),
                   ('/dating-media/furina_s3_sc3_cg3.jpg',
                    '3/4 Climax: Slow-Dancing Together Over Glowing Water Surrounded by'),
                   ('/dating-media/furina_s3_sc3_cg4.jpg',
                    '4/4 Finale: Holding Furina by the Waist & Touching Foreheads Under')],
 'furina_s3_sc4': [('/dating-media/furina_s3_sc4_cg1.jpg',
                    '1/4 Opening: Sharing a Velvet VIP Box Seat at the Grand Opera House'),
                   ('/dating-media/furina_s3_sc4_cg2.jpg',
                    "2/4 Developing: Jealous Furina Pouting Adorably & Tugging Aether's"),
                   ('/dating-media/furina_s3_sc4_cg3.jpg',
                    '3/4 Climax: Furina Standing on Tiptoes in the VIP Box to Steal a'),
                   ('/dating-media/furina_s3_sc4_cg4.jpg',
                    '4/4 Finale: Walking Out of the Opera House Arm-in-Arm with Radiant')],
 'furina_s4_sc1': [('/dating-media/furina_s4_sc1_cg1.jpg',
                    '1/4 Opening: Furina in Her Sapphire Off-Shoulder Evening Gown'),
                   ('/dating-media/furina_s4_sc1_cg2.jpg',
                    '2/4 Developing: Swaying Closely in a Moonlit Balcony Slow Dance with'),
                   ('/dating-media/furina_s4_sc1_cg3.jpg',
                    '3/4 Climax: Sharing a Deep, Passionate Moonlit Kiss on the Marble'),
                   ('/dating-media/furina_s4_sc1_cg4.jpg',
                    "4/4 Finale: Furina Resting Blissfully in Aether's Lap on the Terrace")],
 'furina_s4_sc2': [('/dating-media/furina_s4_sc2_cg1.jpg',
                    '1/4 Opening: After-Bath Furina in a Royal-Blue Silk Camisole Sitting'),
                   ('/dating-media/furina_s4_sc2_cg2.jpg',
                    '2/4 Developing: Aether Sitting Behind Furina on the Bed Gently'),
                   ('/dating-media/furina_s4_sc2_cg3.jpg',
                    "3/4 Climax: Aether Pressing a Warm Kiss to Furina's Bare Shoulder as"),
                   ('/dating-media/furina_s4_sc2_cg4.jpg',
                    '4/4 Finale: Cuddling Closely Under the Canopy Bed Covers Listening')],
 'furina_s4_sc3': [('/dating-media/furina_s4_sc3_cg1.jpg',
                    '1/4 Opening: Arriving Together at the Private Cliffside Starlit'),
                   ('/dating-media/furina_s4_sc3_cg2.jpg',
                    '2/4 Developing: Furina Floating Blue Romaritime Petals Across the'),
                   ('/dating-media/furina_s4_sc3_cg3.jpg',
                    '3/4 Climax: Sitting Side-by-Side in the Steaming Spring as Furina'),
                   ('/dating-media/furina_s4_sc3_cg4.jpg',
                    '4/4 Finale: Wrapped in Matching Silk Robes on the Veranda Sharing')],
 'furina_s4_sc4': [('/dating-media/furina_s4_sc4_cg1.jpg',
                    '1/4 Opening: Furina Presenting a Brass Mansion Key Tied with a Blue'),
                   ('/dating-media/furina_s4_sc4_cg2.jpg',
                    '2/4 Developing: Aether Closing His Hand Over the Key & Pulling'),
                   ('/dating-media/furina_s4_sc4_cg3.jpg',
                    '3/4 Climax: Unlocking Her Richman Mansion Front Door Together'),
                   ('/dating-media/furina_s4_sc4_cg4.jpg',
                    '4/4 Finale: Aether Carrying a Laughing, Blushing Furina Across the')],
 'furina_s5_sc1': [('/dating-media/furina_s5_sc1_cg1.jpg',
                    "1/4 Opening: Aether Gently Applying Sunscreen to Furina's Shoulders"),
                   ('/dating-media/furina_s5_sc1_cg2.jpg',
                    '2/4 Developing: Furina in Her Sapphire Halter Swimsuit Leaping into'),
                   ('/dating-media/furina_s5_sc1_cg3.jpg',
                    '3/4 Climax: Passionate Sunset Embrace on the Beach Towel Wrapped in'),
                   ('/dating-media/furina_s5_sc1_cg4.jpg',
                    '4/4 Finale: Cuddling by the Starlit Beach Bonfire as Ocean Waves')],
 'furina_s5_sc2': [('/dating-media/furina_s5_sc2_cg1.jpg',
                    '1/4 Opening: Furina in a Pearl-and-Sapphire Silk Evening Negligee'),
                   ('/dating-media/furina_s5_sc2_cg2.jpg',
                    "2/4 Developing: Sitting Across Aether's Lap on the Velvet Sofa"),
                   ('/dating-media/furina_s5_sc2_cg3.jpg',
                    '3/4 Climax: Deep Candlelit Kiss Surrounded by Blue Rose Petals &'),
                   ('/dating-media/furina_s5_sc2_cg4.jpg',
                    "4/4 Finale: Sleeping Peacefully in Aether's Arms Under Silk Sheets")],
 'furina_s5_sc3': [('/dating-media/furina_s5_sc3_cg1.jpg',
                    "1/4 Opening: Sleepy Furina in Aether's Oversized White Shirt Pulling"),
                   ('/dating-media/furina_s5_sc3_cg2.jpg',
                    '2/4 Developing: Furina Feeding Aether a Fresh Strawberry Crepe Bite'),
                   ('/dating-media/furina_s5_sc3_cg3.jpg',
                    '3/4 Climax: Aether Hugging Furina from Behind by the Sunny Bedroom'),
                   ('/dating-media/furina_s5_sc3_cg4.jpg',
                    '4/4 Finale: Intertwined Fingers on the Sunlit Pillow with Matching')],
 'furina_s5_sc4': [('/dating-media/furina_s5_sc4_cg1.jpg',
                    '1/4 Opening: Walking Hand-in-Hand Down the Starlit Opera Aisle Under'),
                   ('/dating-media/furina_s5_sc4_cg2.jpg',
                    '2/4 Developing: Furina Singing Her Unscripted Eternal Love Aria for'),
                   ('/dating-media/furina_s5_sc4_cg3.jpg',
                    '3/4 Climax: Aether Slipping the Sapphire-and-Gold Promise Ring onto'),
                   ('/dating-media/furina_s5_sc4_cg4.jpg',
                    '4/4 Finale: Passionate Eternal-Vow Kiss Surrounded by Salon')],
 'furina_s1_ex1': [('/dating-media/furina_s1_ex1_cg1.jpg',
                    '1/4 Opening: Running into Iudex Neuvillette at a Fontaine Cafe Over'),
                   ('/dating-media/furina_s1_ex1_cg2.jpg',
                    '2/4 Developing: Aether Ordering Romaritime Spring Water & Cake for'),
                   ('/dating-media/furina_s1_ex1_cg3.jpg',
                    '3/4 Climax: Neuvillette Formally Thanking Aether for Bringing'),
                   ('/dating-media/furina_s1_ex1_cg4.jpg',
                    '4/4 Cameo: Warm Cafe Toast Between Aether, Blushing Furina &')],
 'furina_s1_ex2': [('/dating-media/furina_s1_ex2_cg1.jpg',
                    '1/4 Opening: Steambird Reporter Charlotte Popping Out with Monsieur'),
                   ('/dating-media/furina_s1_ex2_cg2.jpg',
                    '2/4 Developing: Aether Playfully Shielding Furina as They Duck'),
                   ('/dating-media/furina_s1_ex2_cg3.jpg',
                    "3/4 Climax: Mademoiselle Crabaletta Photobombing Charlotte's Kamera"),
                   ('/dating-media/furina_s1_ex2_cg4.jpg',
                    '4/4 Cameo: Laughing Over the Hilarious Photobomb Print with')],
 'furina_s2_ex1': [('/dating-media/furina_s2_ex1_cg1.jpg',
                    '1/4 Opening: Afternoon Tea & Macarons on the Promenade with Navia &'),
                   ('/dating-media/furina_s2_ex1_cg2.jpg',
                    '2/4 Developing: Navia Teasing Furina for Saving the Crown Strawberry'),
                   ('/dating-media/furina_s2_ex1_cg3.jpg',
                    '3/4 Climax: Clorinde Calmly Pouring Tea While Blushing Furina Feeds'),
                   ('/dating-media/furina_s2_ex1_cg4.jpg',
                    '4/4 Cameo: Cheerful Fontaine Tea Party Group Photo with Navia,')],
 'furina_s2_ex2': [('/dating-media/furina_s2_ex2_cg1.jpg',
                    '1/4 Opening: Visiting Chioriya Boutique with Aether for Custom Stage'),
                   ('/dating-media/furina_s2_ex2_cg2.jpg',
                    '2/4 Developing: Chiori Holding Up Gold-and-Starlight Silk Accents'),
                   ('/dating-media/furina_s2_ex2_cg3.jpg',
                    "3/4 Climax: Aether Fastening the Gold Starlight Brooch on Furina's"),
                   ('/dating-media/furina_s2_ex2_cg4.jpg',
                    '4/4 Cameo: Walking Out of Chioriya Boutique in Matching')],
 'furina_s3_ex1': [('/dating-media/furina_s3_ex1_cg1.jpg',
                    '1/4 Opening: Attending a Magic Show Rehearsal at Opera Epiclese with'),
                   ('/dating-media/furina_s3_ex1_cg2.jpg',
                    '2/4 Developing: Lyney & Lynette Inviting Aether & Furina to the'),
                   ('/dating-media/furina_s3_ex1_cg3.jpg',
                    '3/4 Climax: Lyney Producing a Glowing Blue Romaritime Flower Right'),
                   ('/dating-media/furina_s3_ex1_cg4.jpg',
                    "4/4 Cameo: Aether Pinning the Romaritime Flower in Furina's Hair as")],
 'furina_s3_ex2': [('/dating-media/furina_s3_ex2_cg1.jpg',
                    '1/4 Opening: Director Hu Tao Visiting from Liyue to Pitch a'),
                   ('/dating-media/furina_s3_ex2_cg2.jpg',
                    '2/4 Developing: Boo Tao & Crabaletta Floating Nose-to-Nose as Furina'),
                   ('/dating-media/furina_s3_ex2_cg3.jpg',
                    "3/4 Climax: Hu Tao Teasing How Tightly Furina Holds Aether's Arm in"),
                   ('/dating-media/furina_s3_ex2_cg4.jpg',
                    "4/4 Cameo: Cross-Region Directors' Tea Toast with Hu Tao, Furina &")],
 'furina_s4_ex1': [('/dating-media/furina_s4_ex1_cg1.jpg',
                    "1/4 Opening: Walking Hand-in-Hand Outside Patisserie 'Pour la"),
                   ('/dating-media/furina_s4_ex1_cg2.jpg',
                    '2/4 Developing: Caught on a Date! Charlotte Gasps with Her Kamera as'),
                   ('/dating-media/furina_s4_ex1_cg3.jpg',
                    '3/4 Climax: Navia Playfully Opening Her Golden Umbrella to Block'),
                   ('/dating-media/furina_s4_ex1_cg4.jpg',
                    '4/4 Cameo: Escaping Hand-in-Hand Down the Harbor Steps Laughing as')],
 'furina_s4_ex2': [('/dating-media/furina_s4_ex2_cg1.jpg',
                    '1/4 Opening: A Sudden Evening Drizzle Over the Promenade as'),
                   ('/dating-media/furina_s4_ex2_cg2.jpg',
                    "2/4 Developing: Furina Under Aether's Umbrella Teasing Neuvillette"),
                   ('/dating-media/furina_s4_ex2_cg3.jpg',
                    '3/4 Climax: Neuvillette Smiling Gently as Golden Sunset Parting the'),
                   ('/dating-media/furina_s4_ex2_cg4.jpg',
                    '4/4 Cameo: Walking Beneath a Double Rainbow Over the Bay as')],
 'furina_s5_ex1': [('/dating-media/furina_s5_ex1_cg1.jpg',
                    '1/4 Opening: Opening Night Gala Red Carpet with Navia, Clorinde,'),
                   ('/dating-media/furina_s5_ex1_cg2.jpg',
                    '2/4 Developing: The Entire Fontaine Cast Raising a Sparkling Toast'),
                   ('/dating-media/furina_s5_ex1_cg3.jpg',
                    '3/4 Climax: Furina & Aether Sharing the Centerpiece Spotlight Waltz'),
                   ('/dating-media/furina_s5_ex1_cg4.jpg',
                    '4/4 Cameo: Grand Finale Curtain Call Kiss Applauded by All Their')],
 'furina_s5_ex2': [('/dating-media/furina_s5_ex2_cg1.jpg',
                    '1/4 Opening: Approaching the Starlit Fountain of Lucine Hand-in-Hand'),
                   ('/dating-media/furina_s5_ex2_cg2.jpg',
                    '2/4 Developing: Neuvillette Noticing Their Sapphire-and-Gold Promise'),
                   ('/dating-media/furina_s5_ex2_cg3.jpg',
                    '3/4 Climax: Neuvillette Offering His Solemn Blessing Over Pure'),
                   ('/dating-media/furina_s5_ex2_cg4.jpg',
                    '4/4 Cameo: Embracing Beneath the Glowing Fountain of Lucine as')]}

FURINA_20_SCENARIOS: list[dict[str, Any]] = [{'id': 'furina_s1_sc1',
  'char_id': 'furina',
  'stage': 1,
  'order': 1,
  'scenario_num': 1,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 1 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': "The Last 'Pour la Justice' Opera Cake",
  'subtitle': 'Stage 1 - Episode 1 - Sunlit Patisserie Terrace',
  'location': 'Rodeo Boulevard Patisserie',
  'cg_url': '/dating-media/furina_s1_sc1_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s1_sc1_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Clinking Porcelain Teacups in the Sunlit Courtyard with',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s1_sc1_cg1.jpg',
                   'label': "1/4 Opening: Reaching for the Final 'Pour la Justice' Cake Slice"},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s1_sc1_cg2.jpg',
                   'label': '2/4 Developing: Aether Gallantly Sliding the Cake Plate to a'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s1_sc1_cg3.jpg',
                   'label': "3/4 Climax: Crabaletta Nudging Furina's Elbow as She Feeds Aether"},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s1_sc1_cg4.jpg',
                   'label': '4/4 Finale: Clinking Porcelain Teacups in the Sunlit Courtyard with'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': "Shared the final slice of 'Pour la Justice' strawberry opera cake with Furina at the "
                'patisserie as Mademoiselle Crabaletta played wingman.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s1_sc1_cg1.jpg',
             'scene_label': "1/4 Opening: Reaching for the Final 'Pour la Justice' Cake Slice",
             'scene_progress': 'SCENE 1/4',
             'narration': 'Sunlight filters through the blue-and-white awning of Rodeo Boulevard Patisserie '
                          'as you and Furina reach the display counter at the exact same moment - both of '
                          "your dessert forks hovering over the final slice of 'Pour la Justice' strawberry "
                          'opera cake.',
             'inner_thought': "Salon Solitaire's Whisper: Oh no, there's only one slice of 'Pour la Justice' "
                              'left - and Aether is looking right at it too!',
             'action_cue': 'Gasps dramatically with one gloved hand over her chest while Mademoiselle '
                           'Crabaletta floats in a bubble between you.',
             'speaker_line': 'Ahem! Hold your fork right there, my dear Aether! Do my eyes deceive me, or '
                             "were you about to claim the last limited-edition 'Pour la Justice' cake right "
                             'in front of its namesake?',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Gallantly yield the cake to her & ask to join her tea table instead',
                          'player_text': 'I actually grabbed this last slice so nobody else would take it '
                                         'before you arrived, Furina. May I join your table for tea?',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Blushes brightly beneath her top hat.',
                          'reaction_reply': 'W-Wait, you saved it specifically for me?! Well! Since you '
                                            'showed such impeccable chivalry, I insist you sit across from '
                                            'me right now!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Suggest splitting the final slice fifty-fifty over a pot of black tea',
                          'player_text': "Then let's share the final slice together over a pot of Fontaine "
                                         'black tea, Lady Furina!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'A diplomatic and delicious proposal! Sit down, Aether, and I '
                                            'shall pour the tea!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s1_sc1_cg2.jpg',
             'scene_label': '2/4 Developing: Aether Gallantly Sliding the Cake Plate to a',
             'scene_progress': 'SCENE 2/4',
             'narration': 'At the sunlit marble patio table, you slide the porcelain cake plate toward '
                          'Furina. She tries to maintain her haughty star-director posture, even as her '
                          'cyan-and-navy eyes sparkle at the layered strawberry confection.',
             'inner_thought': "Salon Solitaire's Whisper: He handed me the whole slice without hesitation... "
                              "I can't just eat it all in front of him while he only drinks tea!",
             'action_cue': 'Clears her throat and cuts the top strawberry-crowned piece with delicate '
                           'precision.',
             'speaker_line': 'You know, Aether, back when I had to play the role of Archon at grand '
                             'banquets, sweets were the only comfort that felt real. Having someone simply '
                             'sit across from me at a cafe without any formalities... is rather nice.',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Tell her that casual afternoon tea with her is your favorite part of the',
                          'player_text': 'No formalities, no scripts, and no courts here, Furina - just you, '
                                         'me, and the best cake in town whenever you want company.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Her expression softens into a genuine, rosy-cheeked smile.',
                          'reaction_reply': "Careful, Aether - if you spoil me like that, I'll expect your "
                                            'company at tea every single afternoon!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Smile warmly & pour her a fresh cup of fragrant black tea',
                          'player_text': 'Here, let me pour your tea to go with the cake, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, thank you, my attentive co-star!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s1_sc1_cg3.jpg',
             'scene_label': "3/4 Climax: Crabaletta Nudging Furina's Elbow as She Feeds Aether",
             'scene_progress': 'SCENE 3/4',
             'narration': 'Just as Furina hesitates with the strawberry-topped bite on her fork, '
                          "Mademoiselle Crabaletta floats up and nudges Furina's elbow - guiding the fork "
                          'straight toward your lips!',
             'inner_thought': "Salon Solitaire's Whisper: C-Crabaletta!! Don't push my arm - now I'm feeding "
                              'Aether from my own fork!!',
             'action_cue': 'Blushes scarlet as she holds the strawberry forkful right in front of your lips.',
             'speaker_line': "M-Mademoiselle Crabaletta insisted!! Well, don't just sit there staring while "
                             "my hand is shaking, Aether - say 'aaah' and take the crown strawberry bite!",
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Lean forward, eat the bite from her fork & praise how sweet it is',
                          'player_text': "That's the sweetest bite of cake I've ever tasted - thank you, "
                                         'Furina, and thank you, Crabaletta.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Covers her glowing pink cheek with her gloved hand while '
                                             'Crabaletta blows happy bubbles.',
                          'reaction_reply': 'A-Aiya... indirect fork and all! This afternoon was a 100-point '
                                            'premiere!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Happily accept the strawberry bite & thank her warmly',
                          'player_text': 'Thank you, Furina! Your favorite cake really lives up to its '
                                         'reputation.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Naturally! My palate for desserts - and companions - is '
                                            'flawless!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s1_sc2',
  'char_id': 'furina',
  'stage': 1,
  'order': 2,
  'scenario_num': 2,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 1 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Rehearsing Lines on the Bayside Boardwalk',
  'subtitle': 'Stage 1 - Episode 2 - Oceanfront Script Run',
  'location': 'Verona Beach Bayside Boardwalk',
  'cg_url': '/dating-media/furina_s1_sc2_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s1_sc2_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Taking a Joyful Curtain-Call Bow Hand-in-Hand Against',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s1_sc2_cg1.jpg',
                   'label': '1/4 Opening: Rehearsing Musical Lines Together on the Breezy Bayside'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s1_sc2_cg2.jpg',
                   'label': "2/4 Developing: Aether Taking Furina's Gloved Hand in a Dashing"},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s1_sc2_cg3.jpg',
                   'label': "3/4 Climax: Aether Catching Furina's Flying Script Pages & Steadying"},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s1_sc2_cg4.jpg',
                   'label': '4/4 Finale: Taking a Joyful Curtain-Call Bow Hand-in-Hand Against'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Rehearsed a romantic musical scene with Furina on the Verona Beach boardwalk and caught her '
                'script and top hat in the ocean breeze.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s1_sc2_cg1.jpg',
             'scene_label': '1/4 Opening: Rehearsing Musical Lines Together on the Breezy Bayside',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Seagulls wheel above the sunlit wooden boardwalk of Verona Beach as Furina hands '
                          'you a ribbon-bound script notebook and strikes a grand theatrical stance by the '
                          'railing.',
             'inner_thought': "Salon Solitaire's Whisper: Ever since we won the Furina Award together during "
                              'the Fontinalia Film Festival, Aether is the only person I trust to test my '
                              'new dialogue!',
             'action_cue': 'Places one hand over her heart and holds up her copy of the script against the '
                           'sparkling bay.',
             'speaker_line': "Listen well, Aether! I'm writing a new musical about a star traveler and a "
                             "runaway songstress, and I need you to read the hero's lines opposite me. Ready "
                             'from the top of Scene Two?',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Step into character immediately with a warm, theatrical voice',
                          'player_text': "Whenever my favorite director calls 'Action,' I'm ready. Lead the "
                                         'scene, Furina!',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Her heterochromia eyes light up with pure creative joy.',
                          'reaction_reply': "Magnificent! That's the spirit of my Fontinalia co-star!"},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Open the script book & ask what tone the hero should use',
                          'player_text': 'Got the script right here! Should I play the hero dashing and '
                                         'bold, or gentle and sincere?',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Both, naturally - just play him the way you always act around '
                                            'me!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s1_sc2_cg2.jpg',
             'scene_label': "2/4 Developing: Aether Taking Furina's Gloved Hand in a Dashing",
             'scene_progress': 'SCENE 2/4',
             'narration': 'Reading the stage directions aloud, Furina recites the heroine\'s line: "If the '
                          'curtain falls on this world tomorrow, who will remember my song?" Following the '
                          'script prompt, you step forward and gently take her gloved hand in a princely '
                          'bow.',
             'inner_thought': "Salon Solitaire's Whisper: W-Wait - I wrote that hand-holding stage direction "
                              'myself, so why is my heart pounding this fast when Aether actually does it?!',
             'action_cue': 'Gasps softly as you bow over her gloved hand, her cheeks flushing bright pink.',
             'speaker_line': '"Even if every stage fades away, I will remember every note you ever sang." '
                             "...U-Um, Aether?! The script didn't say to look into my eyes quite THAT "
                             'intensely while holding my hand!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Keep holding her hand gently & tell her you meant every word',
                          'player_text': "Maybe it wasn't just acting, Furina - because I really won't ever "
                                         'forget a single song you sing.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Stammers with a radiant blush, unable to pull her hand away.',
                          'reaction_reply': "Y-You can't just blur the line between the script and reality "
                                            "like that! My poor heart wasn't rehearsed for that!"},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Smile & compliment how naturally she wrote the emotional scene',
                          'player_text': 'Your writing makes it easy to put real feeling into the lines, '
                                         'Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'A-Ahem! Well, the writer AND the leading man both deserve ten '
                                            'out of ten!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s1_sc2_cg3.jpg',
             'scene_label': "3/4 Climax: Aether Catching Furina's Flying Script Pages & Steadying",
             'scene_progress': 'SCENE 3/4',
             'narration': 'Suddenly, a strong gust of ocean wind sweeps across the pier, threatening to lift '
                          "Furina's crown-adorned top hat and scatter her script pages - until you catch the "
                          'pages in one hand and steady her hat gently with the other.',
             'inner_thought': "Salon Solitaire's Whisper: His hand is right on my hat brim and we're "
                              'standing only inches apart!',
             'action_cue': 'Holds onto your wrist as you steady her top hat against the sea breeze, looking '
                           'up at you with wide, shining eyes.',
             'speaker_line': 'Whoa - ! My manuscript and my favorite hat! You rescued both in a single beat, '
                             'Aether... Just like a real leading hero.',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Adjust her top hat tenderly & bow with a smile for your curtain call',
                          'player_text': "Can't let the wind steal my director's crown. Shall we take our "
                                         'curtain-call bow together, Furina?',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Laces her fingers with yours and takes a joyful bow toward the '
                                             'ocean sunset.',
                          'reaction_reply': 'Bravo, Encore! Best rehearsal on the boardwalk ever, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hand her the neatly stacked script pages with a warm grin',
                          'player_text': 'Safe and sound, Director! Not a single page lost to the bay.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, my hero on and off the stage!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s1_sc3',
  'char_id': 'furina',
  'stage': 1,
  'order': 3,
  'scenario_num': 3,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 1 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Emergency Gourmet Macaroni Rescue',
  'subtitle': 'Stage 1 - Episode 3 - Cozy Apartment Kitchen',
  'location': "Furina's Richman Apartment Kitchen",
  'cg_url': '/dating-media/furina_s1_sc3_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s1_sc3_cg4.jpg',
  'ending_scene_label': "4/4 Finale: Cozy Domestic After-Dinner Tea in Furina's Warmly Lit",
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s1_sc3_cg1.jpg',
                   'label': '1/4 Opening: Aether Catching a Sheepish Furina Holding Three Boxes'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s1_sc3_cg2.jpg',
                   'label': '2/4 Developing: Standing Shoulder-to-Shoulder at the Stove in'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s1_sc3_cg3.jpg',
                   'label': '3/4 Climax: Aether Offering a Forkful of Gourmet Herbed Macaroni as'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s1_sc3_cg4.jpg',
                   'label': "4/4 Finale: Cozy Domestic After-Dinner Tea in Furina's Warmly Lit"}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Rescued Furina from another night of plain instant macaroni by cooking a gourmet herbed '
                'pasta dinner together in her kitchen.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s1_sc3_cg1.jpg',
             'scene_label': '1/4 Opening: Aether Catching a Sheepish Furina Holding Three Boxes',
             'scene_progress': 'SCENE 1/4',
             'narration': "Dropping by Furina's apartment at dinnertime with a basket of fresh groceries, "
                          'you walk into the kitchen to find Furina standing guiltily by a boiling pot - '
                          'holding three boxes of plain instant macaroni.',
             'inner_thought': "Salon Solitaire's Whisper: Busted!! I told Aether yesterday I was eating "
                              'balanced meals, and he just caught me with three boxes of three-minute '
                              'macaroni!',
             'action_cue': 'Hides the macaroni boxes behind her back with a sheepish, rosy blush and '
                           'whistles innocently.',
             'speaker_line': 'A-Ah, Aether! What a coincidence! I was just preparing an avant-garde '
                             'minimalist Fontaine delicacy - definitely NOT plain boiled macaroni for the '
                             'fourth night this week!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Laugh warmly, set down your fresh ingredients & tie an apron on her',
                          'player_text': 'Caught red-handed, Lady Furina! Keep the macaroni pasta, but let '
                                         'me help you cook a real gourmet tomato-and-cream sauce from '
                                         'scratch tonight.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Sighs in happy relief as you tie the frilly apron ribbon '
                                             'behind her waist.',
                          'reaction_reply': 'Okay, okay, I surrender to Chef Aether! Cooking together sounds '
                                            'a hundred times better than eating alone anyway!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Unpack fresh tomatoes, sweet basil & cream onto the counter',
                          'player_text': "Good thing I brought fresh tomatoes, basil, and cream! Let's "
                                         'upgrade dinner together.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Oho! Fresh ingredients from the Traveler himself - my kitchen '
                                            'is honored!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s1_sc3_cg2.jpg',
             'scene_label': '2/4 Developing: Standing Shoulder-to-Shoulder at the Stove in',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Standing shoulder-to-shoulder at the warm stove in matching aprons, you guide '
                          "Furina's hand on the wooden spoon as the rich tomato, garlic, and cream sauce "
                          'simmers to a glossy perfection.',
             'inner_thought': "Salon Solitaire's Whisper: Standing right next to Aether at the stove with "
                              'his hand guiding mine... my apartment feels so warm and lively tonight!',
             'action_cue': 'Leans slightly against your arm as you guide her hand stirring the copper pan.',
             'speaker_line': 'Mmm, smell that basil and cream! When I first moved into my own apartment '
                             'after the prophecy ended, the kitchen felt so quiet... Having you here '
                             'teaching me like this feels wonderful, Aether.',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Tell her you'll come cook dinner with her whenever her apartment feels",
                          'player_text': "Whenever your kitchen feels too quiet, just text me, Furina - I'll "
                                         'come cook with you any night you want.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Turns her head to beam up at you, her cheeks glowing warmer '
                                             'than the stove.',
                          'reaction_reply': "Promise?! Then I'm officially booking you as my permanent head "
                                            'chef and dinner companion!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Praise how quickly she picked up the sauce technique',
                          'player_text': "You've got a natural touch with the sauce, Furina - look how "
                                         'smooth it turned out!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, naturally! With you guiding my hand, how could we fail?'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s1_sc3_cg3.jpg',
             'scene_label': '3/4 Climax: Aether Offering a Forkful of Gourmet Herbed Macaroni as',
             'scene_progress': 'SCENE 3/4',
             'narration': 'Twirling a forkful of the finished gourmet macaroni, you blow on it gently and '
                          'offer the first taste to Furina across the kitchen island.',
             'inner_thought': "Salon Solitaire's Whisper: He's feeding me the first bite right off the "
                              'fork...!',
             'action_cue': 'Leans in and tastes the pasta from your fork, her heterochromia eyes widening in '
                           'pure culinary bliss.',
             'speaker_line': "Mmmmm!! It's creamy, rich, and a million times better than boxed sauce! "
                             'Aether, you have officially ruined plain macaroni for me forever!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Smile & share the rest of the steaming dinner & black tea together',
                          'player_text': "Then I'll just have to keep cooking the real thing for you, "
                                         'Furina. Bon appetit!',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Clinks her teacup happily against yours after dinner.',
                          'reaction_reply': 'Bon appetit, my dearest Traveler - best homemade dinner of my '
                                            'life!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Serve two generous plates & sit down together',
                          'player_text': "Plenty more in the pan! Let's sit down and enjoy it while it's "
                                         'hot.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Best five-star restaurant in San Andreas is right here at our '
                                            'table!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s1_sc4',
  'char_id': 'furina',
  'stage': 1,
  'order': 4,
  'scenario_num': 4,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 1 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Sudden Rain Without a Prophecy',
  'subtitle': 'Stage 1 - Episode 4 - Rainy Promenade Gazebo',
  'location': 'Rodeo Boulevard Marble Gazebo',
  'cg_url': '/dating-media/furina_s1_sc4_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s1_sc4_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Strolling Home Along Glistening Starlit Cobblestones',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s1_sc4_cg1.jpg',
                   'label': '1/4 Opening: Aether Sheltering Furina with His Cape as They Dash'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s1_sc4_cg2.jpg',
                   'label': '2/4 Developing: Watching Peaceful Raindrops Fall from the Gazebo'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s1_sc4_cg3.jpg',
                   'label': '3/4 Climax: Aether Draping His Warm White-and-Gold Scarf Around'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s1_sc4_cg4.jpg',
                   'label': '4/4 Finale: Strolling Home Along Glistening Starlit Cobblestones'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Sheltered from a sudden evening rainstorm in a marble gazebo with Furina, wrapping your '
                'warm scarf around her as she found peace in the rain.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s1_sc4_cg1.jpg',
             'scene_label': '1/4 Opening: Aether Sheltering Furina with His Cape as They Dash',
             'scene_progress': 'SCENE 1/4',
             'narration': 'During an evening stroll along the promenade, silver rainclouds suddenly open '
                          "overhead. You hold your white-and-gold cape over Furina's top hat as the two of "
                          'you dash laughing into a white marble gazebo.',
             'inner_thought': "Salon Solitaire's Whisper: He shielded my hat with his own cape the entire "
                              'run to the gazebo!',
             'action_cue': 'Catches her breath inside the dry gazebo and brushes a sparkling raindrop off '
                           'her sleeve.',
             'speaker_line': "Phew, talk about an unscripted downpour! You didn't let a single drop ruin my "
                             'hat, Aether - though your own shoulder got soaked shielding me!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Assure her you don't mind the rain as long as she stayed dry",
                          'player_text': "A little rain doesn't bother me at all - keeping my leading lady "
                                         'dry was top priority, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Looks at your damp shoulder with a touched, softened blush.',
                          'reaction_reply': 'You always put me first without even thinking twice, Aether...'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Laugh & shake the raindrops off your cape together',
                          'player_text': 'We made it just in time! That was quite the sprint, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, worthy of an action movie scene!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s1_sc4_cg2.jpg',
             'scene_label': '2/4 Developing: Watching Peaceful Raindrops Fall from the Gazebo',
             'scene_progress': 'SCENE 2/4',
             'narration': 'As the rain patters steadily against the marble dome, Furina steps to the edge of '
                          'the gazebo and holds her palm out to catch a cool raindrop, her expression '
                          'turning quiet and reflective.',
             'inner_thought': "Salon Solitaire's Whisper: For five hundred years in Fontaine, every "
                              'rainstorm reminded me of the prophecy of dissolution... yet standing here '
                              'with Aether, the rain feels gentle.',
             'action_cue': 'Watches the rain ripple in the courtyard puddles, then glances softly back at '
                           'you.',
             'speaker_line': 'You know, Aether... back in Fontaine, the sound of rain used to fill my chest '
                             'with dread because of the prophecy. But listening to the rain here with you '
                             'beside me... it just sounds like a peaceful lullaby.',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Step close beside her & tell her the rain can only bring good memories '
                                   'now',
                          'player_text': 'The prophecy is over forever, Furina. From now on, every rainy '
                                         'evening is just a cozy excuse for the two of us to relax together.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Her cyan-and-navy eyes glisten with gratitude as she steps '
                                             'closer to your side.',
                          'reaction_reply': 'Thank you, Aether... hearing you say that washes away the last '
                                            'shadow in my heart.'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Stand warmly at her shoulder & listen to the rain rhythm together',
                          'player_text': "It really is a soothing rhythm when we're listening to it "
                                         'together, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "Mmm... I actually like rainy days now when you're here."},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s1_sc4_cg3.jpg',
             'scene_label': '3/4 Climax: Aether Draping His Warm White-and-Gold Scarf Around',
             'scene_progress': 'SCENE 3/4',
             'narration': 'A cool evening breeze drifts through the gazebo arches. Sitting beside her on the '
                          "bench, you drape your warm white-and-gold scarf around Furina's shoulders until "
                          'the sky clears into sparkling stars.',
             'inner_thought': "Salon Solitaire's Whisper: Wrapped in Aether's warm scarf while the stars "
                              "come out... I don't want this walk to end.",
             'action_cue': 'Holds the ends of your golden scarf close to her chin as you both step out onto '
                           'the glistening cobblestones.',
             'speaker_line': 'Look, the clouds parted and the stars are reflecting in every puddle! Thank '
                             'you for lending me your scarf - and your warmth - tonight, Aether.',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Offer your arm to escort her all the way home under the stars',
                          'player_text': 'Keep the scarf on until we reach your door, Furina - and hold onto '
                                         "my arm so you don't slip on the wet cobblestones.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Hooks her hands happily around your arm, leaning close as you '
                                             'walk home.',
                          'reaction_reply': 'Best rainy evening in five hundred years, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Walk side-by-side along the starlit street together',
                          'player_text': "Let's walk home slowly and enjoy the starlight, Furina.",
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Lead the way, my faithful Traveler!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s2_sc1',
  'char_id': 'furina',
  'stage': 2,
  'order': 1,
  'scenario_num': 1,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 2 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Midnight Audition at the Empty Amphitheater',
  'subtitle': 'Stage 2 - Episode 1 - Private Spotlight Duet',
  'location': 'Vinewood Open-Air Amphitheater',
  'cg_url': '/dating-media/furina_s2_sc1_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s2_sc1_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Sitting Side-by-Side on the Stage Edge Sharing Warm',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s2_sc1_cg1.jpg',
                   'label': '1/4 Opening: Furina Under a Single Golden Spotlight Inviting Aether'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s2_sc1_cg2.jpg',
                   'label': '2/4 Developing: Hands Brushing at the Backstage Console While Tuning'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s2_sc1_cg3.jpg',
                   'label': '3/4 Climax: Singing a Private Heartfelt Duet Center-Stage Under'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s2_sc1_cg4.jpg',
                   'label': '4/4 Finale: Sitting Side-by-Side on the Stage Edge Sharing Warm'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Tuned stage spotlights and sang a heartfelt private midnight duet with Furina on the empty '
                'amphitheater stage.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s2_sc1_cg1.jpg',
             'scene_label': '1/4 Opening: Furina Under a Single Golden Spotlight Inviting Aether',
             'scene_progress': 'SCENE 1/4',
             'narration': 'At midnight, the grand open-air amphitheater is completely empty save for a '
                          'single golden spotlight shining center-stage. Furina stands in the beam of light '
                          'and waves you up the stage steps.',
             'inner_thought': "Salon Solitaire's Whisper: Singing in front of crowds used to terrify me "
                              "after the trial, until Aether helped me sing as Clio in 'The Little "
                              "Oceanid'... tonight I want to sing just for him.",
             'action_cue': 'Extends her hand from the center of the glowing stage toward you.',
             'speaker_line': "Welcome to our private midnight theater, Aether! There's no audience and no "
                             'critics tonight - just the two of us. Come up on stage with me!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Walk up onto the stage & take her outstretched hand',
                          'player_text': "An exclusive midnight premiere with my favorite star? I wouldn't "
                                         'miss this for the world, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Squeezes your hand happily as you step into the golden '
                                             'spotlight beside her.',
                          'reaction_reply': 'Having you on stage beside me makes me feel invincible!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Step into the spotlight beside her & admire the night view',
                          'player_text': 'The whole amphitheater looks magical under the stars tonight, '
                                         'Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'And the acoustics are perfect for a duet!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s2_sc1_cg2.jpg',
             'scene_label': '2/4 Developing: Hands Brushing at the Backstage Console While Tuning',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Stepping backstage to the lighting console first, you and Furina lean close '
                          'together to set the sapphire-blue and golden-amber stage lights - your hand '
                          'brushing warmly over hers on the dimmer lever.',
             'inner_thought': "Salon Solitaire's Whisper: Our hands are right on top of each other on the "
                              'dimmer switch, and his cheek is so close to mine!',
             'action_cue': 'Blushes softly in the console glow, leaving her hand resting under yours on the '
                           'lever.',
             'speaker_line': 'O-Oh! Look how the sapphire Hydro light blends with your golden starlight on '
                             "the stage floor... You did that on purpose to match our colors, didn't you, "
                             'Aether?',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Smile & admit that blue and gold belong together on every stage',
                          'player_text': 'Of course I did - because sapphire blue and starlight gold belong '
                                         'together in every spotlight, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Her heart skips a beat as she gazes up at you.',
                          'reaction_reply': 'Aether... with lighting this romantic, we have to sing our duet '
                                            'right now!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Lock the blue-and-gold spotlight cue into place',
                          'player_text': 'Our signature colors make the best stage atmosphere! Ready to test '
                                         'it center-stage?',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Ready when you are, my co-star!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s2_sc1_cg3.jpg',
             'scene_label': '3/4 Climax: Singing a Private Heartfelt Duet Center-Stage Under',
             'scene_progress': 'SCENE 3/4',
             'narration': 'Back at center-stage beneath shimmering blue-and-gold lights, Furina begins the '
                          "tender melody of 'The Little Oceanid' - and when you harmonize with her on the "
                          'chorus, she reaches out to hold both of your hands.',
             'inner_thought': "Salon Solitaire's Whisper: Singing with Aether holding both my hands... I "
                              'never knew music could feel this warm and intimate.',
             'action_cue': 'Finishes the final note gazing deeply into your golden eyes, then sits with you '
                           'on the edge of the stage.',
             'speaker_line': "When I sang 'The Little Oceanid' in Poisson, you gave me the courage to love "
                             'the stage again... And tonight, singing with you holding my hands made me '
                             'realize who my song is truly for.',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Pour her a cup of warm honey tea & let her rest her head on your '
                                   'shoulder',
                          'player_text': "Every time you sing, Furina, I'll always be right here listening - "
                                         'whether in the front row or holding your hand on stage.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Rests her head softly against your shoulder on the stage edge.',
                          'reaction_reply': 'Best midnight audition ever, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Applaud her beautiful voice & share the warm thermos of tea',
                          'player_text': 'Your voice gets more breathtaking every time I hear it, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, only because my favorite audience of one is right beside '
                                            'me!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s2_sc2',
  'char_id': 'furina',
  'stage': 2,
  'order': 2,
  'scenario_num': 2,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 2 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Papier-Mache Props & Paint on Her Nose',
  'subtitle': 'Stage 2 - Episode 2 - Backstage Prop Workshop',
  'location': 'Theater Backstage Prop Studio',
  'cg_url': '/dating-media/furina_s2_sc2_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s2_sc2_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Admiring the Finished Stage Backdrop Together as Salon',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s2_sc2_cg1.jpg',
                   'label': '1/4 Opening: Painting Theater Set Backdrops with a Cute Smudge of'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s2_sc2_cg2.jpg',
                   'label': '2/4 Developing: Aether Leaning Close to Gently Wipe the Blue Paint'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s2_sc2_cg3.jpg',
                   'label': "3/4 Climax: Guiding Furina's Brush Hand Together to Paint a Golden"},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s2_sc2_cg4.jpg',
                   'label': '4/4 Finale: Admiring the Finished Stage Backdrop Together as Salon'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Painted a starry ocean stage backdrop with Furina in the prop workshop and gently wiped a '
                'smudge of blue paint from her nose.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s2_sc2_cg1.jpg',
             'scene_label': '1/4 Opening: Painting Theater Set Backdrops with a Cute Smudge of',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Inside the sunlit backstage prop studio, Furina wears a paint-dabbed canvas smock '
                          'over her waistcoat, proudly holding up a wide brush in front of a half-painted '
                          'ocean backdrop - completely unaware of the cute dot of sky-blue paint on the tip '
                          'of her nose.',
             'inner_thought': "Salon Solitaire's Whisper: I want this ocean-and-starlight backdrop to look "
                              'worthy of our next production!',
             'action_cue': 'Places a hand on her hip with a proud grin, a smudge of sky-blue paint right on '
                           'the tip of her nose.',
             'speaker_line': 'Behold, Aether! I have single-handedly painted the waves of Fontaine across '
                             'the main canvas! Why are you smiling like that - is my brushstroke technique '
                             'THAT awe-inspiring?',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Step close with a soft cloth & gently dab the blue paint off the tip of',
                          'player_text': 'Your waves are great, Director - enhancing your nose with sky-blue '
                                         'paint was an adorable artistic choice too. Hold still for a '
                                         'second.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Freezes with wide cyan-and-navy eyes and a crimson blush as '
                                             'you gently wipe the tip of her nose.',
                          'reaction_reply': "E-Eep!! How long was that paint on my nose?! And don't lean in "
                                            'so close without warning, Aether!!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Chuckle warmly & point to the cute blue paint dot on her nose',
                          'player_text': "You've got a cute little dot of sky-blue paint right on the tip of "
                                         'your nose, Furina!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "W-What?! Where's a mirror - no, wipe it off for me, Aether!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s2_sc2_cg2.jpg',
             'scene_label': '2/4 Developing: Aether Leaning Close to Gently Wipe the Blue Paint',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Still blushing from how close you leaned in, Furina picks up a jar of metallic '
                          'gold paint and looks up at the top of the backdrop canvas.',
             'inner_thought': "Salon Solitaire's Whisper: My nose is still tingling where Aether touched "
                              'it...!',
             'action_cue': 'Hands you a fine detail brush dipped in luminous gold paint.',
             'speaker_line': 'A-Ahem! Now that my face is paint-free, we need to paint the constellation of '
                             'stars above the ocean waves. Come help me guide the gold brush so the '
                             'starlight looks authentic, Traveler!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Stand close behind her & guide her brush hand to paint a golden star',
                          'player_text': "Let's paint the brightest star together - put your hand on the "
                                         "brush and I'll guide your stroke, Furina.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Leans back slightly against your chest as your hand covers '
                                             'hers, painting a radiant gold star on the canvas.',
                          'reaction_reply': 'Mmm... painting together like this feels way too romantic for a '
                                            'prop workshop!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Paint a trail of golden stars side-by-side across the canvas',
                          'player_text': "You paint the ocean reflections and I'll paint the stars right "
                                         'above them!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Look how beautifully our brushstrokes blend together!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s2_sc2_cg3.jpg',
             'scene_label': "3/4 Climax: Guiding Furina's Brush Hand Together to Paint a Golden",
             'scene_progress': 'SCENE 3/4',
             'narration': 'Stepping back to admire the finished ocean-and-starlight backdrop while '
                          'Crabaletta, Chevalmarin, and Usher applaud in floating bubbles, Furina adds two '
                          "tiny initials - 'A + F' - in the bottom corner of the canvas.",
             'inner_thought': "Salon Solitaire's Whisper: I hid our initials right in the corner wave so "
                              'every play we stage carries our signature!',
             'action_cue': "Points shyly to the tiny 'A + F' painted inside a seashell on the bottom corner "
                           'of the backdrop.',
             'speaker_line': "Look in the corner shell, Aether - every masterpiece needs the artists' "
                             'signature! What do you think of our joint creation?',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Praise the 'A + F' signature & kiss her paint-free cheek lightly",
                          'player_text': "That 'A + F' seashell is my favorite part of the whole backdrop, "
                                         'Furina. We make an unbeatable duo.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Touches her cheek with a dreamy, glowing smile.',
                          'reaction_reply': 'An unbeatable duo indeed, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'High-five her & celebrate with afternoon pastries',
                          'player_text': "Best stage backdrop in the theater! Let's wash up and celebrate "
                                         'with pastries!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Yay! Pastries with my co-artist!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s2_sc3',
  'char_id': 'furina',
  'stage': 2,
  'order': 3,
  'scenario_num': 3,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 2 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Coastal Convertible Run & Flying Top Hat',
  'subtitle': 'Stage 2 - Episode 3 - Scenic Highway Pullout',
  'location': 'Santa Maria Coastal Cliff Overlook',
  'cg_url': '/dating-media/furina_s2_sc3_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s2_sc3_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Watching the Golden Ocean Horizon Side-by-Side from the',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s2_sc3_cg1.jpg',
                   'label': '1/4 Opening: Cruising the Sunny Coastal Highway with Furina in Her'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s2_sc3_cg2.jpg',
                   'label': "2/4 Developing: Aether Catching Furina's Ribboned Top Hat at the"},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s2_sc3_cg3.jpg',
                   'label': '3/4 Climax: Furina Feeding Aether a Strawberry Macaron on the Hood'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s2_sc3_cg4.jpg',
                   'label': '4/4 Finale: Watching the Golden Ocean Horizon Side-by-Side from the'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Drove Furina along the coastal highway in your convertible, caught her ribboned top hat at '
                'the cliffside overlook, and shared macarons on the car hood.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s2_sc3_cg1.jpg',
             'scene_label': '1/4 Opening: Cruising the Sunny Coastal Highway with Furina in Her',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Cruising along the sunny coastal highway with the convertible top down, Furina '
                          'sits in your passenger seat wearing her sapphire heart-rimmed sunglasses, humming '
                          'happily to the radio.',
             'inner_thought': "Salon Solitaire's Whisper: Riding beside Aether with the ocean wind in my "
                              'hair and our favorite music playing... I could stay in this passenger seat '
                              'forever!',
             'action_cue': 'Lowers her heart-shaped sunglasses slightly to wink at you at the wheel.',
             'speaker_line': 'Five-star smooth cornering, my dear chauffeur! Pull over at this cliffside '
                             'ocean overlook - the golden hour light on the bay is begging for an '
                             'intermission!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Pull smoothly into the scenic overlook & open her passenger door like a',
                          'player_text': 'Your wish is my command, Lady Furina. Allow me to escort you to '
                                         'the best view on the coast.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Takes your hand as she steps out of the convertible with a '
                                             'delighted laugh.',
                          'reaction_reply': 'Such impeccable service! Ten bonus points for my driver!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Park at the cliffside rail so you can both admire the ocean view',
                          'player_text': 'Great call, Furina - look how clear the ocean horizon is from '
                                         'here!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Right?! I always know the most cinematic spots!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s2_sc3_cg2.jpg',
             'scene_label': "2/4 Developing: Aether Catching Furina's Ribboned Top Hat at the",
             'scene_progress': 'SCENE 2/4',
             'narration': 'As Furina steps up to the cliffside railing, a sudden coastal updraft sweeps her '
                          'ribboned top hat into the air - until you leap forward and snatch it cleanly '
                          'before it can blow over the cliff edge.',
             'inner_thought': "Salon Solitaire's Whisper: He caught my hat right at the railing and pulled "
                              'me safely back against his side!',
             'action_cue': 'Holds her hand to her wind-tousled white-and-blue hair as you place the hat '
                           'gently back onto her head.',
             'speaker_line': 'O-Oh! Thank the stars for your reflexes, Aether! For a second I thought my hat '
                             'was going for a swim in the ocean - and you pulled me back so securely too!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Fasten her hat ribbon gently under her chin so it stays secure',
                          'player_text': 'Let me tie this blue ribbon loosely under your chin so the sea '
                                         "breeze can't steal your crown again, Furina.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Stands completely still with a racing heart and rosy cheeks as '
                                             'your fingers tie the ribbon beneath her chin.',
                          'reaction_reply': 'U-Um, when your hands are that close to my face, Aether, the '
                                            "wind isn't the only thing taking my breath away!"},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hand her hat back with a warm, reassuring smile',
                          'player_text': "Got it safe and sound! Can't let the ocean take your signature top "
                                         'hat.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, my reliable knight in a convertible!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s2_sc3_cg3.jpg',
             'scene_label': '3/4 Climax: Furina Feeding Aether a Strawberry Macaron on the Hood',
             'scene_progress': 'SCENE 3/4',
             'narration': 'Sitting side-by-side on the warm hood of your convertible facing the golden ocean '
                          'horizon, Furina opens her pastel box of macarons and holds a strawberry one to '
                          'your lips.',
             'inner_thought': "Salon Solitaire's Whisper: Sitting on the hood of Aether's car watching the "
                              'sunset and feeding him macarons... this feels like a real romantic date!',
             'action_cue': 'Leans against your shoulder on the car hood and offers the pink strawberry '
                           'macaron to your lips.',
             'speaker_line': 'Since you rescued my hat AND drove so smoothly, here is your official reward, '
                             "Aether - say 'aaah'!",
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Take the macaron bite from her fingers & put your arm around her '
                                   'shoulder',
                          'player_text': 'Sweetest reward on the coast - and sitting here with my arm around '
                                         'you makes the sunset complete, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Nestles happily against your side on the car hood.',
                          'reaction_reply': "Let's stay right here until the first stars come out, Aether!"},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Enjoy the macaron & watch the golden waves together',
                          'player_text': 'Delicious! Thanks for sharing your favorite macarons with me, '
                                         'Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "With you, Aether, I'll always share the best ones!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s2_sc4',
  'char_id': 'furina',
  'stage': 2,
  'order': 4,
  'scenario_num': 4,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 2 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': "Falling Asleep Over Act III's Script",
  'subtitle': 'Stage 2 - Episode 4 - Midnight Study Balcony',
  'location': "Furina's Richman Study & Sofa",
  'cg_url': '/dating-media/furina_s2_sc4_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s2_sc4_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Writing the Final Scene of Her Script Together on the',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s2_sc4_cg1.jpg',
                   'label': '1/4 Opening: Finding Furina Fast Asleep Over Her Act III Manuscript'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s2_sc4_cg2.jpg',
                   'label': '2/4 Developing: Aether Gently Wrapping His Golden Scarf Around'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s2_sc4_cg3.jpg',
                   'label': "3/4 Climax: Sleepy Furina Waking Up & Holding Aether's Wrist So He"},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s2_sc4_cg4.jpg',
                   'label': '4/4 Finale: Writing the Final Scene of Her Script Together on the'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Found Furina asleep over her manuscript at midnight, draped your warm scarf over her, and '
                'stayed beside her to finish writing Act III together.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s2_sc4_cg1.jpg',
             'scene_label': '1/4 Opening: Finding Furina Fast Asleep Over Her Act III Manuscript',
             'scene_progress': 'SCENE 1/4',
             'narration': "When you arrive at Furina's apartment with late-night snacks to check on her "
                          'script deadline, you find her fast asleep on her velvet study sofa, her head '
                          'resting on pages of Act III and her fountain pen still loosely in her hand.',
             'inner_thought': "Salon Solitaire's Whisper: (Sleeping peacefully, murmuring softly in her "
                              'dreams...)',
             'action_cue': 'Sleeps curled up on the velvet sofa, her eyelashes fluttering softly in the warm '
                           'desk-lamp glow.',
             'speaker_line': 'murmurs in her sleep "...Don\'t go too far ahead, Aether... save the last '
                             'scene... for me..."',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Gently slip the pen from her fingers & drape your warm golden scarf over',
                          'player_text': "Rest easy, Furina - I'm right here, and I'm not going anywhere.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Sighs contentedly in her sleep, snuggling her cheek into the '
                                             'warm folds of your scarf.',
                          'reaction_reply': ''},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Set the warm tea on the table & brush a stray lock of hair from her',
                          'player_text': 'She worked herself to exhaustion on this script - let me cover her '
                                         'up so she stays warm.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Her breathing steadies peacefully under your scarf.',
                          'reaction_reply': ''},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s2_sc4_cg2.jpg',
             'scene_label': '2/4 Developing: Aether Gently Wrapping His Golden Scarf Around',
             'scene_progress': 'SCENE 2/4',
             'narration': 'A few minutes later, as you quietly organize her scattered manuscript pages, '
                          "Furina's cyan-and-navy eyes flutter open - and before she's even fully awake, her "
                          'hand reaches out and catches your wrist.',
             'inner_thought': "Salon Solitaire's Whisper: When I opened my eyes and saw Aether right beside "
                              'the sofa under the warm lamp, my hand moved on its own to hold him!',
             'action_cue': 'Holds onto your wrist with both hands from the sofa, looking up with sleepy, '
                           'unguarded eyes and a soft blush.',
             'speaker_line': "Aether...? You're really here, it wasn't just a dream... Please don't leave "
                             'yet - stay with me on the sofa for a little while?',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Sit right beside her on the sofa & hold her hand warmly in both of yours',
                          'player_text': "I'm not leaving, Furina. I'll stay right here beside you on the "
                                         'sofa as long as you want.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Leans her sleepy head against your upper arm with a blissful '
                                             'sigh.',
                          'reaction_reply': 'Whenever I wake up and see you here, the loneliness of the past '
                                            'disappears completely...'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Pour her a cup of warm chamomile tea & sit next to her',
                          'player_text': 'Right here beside you, Furina. Drink some warm tea and wake up '
                                         'slowly.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Mmm... thank you for staying with me, Aether.'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s2_sc4_cg3.jpg',
             'scene_label': "3/4 Climax: Sleepy Furina Waking Up & Holding Aether's Wrist So He",
             'scene_progress': 'SCENE 3/4',
             'narration': 'Fully cozy under your golden scarf, Furina props the clipboard on her lap between '
                          'the two of you so you can brainstorm the ending of Act III together.',
             'inner_thought': "Salon Solitaire's Whisper: Writing the climax of my romance musical while "
                              'leaning against Aether on the sofa... the hero in this script is 100% based '
                              'on him!',
             'action_cue': 'Points her pen at the final blank page while leaning her shoulder warmly against '
                           'yours.',
             'speaker_line': "All that's left is the final line of Act III, where the hero promises the "
                             "songstress she'll never be alone again. What line would you give him, Aether?",
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Write: 'Even when the final curtain falls, my hand will still be holding",
                          'player_text': "'Even when the final curtain falls, my hand will still be holding "
                                         "yours.' Because that's my real promise to you, Furina.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Stares at the line with shimmering eyes before hugging your '
                                             'arm tightly.',
                          'reaction_reply': "That's going straight into the script - and straight into my "
                                            'heart forever, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Help her polish the final stanza until the script is 100% complete',
                          'player_text': "Let's make the finale warm, hopeful, and unforgettable - just like "
                                         'our time together!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Script complete! Best late-night co-writing session ever!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s3_sc1',
  'char_id': 'furina',
  'stage': 3,
  'order': 1,
  'scenario_num': 1,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 3 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Unmasked Beneath the Lighthouse Stars',
  'subtitle': 'Stage 3 - Episode 1 - Oceanfront Heart-to-Heart',
  'location': 'Santa Maria Sunset Lighthouse',
  'cg_url': '/dating-media/furina_s3_sc1_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s3_sc1_cg4.jpg',
  'ending_scene_label': "4/4 Finale: Furina Resting Her Cheek Against Aether's Shoulder Under",
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s3_sc1_cg1.jpg',
                   'label': '1/4 Opening: Walking Up to the Santa Maria Sunset Lighthouse as the'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s3_sc1_cg2.jpg',
                   'label': '2/4 Developing: Hatless Furina Opening Her Heart About Her 500-Year'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s3_sc1_cg3.jpg',
                   'label': "3/4 Climax: Aether Intertwining Fingers with Furina's Ungloved Hand"},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s3_sc1_cg4.jpg',
                   'label': "4/4 Finale: Furina Resting Her Cheek Against Aether's Shoulder Under"}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Walked with Furina beneath the Santa Maria lighthouse stars as she opened her heart about '
                'her 500-year masquerade and held your hand without any mask.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s3_sc1_cg1.jpg',
             'scene_label': '1/4 Opening: Walking Up to the Santa Maria Sunset Lighthouse as the',
             'scene_progress': 'SCENE 1/4',
             'narration': 'As twilight deepens into a canopy of stars above the Santa Maria lighthouse, the '
                          'golden beacon sweeps across the ocean waves. Furina takes off her top hat and '
                          'holds it against her chest, letting the sea breeze stir her dual-toned hair.',
             'inner_thought': "Salon Solitaire's Whisper: Back in the inner opera house during the trial, "
                              'Aether was the only soul who saw my 182,376 days of silent endurance... with '
                              'him, I never have to pretend.',
             'action_cue': 'Stands at the lighthouse stone parapet with her hat off, looking up at you with '
                           'luminous, unguarded heterochromia eyes.',
             'speaker_line': 'Aether... for five hundred years, I had to wear a mask every waking second so '
                             'nobody could see me cry. Even after I became a normal human, part of me '
                             'wondered if anyone would ever truly love the ordinary, imperfect girl behind '
                             'the curtain.',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Step close, take her bare ungloved hand & tell her the girl behind the',
                          'player_text': 'From the moment I stepped into your inner world in Fontaine, '
                                         'Furina, the brave, gentle girl behind the curtain has been the '
                                         'most precious person in my life.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Her breath catches as her fingers intertwine tightly with '
                                             'yours, a tear of pure relief sparkling on her lashes.',
                          'reaction_reply': 'Aether... hearing you say that makes all five hundred years '
                                            'feel worth surviving.'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hold her hand warmly under the lighthouse beam',
                          'player_text': 'You never have to doubt it, Furina - I care about the real you '
                                         'more than any title or role.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Thank you, Aether... with you, I finally feel completely seen.'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s3_sc1_cg2.jpg',
             'scene_label': '2/4 Developing: Hatless Furina Opening Her Heart About Her 500-Year',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Glowing blue Hydro fireflies rise from her Vision and swirl around your joined '
                          'hands as you lift her ungloved hand toward your chest.',
             'inner_thought': "Salon Solitaire's Whisper: His thumb is tracing the back of my bare hand... "
                              'my heart is beating so fast I think he can feel it through my fingers!',
             'action_cue': 'Gazes at your joined hands with a deep rose blush as the lighthouse beam passes '
                           'overhead.',
             'speaker_line': "You know, when you hold my bare hand like this, Aether... it doesn't feel like "
                             'two co-stars rehearsing anymore. Tell me honestly - is your heart beating as '
                             'fast as mine right now?',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Lift her hand & press a tender kiss to her bare knuckles',
                          'player_text': "My heart beats this fast every time I'm near you, Furina - because "
                                         "I don't see you as just a friend or co-star anymore.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Gasps softly, her face turning radiant crimson as your lips '
                                             'touch her knuckles.',
                          'reaction_reply': 'A-Aether!! Kissing my hand under the lighthouse stars like a '
                                            "prince... you're going to make my Hydro Vision overflow!"},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Place her hand over your heartbeat so she can feel it',
                          'player_text': 'Feel for yourself, Furina - my heart only races like this for you.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe... it really is beating in the exact same rhythm as mine!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s3_sc1_cg3.jpg',
             'scene_label': "3/4 Climax: Aether Intertwining Fingers with Furina's Ungloved Hand",
             'scene_progress': 'SCENE 3/4',
             'narration': 'Stepping right into your side at the parapet, Furina rests her cheek against your '
                          'shoulder while keeping all five fingers locked with yours.',
             'inner_thought': "Salon Solitaire's Whisper: I'm completely, hopelessly in love with Aether.",
             'action_cue': 'Rests her head tenderly on your shoulder as the ocean waves lap below the '
                           'lighthouse.',
             'speaker_line': "Let's stay under the lighthouse stars a little longer, Aether... Tonight, I "
                             "don't want to be Lady Furina the director - I just want to be yours.",
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Wrap your arm around her waist & hold her close under the stars',
                          'player_text': 'Stay right here in my arms as long as you want, Furina. Tonight '
                                         "and always, you're mine.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Beams with sparkling cyan-and-navy heterochromia eyes.',
                          'reaction_reply': 'Mmm... best night of my human life, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hold her close & watch the starlit ocean together',
                          'player_text': "Take all the time in the world, Furina. I'm right here beside you.",
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Thank you, my dearest Traveler!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s3_sc2',
  'char_id': 'furina',
  'stage': 3,
  'order': 2,
  'scenario_num': 2,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 3 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Apex of the Sunset Ferris Wheel',
  'subtitle': 'Stage 3 - Episode 2 - Golden-Hour Confession',
  'location': 'Santa Maria Pier Ferris Wheel',
  'cg_url': '/dating-media/furina_s3_sc2_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s3_sc2_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Embracing in the Sunset Ferris Wheel Gondola as Official',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s3_sc2_cg1.jpg',
                   'label': '1/4 Opening: Aether Escorting a Blushing Furina by the Hand into the'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s3_sc2_cg2.jpg',
                   'label': '2/4 Developing: Furina Moving to Sit Right Beside Aether as the'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s3_sc2_cg3.jpg',
                   'label': "3/4 Climax: Furina Cradling Aether's Cheek at the Apex of the Wheel"},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s3_sc2_cg4.jpg',
                   'label': '4/4 Finale: Embracing in the Sunset Ferris Wheel Gondola as Official'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Shared a heartfelt romantic confession with Furina at the apex of the Santa Maria Ferris '
                'wheel at golden sunset.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s3_sc2_cg1.jpg',
             'scene_label': '1/4 Opening: Aether Escorting a Blushing Furina by the Hand into the',
             'scene_progress': 'SCENE 1/4',
             'narration': 'At the Santa Maria boardwalk pier as the sun paints the sky in rose-gold and '
                          'violet, you escort a blushing Furina by the hand into a private glass Ferris '
                          'wheel gondola.',
             'inner_thought': "Salon Solitaire's Whisper: Inside this glass gondola rising above the ocean, "
                              "it's just Aether and me...",
             'action_cue': 'Leaves the opposite bench and sits right beside you on the same cushioned seat '
                           'as the cabin climbs.',
             'speaker_line': "Look how high we're rising above the pier lights, Aether! Though I'll let you "
                             "in on a secret... I didn't ask to ride the Ferris wheel at sunset just for the "
                             'scenery.',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Put your arm behind her shoulders & tell her you only have eyes for her',
                          'player_text': "I didn't get on this Ferris wheel for the scenery either, Furina - "
                                         'the only view I wanted at sunset is sitting right next to me.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Blushes warmly and leans into your arm as the gondola climbs '
                                             'higher.',
                          'reaction_reply': 'Aether...'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hold her hand on the bench as the cabin rises toward the top',
                          'player_text': 'Sitting right beside you at golden hour beats any view in San '
                                         'Andreas.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "Hehe, I was hoping you'd say that!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s3_sc2_cg2.jpg',
             'scene_label': '2/4 Developing: Furina Moving to Sit Right Beside Aether as the',
             'scene_progress': 'SCENE 2/4',
             'narration': 'As your glass cabin reaches the very apex of the Ferris wheel, golden sunset '
                          'light floods the interior. Furina turns toward you and gently cradles your cheek '
                          'in her warm, ungloved palm.',
             'inner_thought': "Salon Solitaire's Whisper: No stage cues, no hiding behind bravado - I want "
                              'Aether to know that my whole heart belongs to him.',
             'action_cue': 'Cradles your cheek tenderly with her bare hand, her cyan-and-navy eyes '
                           'shimmering with deep love.',
             'speaker_line': 'In every story I ever read or directed, I used to wonder what true love felt '
                             'like... until you walked into my life and showed me. Tell me, Aether - will '
                             'you be my leading man not on a stage, but in real life, as my boyfriend?',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Cover her hand on your cheek & confess your love wholeheartedly',
                          'player_text': 'I fell in love with you a long time ago, Furina - your courage, '
                                         'your laugh, and every quiet moment we share. I want you as my '
                                         'girlfriend, now and always.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Joyful tears sparkle on her lashes before she throws both arms '
                                             'around your neck.',
                          'reaction_reply': 'Yes!! A thousand times yes, my beloved Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Pull her into your embrace & tell her your heart belongs to her',
                          'player_text': "You're the most special girl in my world, Furina. My heart is "
                                         'completely yours.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'And mine belongs only to you, Aether - forever!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s3_sc2_cg3.jpg',
             'scene_label': "3/4 Climax: Furina Cradling Aether's Cheek at the Apex of the Wheel",
             'scene_progress': 'SCENE 3/4',
             'narration': 'As the Ferris wheel slowly descends toward the glowing pier below, Furina stays '
                          'curled happily in your arms, pressing a soft, lingering kiss to your cheek.',
             'inner_thought': "Salon Solitaire's Whisper: We're officially lovers! My heart feels lighter "
                              'than a Hydro bubble floating into the stars!',
             'action_cue': 'Kisses your cheek tenderly and laces her fingers with yours.',
             'speaker_line': "From this sunset onward, no rewrites and no understudies allowed, okay? You're "
                             'officially my boyfriend, Aether!',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Kiss her lips softly before the gondola doors open',
                          'player_text': "No rewrites ever, my love. Come on, let's celebrate our first "
                                         'evening as an official couple!',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Touches her lips with a radiant, lovestruck blush.',
                          'reaction_reply': 'Best sunset of my entire life, mon amour!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Walk off the Ferris wheel hand-in-hand as a couple',
                          'player_text': "Official and permanent, Furina! Let's go celebrate on the pier!",
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, lead the way, boyfriend!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s3_sc3',
  'char_id': 'furina',
  'stage': 3,
  'order': 3,
  'scenario_num': 3,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 3 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Waltz of the Little Oceanid on the Dock',
  'subtitle': 'Stage 3 - Episode 3 - Starlit Hydro Dance',
  'location': 'Bayside Marina Wooden Pier',
  'cg_url': '/dating-media/furina_s3_sc3_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s3_sc3_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Holding Furina by the Waist & Touching Foreheads Under',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s3_sc3_cg1.jpg',
                   'label': '1/4 Opening: Starlit Rendezvous at the Quiet Bayside Marina Wooden'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s3_sc3_cg2.jpg',
                   'label': '2/4 Developing: Furina Stepping Barefoot onto Shimmering Hydro'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s3_sc3_cg3.jpg',
                   'label': '3/4 Climax: Slow-Dancing Together Over Glowing Water Surrounded by'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s3_sc3_cg4.jpg',
                   'label': '4/4 Finale: Holding Furina by the Waist & Touching Foreheads Under'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Slow-danced with Furina over glowing starlit water at Bayside Marina surrounded by Salon '
                'Solitaire.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s3_sc3_cg1.jpg',
             'scene_label': '1/4 Opening: Starlit Rendezvous at the Quiet Bayside Marina Wooden',
             'scene_progress': 'SCENE 1/4',
             'narration': 'At the quiet Bayside Marina wooden pier under a velvet night sky, Furina slips '
                          'off her shoes at the edge of the dock and steps lightly onto the calm bay water - '
                          'her Hydro Vision making luminescent blue ripples bloom beneath her feet.',
             'inner_thought': "Salon Solitaire's Whisper: Dancing on the water under the stars with "
                              'Aether... I want to share my most magical side with him.',
             'action_cue': 'Turns on the glowing surface of the water and extends her hand toward you on the '
                           'dock with an enchanting smile.',
             'speaker_line': 'Look, Aether - the bay is calm as glass tonight, and Mademoiselle Crabaletta, '
                             'Chevalmarin, and Usher are providing the starlight bubbles! Care to join me '
                             'for a midnight waltz?',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Take her hand, step close to the water's edge & pull her into a waltz",
                          'player_text': 'How could I ever refuse a midnight waltz with the Regina of All '
                                         'Waters? Come into my arms, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Glides into your arms at the low dock edge, her hand resting '
                                             'warmly on your shoulder.',
                          'reaction_reply': 'Hehe, hold me steady around the waist, my prince!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': "Take her hand warmly & hum the melody of 'The Little Oceanid'",
                          'player_text': "I'll hum the melody while we dance, Furina - lead the first step!",
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'You remember every note of my song, Aether!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s3_sc3_cg2.jpg',
             'scene_label': '2/4 Developing: Furina Stepping Barefoot onto Shimmering Hydro',
             'scene_progress': 'SCENE 2/4',
             'narration': 'As you sway together in a slow, romantic waltz along the water-skimming dock, '
                          "Salon Solitaire's luminous Hydro bubbles drift around the two of you like "
                          'floating starlight lanterns.',
             'inner_thought': "Salon Solitaire's Whisper: His arm around my waist feels so strong and "
                              "warm... I feel like I'm floating on air instead of water!",
             'action_cue': 'Rests her cheek against your chest as you spin her gently through the glowing '
                           'blue droplets.',
             'speaker_line': "You know, in the fairy tale of 'The Little Oceanid,' Clio couldn't stay beside "
                             "the one she loved... Aren't you glad our real story has a much happier script, "
                             'Aether?',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Hold her closer by the waist & whisper that you'll never be parted",
                          'player_text': 'In our story, Furina, nothing in any world will ever separate us - '
                                         'we write our own happy ending every single day.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Gazes up at you with shining heterochromia eyes, her breath '
                                             'warm against your collarbone.',
                          'reaction_reply': 'Aether... when you hold me like this, I believe in forever.'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Spin her gently into a close embrace under the stars',
                          'player_text': 'Our story only has happy chapters ahead, my love.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "And we're going to dance through every single one of them!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s3_sc3_cg3.jpg',
             'scene_label': '3/4 Climax: Slow-Dancing Together Over Glowing Water Surrounded by',
             'scene_progress': 'SCENE 3/4',
             'narration': 'As the waltz slows to a gentle pause over the starlit water, you hold Furina by '
                          'the waist and rest your forehead tenderly against hers.',
             'inner_thought': "Salon Solitaire's Whisper: Our foreheads are touching and his lips are right "
                              'there in the starlight...',
             'action_cue': 'Closes her eyes softly with her hands resting over your heart, leaning her '
                           'forehead against yours.',
             'speaker_line': "Mmm... my heart is still dancing even though our feet stopped, Aether. Don't "
                             'let go of my waist yet, okay?',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Tilt her chin up gently & press a soft, romantic kiss to her lips',
                          'player_text': "I'm not letting go, my love - not tonight, not ever.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': "Melts into the starlit kiss at the water's edge, her arms "
                                             'wrapping tightly around your neck.',
                          'reaction_reply': 'Best midnight waltz in the universe, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hold her close against your heart under the marina stars',
                          'player_text': 'Stay right here in my arms as long as you want, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'My favorite place in all the world!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s3_sc4',
  'char_id': 'furina',
  'stage': 3,
  'order': 4,
  'scenario_num': 4,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 3 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Jealous Crabaletta & The Velvet Box Seat',
  'subtitle': 'Stage 3 - Episode 4 - Grand Opera VIP Box',
  'location': 'Los Santos Grand Opera House VIP Box',
  'cg_url': '/dating-media/furina_s3_sc4_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s3_sc4_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Walking Out of the Opera House Arm-in-Arm with Radiant',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s3_sc4_cg1.jpg',
                   'label': '1/4 Opening: Sharing a Velvet VIP Box Seat at the Grand Opera House'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s3_sc4_cg2.jpg',
                   'label': "2/4 Developing: Jealous Furina Pouting Adorably & Tugging Aether's"},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s3_sc4_cg3.jpg',
                   'label': '3/4 Climax: Furina Standing on Tiptoes in the VIP Box to Steal a'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s3_sc4_cg4.jpg',
                   'label': '4/4 Finale: Walking Out of the Opera House Arm-in-Arm with Radiant'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Shared a private velvet VIP opera box with Furina as she playfully claimed exclusive rights '
                'to your attention and stole a cheek kiss.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s3_sc4_cg1.jpg',
             'scene_label': '1/4 Opening: Sharing a Velvet VIP Box Seat at the Grand Opera House',
             'scene_progress': 'SCENE 1/4',
             'narration': 'During intermission at the Grand Opera House, you and Furina relax in a private '
                          'crimson-velvet VIP balcony box. When an usher downstairs waves politely toward '
                          'you from the lobby, Furina immediately puffs her cheeks in adorable jealousy.',
             'inner_thought': "Salon Solitaire's Whisper: Did that actress in the lobby just wink at MY "
                              'Aether?! Unacceptable! Mademoiselle Crabaletta, close the velvet box curtains '
                              'immediately!',
             'action_cue': 'Tugs the red velvet privacy curtain half-shut and pokes your chest with a cute, '
                           'possessive pout.',
             'speaker_line': 'Ahem! Full disclosure, Aether: I saw that girl in the lobby smiling at you for '
                             'three whole seconds too long! Just so there is zero confusion in the theater '
                             'tonight - who are you here with?',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Laugh fondly, pull her into your lap on the velvet settee & kiss her',
                          'player_text': 'Are you jealous, my cute Director? You never have to worry - '
                                         "you're the only star in this theater or anywhere else in my eyes.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Melts instantly in your lap, hiding a thrilled blush behind '
                                             'her fan.',
                          'reaction_reply': "H-Hmph! I wasn't jealous, I was merely enforcing VIP box "
                                            'exclusivity! ...Though hearing you say that while holding me is '
                                            'very acceptable!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Take her hand & reassure her that your eyes are only on her',
                          'player_text': 'My eyes - and my VIP seat - belong 100% to you tonight and always, '
                                         'Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Good answer! Approved by both me and Mademoiselle Crabaletta!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s3_sc4_cg2.jpg',
             'scene_label': "2/4 Developing: Jealous Furina Pouting Adorably & Tugging Aether's",
             'scene_progress': 'SCENE 2/4',
             'narration': 'With the velvet box curtains drawn for privacy before the second act begins, '
                          'Furina stays nestled close beside you on the settee, tracing the gold trim on '
                          'your scarf.',
             'inner_thought': "Salon Solitaire's Whisper: Sitting this close in a private opera box with "
                              "Aether's arm around my waist...",
             'action_cue': 'Looks up at you from under her lashes with a playful, affectionate glint in her '
                           'cyan-and-navy eyes.',
             'speaker_line': 'Since you passed my jealousy inspection with flying colors, Aether... bend '
                             'down a little bit so I can give my leading man his official VIP stamp of '
                             'ownership!',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Lean down close & let her claim you properly',
                          'player_text': 'Right here, my love - stamp away so the whole world knows I belong '
                                         'to Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Stands up on her knees on the velvet sofa and presses a warm, '
                                             'lingering kiss right onto your cheek.',
                          'reaction_reply': 'There! Marked by Lady Furina herself!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Smile & tilt your cheek toward her in the dim box light',
                          'player_text': 'All yours, Director Furina!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Kisses your cheek with a happy giggle.',
                          'reaction_reply': 'Hehe, officially mine!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s3_sc4_cg3.jpg',
             'scene_label': '3/4 Climax: Furina Standing on Tiptoes in the VIP Box to Steal a',
             'scene_progress': 'SCENE 3/4',
             'narration': 'As the orchestra begins the second act below, Furina intertwines her fingers with '
                          'yours and whispers softly against your ear.',
             'inner_thought': "Salon Solitaire's Whisper: I want our next date to be somewhere completely "
                              'private - just Aether and me at my mansion after hours.',
             'action_cue': 'Rests her flushed cheek against your shoulder in the dim velvet box, whispering '
                           'near your ear.',
             'speaker_line': "Hey, Aether... next time we go out at night, let's skip the public theater and "
                             'have a private late-night rendezvous at my Richman terrace instead, okay?',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Squeeze her hand & promise a private late-night date at her mansion',
                          'player_text': "It's a promise, my love - next time, the whole night belongs to "
                                         'just the two of us at your place.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Smiles alluringly and kisses your jawline.',
                          'reaction_reply': "I'll wear my new sapphire evening gown just for you, Aether!"},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': "Whisper back that you can't wait for a private evening together",
                          'player_text': "I'd love that, Furina - just you and me after hours.",
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "Can't wait, mon amour!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s4_sc1',
  'char_id': 'furina',
  'stage': 4,
  'order': 1,
  'scenario_num': 1,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 4 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Sapphire Gown on the Moonlit Balcony',
  'subtitle': 'Stage 4 - Episode 1 - Mansion Terrace Romance',
  'location': "Furina's Richman Mansion Balcony",
  'cg_url': '/dating-media/furina_s4_sc1_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s4_sc1_cg4.jpg',
  'ending_scene_label': "4/4 Finale: Furina Resting Blissfully in Aether's Lap on the Terrace",
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s4_sc1_cg1.jpg',
                   'label': '1/4 Opening: Furina in Her Sapphire Off-Shoulder Evening Gown'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s4_sc1_cg2.jpg',
                   'label': '2/4 Developing: Swaying Closely in a Moonlit Balcony Slow Dance with'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s4_sc1_cg3.jpg',
                   'label': '3/4 Climax: Sharing a Deep, Passionate Moonlit Kiss on the Marble'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s4_sc1_cg4.jpg',
                   'label': "4/4 Finale: Furina Resting Blissfully in Aether's Lap on the Terrace"}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Danced closely with Furina in her sapphire off-shoulder evening gown on her moonlit Richman '
                'terrace and shared a deep, passionate kiss.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s4_sc1_cg1.jpg',
             'scene_label': '1/4 Opening: Furina in Her Sapphire Off-Shoulder Evening Gown',
             'scene_progress': 'SCENE 1/4',
             'narration': "Stepping through the French doors onto Furina's candlelit Richman Mansion balcony "
                          'overlooking the sparkling city lights of Los Santos, your breath catches as '
                          'Furina turns to greet you in a figure-hugging sapphire-and-pearl off-shoulder '
                          'evening gown.',
             'inner_thought': "Salon Solitaire's Whisper: I wore this Chioriya sapphire gown tonight solely "
                              "to take Aether's breath away...",
             'action_cue': 'Smooths the silk skirt of her off-shoulder sapphire gown and steps toward you '
                           'with a sultry, blushing smile.',
             'speaker_line': 'Welcome to our private premiere, mon amour! I had Chiori tailor this sapphire '
                             "dress specifically for tonight... Well? Don't keep a lady in suspense - how do "
                             'I look, Aether?',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Pull her close by the waist & whisper that she looks breathtaking',
                          'player_text': 'You look breathtaking, Furina - like the most enchanting goddess '
                                         "under the moonlight, and I can't take my eyes off you.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Shivers happily as your hands settle on her bare waist, her '
                                             'cheeks glowing rose-pink.',
                          'reaction_reply': 'Hearing that in your low voice makes every minute of dressing '
                                            'up worth it, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Take her hand & kiss her fingertips like a devoted gentleman',
                          'player_text': 'That sapphire gown is stunning on you, my love - you outshine '
                                         'every star over Los Santos tonight.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, my silver-tongued leading man always knows how to make me '
                                            'melt!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s4_sc1_cg2.jpg',
             'scene_label': '2/4 Developing: Swaying Closely in a Moonlit Balcony Slow Dance with',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Soft violin music drifts from the gramophone inside her suite as you draw Furina '
                          'into a slow, intimate dance on the marble balcony, her bare shoulder warm beneath '
                          'your fingertips.',
             'inner_thought': "Salon Solitaire's Whisper: Swaying against Aether's chest under the moonlight "
                              'with his hand on my waist... I want to melt completely into his arms.',
             'action_cue': 'Wraps her arms around your neck and gazes up into your golden eyes from only '
                           'inches away.',
             'speaker_line': "When we danced on the pier, I thought my heart couldn't beat any faster... Yet "
                             'tonight, feeling your hand against my waist in this dress makes me feel '
                             'delightfully dizzy, Aether.',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Draw her flush against your chest & trace her jawline tenderly',
                          'player_text': "Then lean on me completely, Furina - I've got you, and tonight "
                                         'belongs only to the two of us.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Her eyelids flutter half-closed as she leans her warm cheek '
                                             'into your palm.',
                          'reaction_reply': 'Aether... kiss me right now, please...'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hold her close as you sway together in the moonlight',
                          'player_text': 'You feel so warm and delicate in my arms tonight, my love.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Only for you, my beloved Traveler!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s4_sc1_cg3.jpg',
             'scene_label': '3/4 Climax: Sharing a Deep, Passionate Moonlit Kiss on the Marble',
             'scene_progress': 'SCENE 3/4',
             'narration': "Beneath the silver moonlight and floating Hydro droplets, you tilt Furina's chin "
                          'up and capture her lips in a deep, passionate kiss before resting together on the '
                          'cushioned terrace chaise.',
             'inner_thought': "Salon Solitaire's Whisper: His kiss is so warm and intoxicating... I never "
                              'want this night to end.',
             'action_cue': 'Parts from the deep kiss breathless and radiant, curling up blissfully across '
                           'your lap on the velvet terrace chaise.',
             'speaker_line': "Mmm... if every night on this balcony feels like that kiss, Aether, I don't "
                             "think I'll ever let you go home.",
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Hold her in your lap & kiss her bare shoulder softly',
                          'player_text': "You don't ever have to let me go home, my love - my favorite place "
                                         'is right here holding you.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Nestles against your collarbone with a dreamy sigh.',
                          'reaction_reply': 'Stay with me all night, mon amour!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Wrap your cape around the two of you on the chaise under the stars',
                          'player_text': "I'm staying right here with you under the stars tonight, Furina.",
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Best private premiere ever, Aether!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s4_sc2',
  'char_id': 'furina',
  'stage': 4,
  'order': 2,
  'scenario_num': 2,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 4 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Silk Camisole & Brushing Her Long Hair',
  'subtitle': 'Stage 4 - Episode 2 - Private Bedroom Intimacy',
  'location': "Furina's Master Bedroom Suite",
  'cg_url': '/dating-media/furina_s4_sc2_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s4_sc2_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Cuddling Closely Under the Canopy Bed Covers Listening',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s4_sc2_cg1.jpg',
                   'label': '1/4 Opening: After-Bath Furina in a Royal-Blue Silk Camisole Sitting'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s4_sc2_cg2.jpg',
                   'label': '2/4 Developing: Aether Sitting Behind Furina on the Bed Gently'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s4_sc2_cg3.jpg',
                   'label': "3/4 Climax: Aether Pressing a Warm Kiss to Furina's Bare Shoulder as"},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s4_sc2_cg4.jpg',
                   'label': '4/4 Finale: Cuddling Closely Under the Canopy Bed Covers Listening'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': "Dried and brushed Furina's long Ousia/Pneuma hair in her private bedroom while she wore a "
                'royal-blue silk camisole, before cuddling under the canopy covers.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s4_sc2_cg1.jpg',
             'scene_label': '1/4 Opening: After-Bath Furina in a Royal-Blue Silk Camisole Sitting',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Fresh from a warm evening bath scented with Romaritime flower oil, Furina sits on '
                          'the edge of her canopy bed wearing a delicate royal-blue silk camisole and '
                          'matching lace robe, her long white-and-blue Pneuma hair cascading damply down her '
                          'back.',
             'inner_thought': "Salon Solitaire's Whisper: Nobody else has ever seen me right after a bath in "
                              'silk loungewear with my hair all the way down...',
             'action_cue': 'Holds out a plush towel and a pearl-inlaid hairbrush toward you with a shy, '
                           'alluring blush.',
             'speaker_line': "My long Pneuma hair always takes forever to dry after a bath... Since you're "
                             'staying over tonight, Aether, would you sit behind me on the bed and help me '
                             'dry and brush it?',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Sit right behind her on the bed & gently wrap the warm towel around her',
                          'player_text': 'Come here, my love - sit right between my knees and relax while I '
                                         'dry and brush every strand for you.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Settles between your knees on the soft mattress with a '
                                             'contented shiver.',
                          'reaction_reply': 'Mmm... your hands are so warm and gentle, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Take the pearl hairbrush & smile affectionately',
                          'player_text': "I'd love to, Furina. Just lean back and let me pamper you tonight.",
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, being pampered by my boyfriend is the ultimate luxury!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s4_sc2_cg2.jpg',
             'scene_label': '2/4 Developing: Aether Sitting Behind Furina on the Bed Gently',
             'scene_progress': 'SCENE 2/4',
             'narration': 'As you slowly draw the pearl brush through her silky, glowing locks, the lace '
                          'robe slips slightly off her porcelain shoulder. Furina tilts her head back '
                          'against your chest, looking up at you upside-down with half-lidded heterochromia '
                          'eyes.',
             'inner_thought': "Salon Solitaire's Whisper: Every stroke of the brush feels like a caress... "
                              "and feeling Aether's breath near my neck is making my whole body tingle.",
             'action_cue': 'Reaches back to touch your wrist lightly as her silk strap slides slightly down '
                           'her warm shoulder.',
             'speaker_line': "Aether... you're brushing so gently I feel like I'm floating. Are you admiring "
                             'my hair... or are you staring at my shoulder in the mirror?',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Lean down & press a slow, warm kiss to her bare shoulder',
                          'player_text': 'Both - your hair is like spun starlight, and your shoulder was '
                                         'begging to be kissed, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Lets out a soft, breathless gasp as your lips brush her skin, '
                                             'her fingers tightening on your knee.',
                          'reaction_reply': 'A-Aether...! When you kiss my shoulder like that, my knees go '
                                            'completely weak...'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Whisper against her ear that every inch of her is gorgeous',
                          'player_text': 'Every single thing about you tonight is captivating, my love.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Mmm... you really know how to make my heart melt, mon amour!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s4_sc2_cg3.jpg',
             'scene_label': "3/4 Climax: Aether Pressing a Warm Kiss to Furina's Bare Shoulder as",
             'scene_progress': 'SCENE 3/4',
             'narration': 'Setting the pearl brush on the nightstand now that her hair is dry and fragrant, '
                          'Furina turns around on the mattress and slides under the silk canopy covers, '
                          'holding the blanket open for you.',
             'inner_thought': "Salon Solitaire's Whisper: I want to fall asleep wrapped in Aether's arms "
                              'listening to his heartbeat...',
             'action_cue': 'Pats the pillow right beside hers and looks at you with tender, lovestruck eyes.',
             'speaker_line': 'My hair is dry, the rain is tapping against the window, and this canopy bed is '
                             'way too big for one person... Come hold me under the covers, Aether.',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Slide under the silk covers & pull her flush against your chest',
                          'player_text': 'Right here, sweetheart. Rest your head on my chest and let me hold '
                                         'you all night.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Curls securely into your embrace, pressing her lips to your '
                                             'collarbone.',
                          'reaction_reply': 'Goodnight, my beloved Aether... I love you so much.'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Gather her into your arms & kiss her forehead tenderly',
                          'player_text': 'Nothing beats holding you close like this, Furina. Sweet dreams, '
                                         'my love.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "Sweetest dreams in the world as long as you're holding me!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s4_sc3',
  'char_id': 'furina',
  'stage': 4,
  'order': 3,
  'scenario_num': 3,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 4 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Starlit Thermal Spring & Romaritime Petals',
  'subtitle': 'Stage 4 - Episode 3 - Cliffside Private Onsen',
  'location': 'Bayside Private Cliffside Thermal Spring',
  'cg_url': '/dating-media/furina_s4_sc3_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s4_sc3_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Wrapped in Matching Silk Robes on the Veranda Sharing',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s4_sc3_cg1.jpg',
                   'label': '1/4 Opening: Arriving Together at the Private Cliffside Starlit'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s4_sc3_cg2.jpg',
                   'label': '2/4 Developing: Furina Floating Blue Romaritime Petals Across the'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s4_sc3_cg3.jpg',
                   'label': '3/4 Climax: Sitting Side-by-Side in the Steaming Spring as Furina'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s4_sc3_cg4.jpg',
                   'label': '4/4 Finale: Wrapped in Matching Silk Robes on the Veranda Sharing'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Shared a private starlit thermal spring bath scattered with glowing blue Romaritime petals '
                'with Furina overlooking the ocean.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s4_sc3_cg1.jpg',
             'scene_label': '1/4 Opening: Arriving Together at the Private Cliffside Starlit',
             'scene_progress': 'SCENE 1/4',
             'narration': 'High on a secluded cliff overlooking the moonlit ocean, warm mineral mist rises '
                          'from a private open-air thermal spring. Wearing a tasteful sapphire bath wrap '
                          'with her hair pinned up by a pearl clip, Furina tests the water with her toes '
                          'before looking back at you.',
             'inner_thought': "Salon Solitaire's Whisper: A private cliffside hot spring under the stars "
                              'with just Aether and me... my heart is racing faster than the ocean tide!',
             'action_cue': 'Steps into the crystal-clear steaming pool and scatters glowing blue Romaritime '
                           'flower petals across the surface.',
             'speaker_line': 'The water temperature is absolute perfection, Aether - and I brought fresh '
                             "Fontaine Romaritime petals so the whole spring smells like home! Don't just "
                             'stand by the rocks, come join me in the water!',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Step into the warm spring beside her & draw her close through the '
                                   'floating',
                          'player_text': "Wild horses couldn't keep me away, Furina - especially with you "
                                         'looking this stunning in the starlight.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Glides into your arms in the warm water, her wet shoulders '
                                             'glistening in the lantern glow.',
                          'reaction_reply': "Ooh, the water feels twice as warm when you're holding me!"},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Join her in the steaming pool & admire the ocean view together',
                          'player_text': 'Between the warm spring, the flower petals, and you, this is '
                                         'paradise, my love.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Our very own secret Fontaine oasis!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s4_sc3_cg2.jpg',
             'scene_label': '2/4 Developing: Furina Floating Blue Romaritime Petals Across the',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Floating blue petals drift around the two of you as Furina settles onto the '
                          'submerged stone bench right against your side, resting her flushed cheek on your '
                          'bare shoulder.',
             'inner_thought': "Salon Solitaire's Whisper: Being this close to Aether in the warm spring "
                              'water makes every bit of stress melt away...',
             'action_cue': 'Traces a glowing droplet of water along your collarbone with her fingertip.',
             'speaker_line': "You know, as the Hydro Archon's human half, water was always my element... yet "
                             'I never knew water could feel this soothing and romantic until I shared it '
                             'with you, Aether.',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Wrap your arm around her wet shoulders & kiss her flushed cheek',
                          'player_text': 'Every element in the world feels warmer when we share it together, '
                                         'Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Turns her face to meet your lips in a tender, steam-veiled '
                                             'kiss.',
                          'reaction_reply': "Mmm... careful, mon amour, or I'll make the spring bubble over "
                                            'with Hydro hearts!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Gently scoop warm petal-scented water over her shoulders',
                          'player_text': 'Relax completely in my arms tonight, my love - you deserve all the '
                                         'peace in the world.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "With you holding me, I've never felt more at peace."},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s4_sc3_cg3.jpg',
             'scene_label': '3/4 Climax: Sitting Side-by-Side in the Steaming Spring as Furina',
             'scene_progress': 'SCENE 3/4',
             'narration': 'After soaking under the stars, the two of you sit on the wooden veranda in '
                          'matching silk robes, sharing chilled Fonta and fresh strawberries as the night '
                          'breeze cools your skin.',
             'inner_thought': "Salon Solitaire's Whisper: Sharing cold Fonta and strawberries in matching "
                              'robes after our bath... I want every weekend to be just like this.',
             'action_cue': 'Leans her damp head against your shoulder on the veranda and holds a sweet '
                           'strawberry to your lips.',
             'speaker_line': 'Cold Fonta and fresh strawberries right after a hot spring soak with my '
                             'favorite person! Take a bite, Aether - my treat!',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Eat the strawberry from her fingers & kiss her sweet lips',
                          'player_text': 'The strawberry is sweet, Furina, but kissing you afterward is even '
                                         'sweeter.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Giggles breathlessly against your lips.',
                          'reaction_reply': 'Best cliffside getaway ever, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Clink your Fonta glass with hers & enjoy the strawberry',
                          'player_text': 'To many more starlit getaways together, my love!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Cheers to us, my eternal co-star!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s4_sc4',
  'char_id': 'furina',
  'stage': 4,
  'order': 4,
  'scenario_num': 4,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 4 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'The Brass Key to Her Richman Sanctuary',
  'subtitle': 'Stage 4 - Episode 4 - Co-Habitation Promise',
  'location': "Furina's Richman Mansion Entrance & Foye",
  'cg_url': '/dating-media/furina_s4_sc4_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s4_sc4_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Aether Carrying a Laughing, Blushing Furina Across the',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s4_sc4_cg1.jpg',
                   'label': '1/4 Opening: Furina Presenting a Brass Mansion Key Tied with a Blue'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s4_sc4_cg2.jpg',
                   'label': '2/4 Developing: Aether Closing His Hand Over the Key & Pulling'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s4_sc4_cg3.jpg',
                   'label': '3/4 Climax: Unlocking Her Richman Mansion Front Door Together'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s4_sc4_cg4.jpg',
                   'label': '4/4 Finale: Aether Carrying a Laughing, Blushing Furina Across the'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': "Accepted the brass key tied with a blue Romaritime ribbon to Furina's Richman Mansion and "
                'carried her across the threshold bridal-style.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s4_sc4_cg1.jpg',
             'scene_label': '1/4 Opening: Furina Presenting a Brass Mansion Key Tied with a Blue',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Standing beneath the warm chandelier of her Richman Mansion porch after a '
                          'romantic dinner date, Furina reaches into her velvet purse and holds out a small '
                          'velvet box tied with a blue satin ribbon.',
             'inner_thought': "Salon Solitaire's Whisper: I had a duplicate brass key forged and polished "
                              'all week for this exact moment...',
             'action_cue': 'Opens the velvet box in both hands, revealing a gleaming brass mansion key tied '
                           'with a Romaritime-blue ribbon.',
             'speaker_line': 'Aether... my mansion used to be just a quiet place where I hid from the '
                             "spotlight. Now, every room only feels alive when you're here with me. I want "
                             'you to have your own key - so my home is officially OUR home.',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Close your hands warmly over hers & accept the key with deep devotion',
                          'player_text': 'Nothing would make me happier, Furina. Wherever you are has always '
                                         "been my true home - and I'll cherish this key with all my heart.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Tears of pure joy shimmer in her heterochromia eyes as she '
                                             'throws her arms around your neck.',
                          'reaction_reply': "Aether!! Hearing you call my place 'our home' makes me the "
                                            'happiest girl in Teyvat and San Andreas!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Slip the ribboned brass key onto your chain & kiss her forehead',
                          'player_text': "Thank you for trusting me with your sanctuary, my love - I'll be "
                                         'coming home to you every single day.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "And I'll be waiting with open arms and warm tea every evening!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s4_sc4_cg2.jpg',
             'scene_label': '2/4 Developing: Aether Closing His Hand Over the Key & Pulling',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Holding the ribboned brass key together, you guide it into the front door lock - '
                          "your hand covering Furina's as the bolt clicks open with a welcoming chime.",
             'inner_thought': "Salon Solitaire's Whisper: Unlocking the door together hand-in-hand... it "
                              "feels like we're starting a whole new life together!",
             'action_cue': 'Places her hand over yours on the brass key and looks up at you with a radiant, '
                           'blushing smile.',
             'speaker_line': 'Click! Just like that, you have permanent VIP backstage and bedroom access '
                             'twenty-four hours a day, my love!',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Sweep her off her feet into a bridal carry right at the open doorway',
                          'player_text': 'In the finest romantic traditions, a new chapter at home requires '
                                         'carrying my leading lady across the threshold!',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Squeals with delighted laughter, wrapping both arms tightly '
                                             'around your shoulders as you lift her effortlessly.',
                          'reaction_reply': 'Kyaa - Aether!! Carrying me bridal-style like a storybook '
                                            'prince?!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Open the door wide & pull her into a warm embrace in the foyer',
                          'player_text': 'Welcome home, my love - now and always.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Welcome home to US, Aether!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s4_sc4_cg3.jpg',
             'scene_label': '3/4 Climax: Unlocking Her Richman Mansion Front Door Together',
             'scene_progress': 'SCENE 3/4',
             'narration': 'Carrying a laughing, blushing Furina across the marble foyer and up toward the '
                          'plush living room sofa, she presses a shower of affectionate kisses along your '
                          'cheek and neck.',
             'inner_thought': "Salon Solitaire's Whisper: Being carried in Aether's strong arms inside our "
                              'home... my heart is overflowing!',
             'action_cue': 'Rests her forehead against yours as you set her gently down on the velvet sofa, '
                           'keeping her arms looped around your neck.',
             'speaker_line': 'Since this is officially our first night with you holding a house key, '
                             'Aether... the doors stay locked until morning, deal?',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Kiss her deeply & stay wrapped in each other's arms on the sofa",
                          'player_text': 'Deal, my love - nowhere else in the world exists tonight except '
                                         'right here with you.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Melts into your kiss with a blissful sigh.',
                          'reaction_reply': 'Welcome home forever, mon amour!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hold her close & celebrate your first night sharing a home key',
                          'player_text': 'Locked until morning, Furina - tonight is all ours!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Best housewarming celebration in history!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s5_sc1',
  'char_id': 'furina',
  'stage': 5,
  'order': 1,
  'scenario_num': 1,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 5 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Golden Riviera Cove & Sapphire Swimsuit',
  'subtitle': 'Stage 5 - Episode 1 - Private Beach Getaway',
  'location': 'Santa Maria Private Riviera Cove',
  'cg_url': '/dating-media/furina_s5_sc1_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s5_sc1_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Cuddling by the Starlit Beach Bonfire as Ocean Waves',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s5_sc1_cg1.jpg',
                   'label': "1/4 Opening: Aether Gently Applying Sunscreen to Furina's Shoulders"},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s5_sc1_cg2.jpg',
                   'label': '2/4 Developing: Furina in Her Sapphire Halter Swimsuit Leaping into'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s5_sc1_cg3.jpg',
                   'label': '3/4 Climax: Passionate Sunset Embrace on the Beach Towel Wrapped in'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s5_sc1_cg4.jpg',
                   'label': '4/4 Finale: Cuddling by the Starlit Beach Bonfire as Ocean Waves'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Spent an intimate golden-hour getaway with Furina in her sapphire halter swimsuit at a '
                'private Riviera cove, embracing in the surf and cuddling by a starlit bonfire.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s5_sc1_cg1.jpg',
             'scene_label': "1/4 Opening: Aether Gently Applying Sunscreen to Furina's Shoulders",
             'scene_progress': 'SCENE 1/4',
             'narration': 'At a secluded golden-sand cove tucked beneath the Santa Maria cliffs, Furina '
                          'unties her sheer white beach pareo - revealing a glamorous sapphire-and-pearl '
                          'two-piece halter swimsuit with golden hydro-droplet clasps that highlight her '
                          'graceful silhouette.',
             'inner_thought': "Salon Solitaire's Whisper: I bought this sapphire two-piece exclusively for "
                              "Aether's eyes at our private cove...",
             'action_cue': 'Poses playfully on the sunlit beach lounger and holds out a bottle of '
                           'coconut-vanilla sunscreen with a sultry blush.',
             'speaker_line': 'Ta-da! Private beach premiere of my new sapphire swimsuit, mon amour! Since '
                             "there's nobody in this cove except the two of us, will you come put sunscreen "
                             "on my back and shoulders so I don't burn?",
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Kneel beside her lounger & massage the warm sunscreen slowly over her',
                          'player_text': 'You look dangerously gorgeous in that sapphire swimsuit, Furina. '
                                         'Turn around slightly and let me take care of every inch of your '
                                         'shoulders.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Shivers deliciously under your warm palms, looking back over '
                                             'her shoulder with half-lidded, lovestruck eyes.',
                          'reaction_reply': 'Mmm... Aether, the way your hands glide over my skin feels way '
                                            'too good to just be sun protection!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Apply the sunscreen tenderly & kiss the nape of her neck',
                          'player_text': 'Happy to oblige, my love - your skin is as soft as silk in the '
                                         'sunlight.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, your touch makes me warmer than the afternoon sun!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s5_sc1_cg2.jpg',
             'scene_label': '2/4 Developing: Furina in Her Sapphire Halter Swimsuit Leaping into',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Running hand-in-hand into the sparkling turquoise surf as golden sunset paints '
                          'the horizon, Furina splashes a playful arc of glowing Hydro droplets before '
                          'leaping straight into your arms in the waist-deep water.',
             'inner_thought': "Salon Solitaire's Whisper: Wrapped around Aether in the warm ocean waves as "
                              'the sun sets... this is pure bliss!',
             'action_cue': 'Wraps her arms around your neck and her legs lightly around your waist in the '
                           'buoyant golden surf.',
             'speaker_line': 'Got you, my Traveler! Out here in the ocean, the Regina of All Waters has '
                             "home-field advantage - and I'm holding onto you until you give me a sunset "
                             'kiss!',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Hold her securely by the waist in the glowing waves & kiss her',
                          'player_text': 'You never have to ask twice, my ocean queen - I could hold you in '
                                         'these waves forever.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Kisses you deeply as golden sunset light and glowing blue '
                                             'Hydro droplets shimmer all around you.',
                          'reaction_reply': 'Mmm... even the ocean waves are applauding us, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Spin her joyfully through the warm surf & kiss her lips',
                          'player_text': 'Best catch in the entire ocean is right here in my arms!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "And I'm never swimming away from you, mon amour!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s5_sc1_cg3.jpg',
             'scene_label': '3/4 Climax: Passionate Sunset Embrace on the Beach Towel Wrapped in',
             'scene_progress': 'SCENE 3/4',
             'narration': 'As twilight settles over the cove, you light a driftwood beach bonfire and wrap a '
                          'single oversized cashmere beach towel around both of your shoulders, pulling '
                          'Furina onto your lap by the firelight.',
             'inner_thought': "Salon Solitaire's Whisper: Wrapped in one warm towel on Aether's lap watching "
                              'the starlit waves...',
             'action_cue': 'Nestles against your chest inside the shared towel, her damp hair fragrant with '
                           'sea breeze and vanilla.',
             'speaker_line': "Warm firelight in front of us, Aether's heartbeat behind me, and the stars "
                             "over the ocean... Tell me this isn't a dream, my love.",
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Hold her tight inside the shared wrap & kiss her temple',
                          'player_text': "It's 100% real, Furina - and every summer from now on belongs to "
                                         'the two of us.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Sighs in complete contentment against your neck.',
                          'reaction_reply': 'My eternal summer with my eternal love!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Keep her warm by the firelight until the stars fill the sky',
                          'player_text': 'Real as the stars above us, sweetheart. Stay warm right here in my '
                                         'arms.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Forever and always, Aether!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s5_sc2',
  'char_id': 'furina',
  'stage': 5,
  'order': 2,
  'scenario_num': 2,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 5 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'Midnight Candlelight & Pearl Silk Suite',
  'subtitle': 'Stage 5 - Episode 2 - Alluring Boudoir Night',
  'location': "Furina's Candlelit Master Suite",
  'cg_url': '/dating-media/furina_s5_sc2_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s5_sc2_cg4.jpg',
  'ending_scene_label': "4/4 Finale: Sleeping Peacefully in Aether's Arms Under Silk Sheets",
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s5_sc2_cg1.jpg',
                   'label': '1/4 Opening: Furina in a Pearl-and-Sapphire Silk Evening Negligee'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s5_sc2_cg2.jpg',
                   'label': "2/4 Developing: Sitting Across Aether's Lap on the Velvet Sofa"},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s5_sc2_cg3.jpg',
                   'label': '3/4 Climax: Deep Candlelit Kiss Surrounded by Blue Rose Petals &'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s5_sc2_cg4.jpg',
                   'label': "4/4 Finale: Sleeping Peacefully in Aether's Arms Under Silk Sheets"}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Shared a deeply romantic, candlelit boudoir night with Furina in her pearl-and-sapphire '
                'silk negligee surrounded by blue rose petals.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s5_sc2_cg1.jpg',
             'scene_label': '1/4 Opening: Furina in a Pearl-and-Sapphire Silk Evening Negligee',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Returning to the Richman Mansion late at night, you open the master bedroom doors '
                          'to find dozens of scented candles and blue Romaritime petals leading to the sofa '
                          '- where Furina awaits in a breathtaking pearl-and-sapphire silk evening negligee '
                          'with a sheer lace shawl.',
             'inner_thought': "Salon Solitaire's Whisper: Tonight, no scripts, no shyness - I want to give "
                              'Aether all of my heart and devotion.',
             'action_cue': 'Rises from the velvet chaise with two crystal glasses of sparkling berry nectar, '
                           'her heterochromia eyes glowing softly in the candlelight.',
             'speaker_line': 'Welcome home, mon amour! I lit the candles and wore pearl silk tonight because '
                             'I wanted to celebrate how deeply in love with you I am. Come sit with me.',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Set the glasses down, pull her into your arms & kiss her neck tenderly',
                          'player_text': 'Forget the nectar for a second, Furina - seeing you in pearl silk '
                                         'by candlelight just stole every breath in my lungs.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Arches her neck softly with a breathless, enamored sigh as her '
                                             'hands slide over your chest.',
                          'reaction_reply': 'Aether... when you hold me with that look in your golden eyes, '
                                            "I'm completely at your mercy!"},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Clink glasses with a tender smile & draw her onto the velvet sofa',
                          'player_text': 'You look like an angel in candlelight, my love. Come sit right '
                                         'here in my arms.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'All yours tonight and every night, my darling!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s5_sc2_cg2.jpg',
             'scene_label': "2/4 Developing: Sitting Across Aether's Lap on the Velvet Sofa",
             'scene_progress': 'SCENE 2/4',
             'narration': 'Sitting gracefully across your lap on the candlelit sofa, Furina lets her sheer '
                          'shawl slip down to her elbows as she cradles your face in both hands, her '
                          'forehead resting against yours.',
             'inner_thought': "Salon Solitaire's Whisper: Five hundred years of loneliness were nothing "
                              'compared to the warmth of being loved by Aether like this...',
             'action_cue': 'Traces your lips with her thumb, her cheeks flushed crimson and her breath warm '
                           'against yours.',
             'speaker_line': 'Aether... thank you for teaching a former actress what real, unconditional '
                             'love feels like. Promise me that when we wake up tomorrow - and a thousand '
                             "tomorrows from now - you'll still be holding me just like this.",
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Carry her to the petal-strewn canopy bed & seal your promise with a deep',
                          'player_text': 'I promise with everything I am, Furina - tomorrow morning, and '
                                         "every morning of our lives, you'll wake up in my arms.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Wraps her arms around your neck as you lay her gently onto the '
                                             'silk pillows, kissing you with all her heart.',
                          'reaction_reply': 'I love you, Aether... hold me close all night long!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Kiss her deeply & whisper that your heart belongs only to her',
                          'player_text': 'My heart is yours for eternity, Furina - nothing will ever change '
                                         'that.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'And every beat of mine belongs to you, mon amour!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s5_sc2_cg3.jpg',
             'scene_label': '3/4 Climax: Deep Candlelit Kiss Surrounded by Blue Rose Petals &',
             'scene_progress': 'SCENE 3/4',
             'narration': 'Hours later, in the quiet glow of the last candle and the moonlit window, Furina '
                          'sleeps peacefully curled against your chest under the silk sheets, her fingers '
                          'still intertwined with yours.',
             'inner_thought': "Salon Solitaire's Whisper: (Sleeping in complete, blissful devotion in "
                              "Aether's embrace...)",
             'action_cue': 'Stirs softly against your chest, pressing a sleepy kiss to your collarbone '
                           'before smiling in her dreams.',
             'speaker_line': 'whispers softly "...Mon amour... forever yours, Aether..."',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Pull the silk comforter over her shoulders & kiss her forehead as you',
                          'player_text': 'Forever yours too, my precious Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Sleeps with a radiant, peaceful smile in your arms until dawn.',
                          'reaction_reply': ''},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hold her close against your heart through the night',
                          'player_text': "Rest peacefully, my love - I'm right here.",
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Nestles deeper into your warmth.',
                          'reaction_reply': ''},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s5_sc3',
  'char_id': 'furina',
  'stage': 5,
  'order': 3,
  'scenario_num': 3,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 5 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': "Morning Sunlight in Aether's Oversized Shirt",
  'subtitle': 'Stage 5 - Episode 3 - Sunlit Morning-After Bliss',
  'location': "Furina's Sunlit Master Bedroom & Kitchen",
  'cg_url': '/dating-media/furina_s5_sc3_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s5_sc3_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Intertwined Fingers on the Sunlit Pillow with Matching',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s5_sc3_cg1.jpg',
                   'label': "1/4 Opening: Sleepy Furina in Aether's Oversized White Shirt Pulling"},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s5_sc3_cg2.jpg',
                   'label': '2/4 Developing: Furina Feeding Aether a Fresh Strawberry Crepe Bite'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s5_sc3_cg3.jpg',
                   'label': '3/4 Climax: Aether Hugging Furina from Behind by the Sunny Bedroom'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s5_sc3_cg4.jpg',
                   'label': '4/4 Finale: Intertwined Fingers on the Sunlit Pillow with Matching'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Woke up to Furina wearing your oversized white Traveler shirt in the golden morning '
                'sunlight and shared strawberry crepes in bed.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s5_sc3_cg1.jpg',
             'scene_label': "1/4 Opening: Sleepy Furina in Aether's Oversized White Shirt Pulling",
             'scene_progress': 'SCENE 1/4',
             'narration': 'Golden morning sunlight streams through the sheer balcony curtains across the '
                          'rumpled silk sheets. When you open your eyes, you find Furina sitting up beside '
                          'you wearing your oversized white Traveler shirt - the collar slipping adorably '
                          'off one bare shoulder as she tugs your sleeve.',
             'inner_thought': "Salon Solitaire's Whisper: Wearing Aether's shirt in the morning makes me "
                              'feel wrapped in his hug even before he wakes up!',
             'action_cue': 'Tugs playfully on your hand from the sunlit pillow, her white-and-blue hair '
                           'adorably tousled.',
             'speaker_line': 'Bonjour, sleepyhead! Yes, I borrowed your white shirt this morning because it '
                             "smells like starlight and you - and no, you're not getting it back until you "
                             'give me my morning kiss!',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Pull her back down into your arms on the sunlit pillows & kiss her '
                                   'warmly',
                          'player_text': 'Keep the shirt as long as you want - because you look ten times '
                                         'cuter in it than I ever did. Good morning, my love.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Giggles happily against your lips as you roll her into a warm '
                                             'morning hug.',
                          'reaction_reply': 'Best wake-up scene in the universe! Good morning, mon amour!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Kiss her lips tenderly & brush her morning-tousled hair',
                          'player_text': 'Good morning, sweetheart - waking up to you in my shirt is the '
                                         'best view imaginable.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "Hehe, then I'll wear it every single morning!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s5_sc3_cg2.jpg',
             'scene_label': '2/4 Developing: Furina Feeding Aether a Fresh Strawberry Crepe Bite',
             'scene_progress': 'SCENE 2/4',
             'narration': 'After whipping up a tray of warm Fontaine strawberry crepes and cafe au lait '
                          'together, you bring breakfast back to the sunlit bed where Furina feeds you a '
                          'powdered-sugar crepe bite.',
             'inner_thought': "Salon Solitaire's Whisper: Breakfast in bed in Aether's shirt... domestic "
                              'bliss is a million times better than any royal palace!',
             'action_cue': 'Holds a warm strawberry-and-cream crepe bite to your lips while dangling her '
                           'bare legs happily on the mattress.',
             'speaker_line': 'Here - breakfast in bed for my five-star chef and eternal leading man! Oh, '
                             "oops - you've got a tiny speck of powdered sugar right at the corner of your "
                             'lips, Aether!',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Smile & invite her to kiss the powdered sugar off herself',
                          'player_text': 'Then my leading lady had better kiss it off for me right now.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Blushes brightly and leans in to kiss the corner of your mouth '
                                             'softly.',
                          'reaction_reply': 'Mmm... sweet as strawberries!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Savor the crepe bite & feed her a sweet strawberry in return',
                          'player_text': 'Delicious! Now open up for your strawberry, Furina!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Mmm, breakfast tastes best when we feed each other!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s5_sc3_cg3.jpg',
             'scene_label': '3/4 Climax: Aether Hugging Furina from Behind by the Sunny Bedroom',
             'scene_progress': 'SCENE 3/4',
             'narration': 'Standing together by the open sunny bedroom window overlooking the ocean horizon, '
                          'you wrap your arms around Furina from behind and rest your chin on her shoulder, '
                          'your fingers lacing with hers.',
             'inner_thought': "Salon Solitaire's Whisper: Looking out at the morning sun wrapped in Aether's "
                              'arms... my life has never been so full of light.',
             'action_cue': 'Leans back against your chest in your oversized shirt, covering your hands at '
                           'her waist.',
             'speaker_line': 'Look how bright the morning sky is, Aether... Tonight at the Opera House, I '
                             'have one final surprise rehearsal waiting for just the two of us. Promise '
                             "you'll meet me center-stage at starlight?",
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Kiss her temple & promise to meet her center-stage tonight',
                          'player_text': "I'll be there waiting for you at starlight, Furina - I wouldn't "
                                         'miss it for all the worlds in the sea of stars.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Turns in your arms for one more lingering morning kiss.',
                          'reaction_reply': 'Until tonight, my beloved Traveler!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hold her close in the morning sun & accept eagerly',
                          'player_text': 'Count on it, my love - see you center-stage tonight!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "It's going to be our greatest finale ever, Aether!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s5_sc4',
  'char_id': 'furina',
  'stage': 5,
  'order': 4,
  'scenario_num': 4,
  'is_extra_cameo': False,
  'cameo_cast': [],
  'cameo_dynamic_tier': 'Stage 5 Core Romance Scenario (Furina & Traveler Aether)',
  'allow_custom_input': True,
  'title': 'La Vaguelette: Our Eternal Final Curtain',
  'subtitle': 'Stage 5 - Episode 4 - Grand Vow on the Starlit Stage',
  'location': 'Starlit Grand Opera Stage',
  'cg_url': '/dating-media/furina_s5_sc4_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s5_sc4_cg4.jpg',
  'ending_scene_label': '4/4 Finale: Passionate Eternal-Vow Kiss Surrounded by Salon',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s5_sc4_cg1.jpg',
                   'label': '1/4 Opening: Walking Hand-in-Hand Down the Starlit Opera Aisle Under'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s5_sc4_cg2.jpg',
                   'label': '2/4 Developing: Furina Singing Her Unscripted Eternal Love Aria for'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s5_sc4_cg3.jpg',
                   'label': '3/4 Climax: Aether Slipping the Sapphire-and-Gold Promise Ring onto'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s5_sc4_cg4.jpg',
                   'label': '4/4 Finale: Passionate Eternal-Vow Kiss Surrounded by Salon'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Exchanged eternal soulmate vows and sapphire-and-gold promise rings with Furina beneath a '
                'starlit hydro canopy on the grand opera stage.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s5_sc4_cg1.jpg',
             'scene_label': '1/4 Opening: Walking Hand-in-Hand Down the Starlit Opera Aisle Under',
             'scene_progress': 'SCENE 1/4',
             'narration': 'When you step into the Grand Opera House at starlight, thousands of floating '
                          'Hydro droplets and golden starlight motes illuminate the center aisle like the '
                          'Milky Way. At center-stage stands Furina in a breathtaking white-and-sapphire '
                          'bridal-inspired opera gown, extending both hands toward you.',
             'inner_thought': "Salon Solitaire's Whisper: For five hundred years I stood on stage alone for "
                              'the sake of a prophecy... Tonight, I stand here as Furina the woman, offering '
                              'my eternity to Aether.',
             'action_cue': 'Steps forward as you reach center-stage, her cyan-and-navy heterochromia eyes '
                           'shining with overwhelming love.',
             'speaker_line': 'Welcome to our private grand finale, Aether... No scripts, no audience, and no '
                             'masks - just you and me beneath the stars.',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Take both of her hands at center-stage & gaze deeply into her eyes',
                          'player_text': 'You look beyond words tonight, Furina. My heart - and my whole '
                                         'life - is standing right here with you.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Squeezes your hands warmly, her voice trembling with happy '
                                             'emotion.',
                          'reaction_reply': 'Listen to the song I wrote only for you, mon amour...'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hold her hands tenderly under the glowing Hydro canopy',
                          'player_text': 'Every step of my journey led me right to this stage with you, my '
                                         'love.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'And every step of mine led me into your arms, Aether.'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s5_sc4_cg2.jpg',
             'scene_label': '2/4 Developing: Furina Singing Her Unscripted Eternal Love Aria for',
             'scene_progress': 'SCENE 2/4',
             'narration': 'With her hands in yours, Furina sings a crystalline, unscripted love aria echoing '
                          "the melody of 'La Vaguelette' - vowing that while plays have a final curtain, her "
                          'love for her Traveler will never end.',
             'inner_thought': "Salon Solitaire's Whisper: Every single note comes straight from my soul for "
                              'Aether...',
             'action_cue': 'Finishes the soaring final note with a tear of pure happiness sparkling on her '
                           'cheek, pressing your hands to her heart.',
             'speaker_line': '"In a world where every play must end, you became my endless encore." '
                             '...Aether, you saved me from five hundred years of solitude and gave me a '
                             'human heart that beats only for you. Will you stay beside me as my soulmate - '
                             'forever?',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Draw out a sapphire-and-gold promise ring & slip it onto her left ring',
                          'player_text': 'I brought this sapphire-and-starlight ring for you tonight, Furina '
                                         '- because my vow is the same. No matter what world or era comes '
                                         'next, you are my eternal soulmate.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Gasps in pure rapture as the sapphire-and-gold ring sparkles '
                                             'on her finger, slipping a matching band onto yours.',
                          'reaction_reply': 'It fits perfectly! Look - sapphire blue and starlight gold, '
                                            'bound together forever!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Vow your eternal love & place the promise ring on her finger',
                          'player_text': 'From this night until the end of time, Furina, I vow to love, '
                                         'cherish, and stand beside you forever.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Forever and beyond, my beloved Aether!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s5_sc4_cg3.jpg',
             'scene_label': '3/4 Climax: Aether Slipping the Sapphire-and-Gold Promise Ring onto',
             'scene_progress': 'SCENE 3/4',
             'narration': 'As Mademoiselle Crabaletta, Surintendante Chevalmarin, and Gentilhomme Usher send '
                          'a cascade of glowing Hydro blossoms and starlight ribbons around the stage, you '
                          'pull Furina into a breathtaking, eternal-vow kiss.',
             'inner_thought': "Salon Solitaire's Whisper: Bound to Aether by ring, song, and soul... our "
                              'true story is only just beginning!',
             'action_cue': 'Wraps her arms around your neck in a passionate, tearfully joyful kiss at '
                           'center-stage as the starlight canopy blazes overhead.',
             'speaker_line': "No final curtain for us, my darling Aether... Here's to Act Infinity - hand in "
                             "hand, forever and always! Je t'aime!",
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Hold her close in the spotlight & whisper 'Je t'aime' against her lips",
                          'player_text': "Je t'aime, my eternal star, my Furina - now and for all eternity.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Rests her forehead against yours with the brightest, happiest '
                                             'smile in the universe.',
                          'reaction_reply': 'Our eternal standing ovation, mon amour!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Sweep her into a joyous spin under the falling hydro blossoms',
                          'player_text': 'To Act Infinity together, my love!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Best eternal love story ever written, Aether!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]}]

FURINA_10_EXTRA_CAMEO_SCENARIOS: list[dict[str, Any]] = [{'id': 'furina_s1_ex1',
  'char_id': 'furina',
  'stage': 1,
  'order': 5,
  'scenario_num': 5,
  'is_extra_cameo': True,
  'cameo_cast': ['Neuvillette'],
  'cameo_dynamic_tier': 'Stage 1 Friendly Fontaine Reunion (Furina, Aether & Neuvillette)',
  'allow_custom_input': True,
  'title': "Neuvillette's Spring Water & Cafe Pastries",
  'subtitle': 'Stage 1 - Genshin Cameo 1 - Fontaine Cafe Reunion',
  'location': 'Rodeo Boulevard Fountain Terrace Cafe',
  'cg_url': '/dating-media/furina_s1_ex1_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s1_ex1_cg4.jpg',
  'ending_scene_label': '4/4 Cameo: Warm Cafe Toast Between Aether, Blushing Furina &',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s1_ex1_cg1.jpg',
                   'label': '1/4 Opening: Running into Iudex Neuvillette at a Fontaine Cafe Over'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s1_ex1_cg2.jpg',
                   'label': '2/4 Developing: Aether Ordering Romaritime Spring Water & Cake for'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s1_ex1_cg3.jpg',
                   'label': '3/4 Climax: Neuvillette Formally Thanking Aether for Bringing'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s1_ex1_cg4.jpg',
                   'label': '4/4 Cameo: Warm Cafe Toast Between Aether, Blushing Furina &'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Shared afternoon pastries and pure Fontaine spring water with Furina and Chief Justice '
                'Neuvillette, who thanked you for bringing genuine laughter back to Furina.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s1_ex1_cg1.jpg',
             'scene_label': '1/4 Opening: Running into Iudex Neuvillette at a Fontaine Cafe Over',
             'scene_progress': 'SCENE 1/4',
             'narration': 'While you and Furina are enjoying afternoon pastries at an outdoor fountain cafe, '
                          'a tall, silver-haired gentleman in aristocratic blue-and-white attire pauses '
                          'beside your table - Chief Justice Neuvillette himself, holding two crystal '
                          'carafes of spring water.',
             'inner_thought': "Salon Solitaire's Whisper: Oh! It's Neuvillette! What is the Iudex doing at "
                              'our cafe terrace - and why is he carrying two different bottles of spring '
                              'water?!',
             'action_cue': 'Sits up straight with a flustered squeak, brushing a pastry crumb off her lapel '
                           'as Neuvillette bows politely.',
             'speaker_line': "A-Ahem! Good afternoon, Neuvillette! Don't tell me you traveled all this way "
                             'just to lecture me on my pastry budget - Aether and I are conducting a very '
                             'serious culinary review!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Warmly invite Neuvillette to join your table & pour a cup for both of '
                                   'them',
                          'player_text': 'Good to see you, Neuvillette! Pull up a chair and join Furina and '
                                         'me - we were just starting afternoon tea.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Neuvillette smiles faintly as Furina relaxes with a bright '
                                             'grin.',
                          'reaction_reply': '"Thank you, Aether. And fear not, Lady Furina - I merely '
                                            'brought chilled Romaritime spring water to pair with your '
                                            'cakes."'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Greet the Iudex warmly & order an extra plate of Fontaine pastries',
                          'player_text': 'Always an honor, Monsieur Neuvillette! Have a seat with us.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'See, Neuvillette? Aether has impeccable manners!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s1_ex1_cg2.jpg',
             'scene_label': '2/4 Developing: Aether Ordering Romaritime Spring Water & Cake for',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Seated at the sunny marble table, Neuvillette pours crystal-clear Fontaine water '
                          "into three goblets while you slide Furina's favorite raspberry mille-feuille onto "
                          'her plate before she even has to ask.',
             'inner_thought': "Salon Solitaire's Whisper: Aether remembered my exact favorite pastry and "
                              'moved the sugar bowl closer without me saying a word - and Neuvillette is '
                              'watching with a knowing smile!',
             'action_cue': 'Blushes beneath her top hat as Neuvillette observes how attentively you look '
                           'after her.',
             'speaker_line': 'Mmm! This Romaritime spring water actually makes the raspberry cream taste '
                             'twice as crisp! Though I must say, Aether, you memorized my dessert '
                             'preferences even faster than the Palais Mermonia staff!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Smile at Furina & say her happiness is easy to pay attention to',
                          'player_text': 'When someone lights up the whole table the way you do over '
                                         "raspberry mille-feuille, Furina, it's impossible not to remember.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Furina hides her glowing cheeks behind her teacup while '
                                             'Neuvillette nods approvingly.',
                          'reaction_reply': 'A-Aether! Not in front of the Chief Justice!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': "Offer Neuvillette a savory galette while refilling Furina's plate",
                          'player_text': "Glad you like it, Furina - there's plenty more where that came "
                                         'from!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, best cafe companion in two worlds!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s1_ex1_cg3.jpg',
             'scene_label': '3/4 Climax: Neuvillette Formally Thanking Aether for Bringing',
             'scene_progress': 'SCENE 3/4',
             'narration': 'When Furina steps briefly to the counter to choose a box of macarons to take '
                          'home, Neuvillette looks across the table at you with quiet, heartfelt gratitude '
                          'in his amethyst eyes.',
             'inner_thought': "Salon Solitaire's Whisper: (From the counter, Furina glances back wondering "
                              'what the two of you are talking about...)',
             'action_cue': 'Neuvillette places his hand over his chest in a solemn gesture of gratitude '
                           'before Furina returns with her macaron box.',
             'speaker_line': '"Aether... for five centuries, Lady Furina bore an unimaginable burden alone. '
                             'Seeing her laugh so freely and genuinely beside you today brings peace to my '
                             'heart - thank you for cherishing her." Just then, Furina trots back: "Hey! '
                             'What are you two whispering about over your water goblets?!"',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Raise your goblet in a warm toast to Furina's bright future together",
                          'player_text': 'We were just agreeing that seeing you smile like this makes every '
                                         'day sunny, Furina. Cheers to many more cafe afternoons together!',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': "Clinks her goblet happily against yours and Neuvillette's with "
                                             'a radiant blush.',
                          'reaction_reply': "Well! Since you both agree I'm the star of the afternoon, "
                                            'cheers to the three of us!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Smile warmly at Neuvillette & clink glasses when Furina sits down',
                          'player_text': 'Just talking about how lively you make every afternoon, Furina!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "Naturally! Now let's share these macarons!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s1_ex2',
  'char_id': 'furina',
  'stage': 1,
  'order': 6,
  'scenario_num': 6,
  'is_extra_cameo': True,
  'cameo_cast': ['Charlotte'],
  'cameo_dynamic_tier': 'Stage 1 Comedic Paparazzi Cameo (Furina, Aether & Charlotte)',
  'allow_custom_input': True,
  'title': "Dodging Charlotte's Steambird Flash!",
  'subtitle': 'Stage 1 - Genshin Cameo 2 - Paparazzi Hijinks',
  'location': 'Vinewood Theater Boulevard',
  'cg_url': '/dating-media/furina_s1_ex2_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s1_ex2_cg4.jpg',
  'ending_scene_label': '4/4 Cameo: Laughing Over the Hilarious Photobomb Print with',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s1_ex2_cg1.jpg',
                   'label': '1/4 Opening: Steambird Reporter Charlotte Popping Out with Monsieur'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s1_ex2_cg2.jpg',
                   'label': '2/4 Developing: Aether Playfully Shielding Furina as They Duck'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s1_ex2_cg3.jpg',
                   'label': "3/4 Climax: Mademoiselle Crabaletta Photobombing Charlotte's Kamera"},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s1_ex2_cg4.jpg',
                   'label': '4/4 Cameo: Laughing Over the Hilarious Photobomb Print with'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': "Playfully dodged reporter Charlotte's Steambird Kamera flash outside the theater with "
                'Furina as Mademoiselle Crabaletta photobombed the lens.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s1_ex2_cg1.jpg',
             'scene_label': '1/4 Opening: Steambird Reporter Charlotte Popping Out with Monsieur',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Stepping out of the Vinewood Theater side entrance with Furina after a matinee '
                          'screening, a pink-haired reporter in a red newsboy cap suddenly pops out from '
                          'behind a lamppost - Charlotte from The Steambird, aiming her Kamera lens '
                          "'Monsieur Verite' straight at the two of you!",
             'inner_thought': "Salon Solitaire's Whisper: Eek!! It's Charlotte! If she snaps a headline "
                              "photo of Aether and me walking out of the theater together, tomorrow's "
                              'Steambird front page will be explosive!',
             'action_cue': "Gasps and ducks half-behind your shoulder as Charlotte's Kamera flash charges "
                           'up.',
             'speaker_line': '"Aha! Exclusive scoop for The Steambird - Lady Furina and the Honorary Knight '
                             'on a secret theater outing!" - A-Aether, do something before Charlotte prints '
                             'a special edition!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Slip an arm protectively around Furina's shoulders & guide her behind a",
                          'player_text': 'Hold onto my cape, Furina - one smooth sidestep behind this patio '
                                         "screen and we're out of lens range!",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Ducks close against your chest behind the screen, her heart '
                                             'racing with playful excitement.',
                          'reaction_reply': 'Ooh, secret-agent theater escape with Aether! Though standing '
                                            'this close behind the menu board is making my face redder than '
                                            "Charlotte's hat!"},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Step smoothly in front of the lens & greet Charlotte with a friendly '
                                   'wave',
                          'player_text': 'Easy on the flash, Charlotte - Furina and I are just enjoying a '
                                         'quiet afternoon off-stage!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, tell her, Aether - no paparazzi without an appointment!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s1_ex2_cg2.jpg',
             'scene_label': '2/4 Developing: Aether Playfully Shielding Furina as They Duck',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Charlotte trots around the patio screen with her notebook out, her green eyes '
                          "sparkling with journalistic curiosity as she sees you still holding Furina's "
                          'hand.',
             'inner_thought': "Salon Solitaire's Whisper: Charlotte is staring right at our hands - and "
                              "honestly, I don't even want to let go!",
             'action_cue': 'Adjusts her top hat with a theatrical cough while keeping her fingers lightly '
                           'hooked with yours.',
             'speaker_line': '"Come on, Lady Furina, Traveler! My readers have been dying to know about your '
                             'creative partnership since the Fontinalia Film Festival! Just one official '
                             'quote and one photo together?"',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Give Charlotte a charming quote praising Furina as the greatest star &',
                          'player_text': 'You can quote me on this, Charlotte: working - and spending my '
                                         'afternoons - with Furina is the highlight of every single week.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Furina beams with a proud, rosy blush while Charlotte '
                                             'scribbles furiously.',
                          'reaction_reply': 'Did you get that down verbatim, Charlotte?! Underline '
                                            "'highlight of every single week' twice!"},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Smile & agree to one friendly photo on the condition of no gossip',
                          'player_text': "One friendly photo is fine, Charlotte, as long as it's an arts "
                                         'feature and not a rumor column!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'A fair press agreement! Pose beside me, Aether!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s1_ex2_cg3.jpg',
             'scene_label': "3/4 Climax: Mademoiselle Crabaletta Photobombing Charlotte's Kamera",
             'scene_progress': 'SCENE 3/4',
             'narration': 'Just as you and Furina strike a pose side-by-side and Charlotte clicks the '
                          'shutter - FLASH! - Mademoiselle Crabaletta floats squarely in front of the lens '
                          'flashing a giant crab-claw peace sign!',
             'inner_thought': "Salon Solitaire's Whisper: Pfft - hahaha!! Mademoiselle Crabaletta stole the "
                              "entire center of Charlotte's scoop photo!",
             'action_cue': 'Bursts into melodious laughter leaning against your shoulder as Charlotte stares '
                           "at the printed photo of Crabaletta's giant claw.",
             'speaker_line': 'Hahaha! Bravo, Mademoiselle Crabaletta! Look at the print, Aether - you can '
                             "only see Crabaletta's claw and the two of us smiling in the corner!",
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Ask Charlotte for a copy of the photobomb print to keep as a souvenir '
                                   'with',
                          'player_text': "Let's keep that photobomb print for our album, Furina - it's "
                                         'one-of-a-kind, just like our afternoon.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Tucks the photo into her script book with a fond smile.',
                          'reaction_reply': 'Best souvenir ever! Thanks for the photo, Charlotte!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Laugh together with Furina & Charlotte over the hilarious print',
                          'player_text': 'Crabaletta definitely wins the Steambird front page today!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Ten out of ten camera blocking from Salon Solitaire!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s2_ex1',
  'char_id': 'furina',
  'stage': 2,
  'order': 5,
  'scenario_num': 5,
  'is_extra_cameo': True,
  'cameo_cast': ['Navia', 'Clorinde'],
  'cameo_dynamic_tier': 'Stage 2 Warm Wingman Teasing (Furina, Aether, Navia & Clorinde)',
  'allow_custom_input': True,
  'title': 'Afternoon Tea & Macarons with Navia & Clorinde',
  'subtitle': 'Stage 2 - Genshin Cameo 1 - Spina di Rosula Tea Party',
  'location': 'Richman Garden Pavilion',
  'cg_url': '/dating-media/furina_s2_ex1_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s2_ex1_cg4.jpg',
  'ending_scene_label': '4/4 Cameo: Cheerful Fontaine Tea Party Group Photo with Navia,',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s2_ex1_cg1.jpg',
                   'label': '1/4 Opening: Afternoon Tea & Macarons on the Promenade with Navia &'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s2_ex1_cg2.jpg',
                   'label': '2/4 Developing: Navia Teasing Furina for Saving the Crown Strawberry'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s2_ex1_cg3.jpg',
                   'label': '3/4 Climax: Clorinde Calmly Pouring Tea While Blushing Furina Feeds'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s2_ex1_cg4.jpg',
                   'label': '4/4 Cameo: Cheerful Fontaine Tea Party Group Photo with Navia,'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Attended an afternoon tea party with Furina, Navia, and Clorinde where Navia teased Furina '
                'for saving her crown strawberry macaron strictly for you.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s2_ex1_cg1.jpg',
             'scene_label': '1/4 Opening: Afternoon Tea & Macarons on the Promenade with Navia &',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Beneath the white roses of the Richman Garden Pavilion, Navia and Clorinde have '
                          'set up an elaborate Fontaine afternoon tea table complete with a three-tier '
                          'silver stand of freshly baked macarons. As you arrive with Furina, Navia waves '
                          'enthusiastically in her golden sunglasses.',
             'inner_thought': "Salon Solitaire's Whisper: Navia baked her famous macarons and Clorinde "
                              'brought Marcotte herbal tea - and we walked in right together!',
             'action_cue': 'Waves back happily as you pull out her garden chair for her beside Navia and '
                           'Clorinde.',
             'speaker_line': '"Welcome, Furina, and welcome, my dear partner Aether!" Navia beams, resting '
                             'her chin on her hands. "Look at the two of you arriving together - and Aether '
                             'pulling out her chair like a true Fontaine gentleman!"',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Greet Navia & Clorinde warmly while pouring Furina's first cup of tea",
                          'player_text': 'Great to see you both, Navia and Clorinde! Your macarons smelled '
                                         'amazing from all the way down the garden path.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Clorinde nods with a calm smile while Furina beams proudly.',
                          'reaction_reply': "Hehe, Aether always spoils me with the first cup of tea - don't "
                                            'be jealous, Navia!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': "Compliment Navia's macaron display & sit right beside Furina",
                          'player_text': 'Those macarons are works of art, Navia! Thanks for inviting Furina '
                                         'and me.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': '"Anything for our favorite duo!" Navia laughs.'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s2_ex1_cg2.jpg',
             'scene_label': '2/4 Developing: Navia Teasing Furina for Saving the Crown Strawberry',
             'scene_progress': 'SCENE 2/4',
             'narration': 'As everyone reaches for the silver dessert stand, Navia notices Furina guarding '
                          'the single heart-stamped strawberry macaron on the top tier - and playfully '
                          "nudges Clorinde's elbow.",
             'inner_thought': "Salon Solitaire's Whisper: I kept that top heart-shaped strawberry macaron "
                              'safe for ten minutes so I could give it to Aether!',
             'action_cue': 'Places her gloved hand protectively beside the top plate as Navia grins '
                           'mischievously.',
             'speaker_line': '"Oho?" Navia teases with a wink. "Furina usually eats the crown strawberry '
                             "macaron within thirty seconds, Clorinde - yet she hasn't touched it! Who could "
                             'she possibly be saving the heart-shaped macaron for?"',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Smile affectionately at blushing Furina & ask if she saved it for you',
                          'player_text': 'Did you really save your favorite strawberry macaron on the top '
                                         'tier just for me, Furina?',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Blushes from ear to ear as Navia giggles and Clorinde hides a '
                                             'smile behind her teacup.',
                          'reaction_reply': "W-Well, of course I did! You're my special guest today, Aether, "
                                            'so the best macaron naturally belongs to you!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Thank Furina warmly & suggest splitting the crown macaron together',
                          'player_text': "That's really sweet of you, Furina - let's share the crown macaron "
                                         'together!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "A-Ahem! Only because it's you, Aether!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s2_ex1_cg3.jpg',
             'scene_label': '3/4 Climax: Clorinde Calmly Pouring Tea While Blushing Furina Feeds',
             'scene_progress': 'SCENE 3/4',
             'narration': 'While Clorinde calmly refills the teacups, Furina picks up the heart-stamped '
                          'strawberry macaron and feeds it directly to your lips in front of her two closest '
                          'Fontaine friends.',
             'inner_thought': "Salon Solitaire's Whisper: Feeding Aether in front of Navia and Clorinde is "
                              'so embarrassing - and yet my heart is so happy!',
             'action_cue': 'Holds the pink heart macaron to your lips with a shy, glowing smile as Navia '
                           'claps delightedly.',
             'speaker_line': "Here, Aether - eat it before Navia teases me any further! ...Well? Isn't the "
                             'strawberry filling the sweetest?',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Savor the macaron from her fingers & gently kiss the sugar crumb from '
                                   'her',
                          'player_text': 'Sweetest macaron at the table - mostly because you saved it and '
                                         'fed it to me yourself, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Turns bright scarlet as Navia cheers and Clorinde offers a '
                                             "quiet 'Well played, Aether'.",
                          'reaction_reply': 'E-Eep!! Kissing my thumb at the tea table?! You really have no '
                                            'mercy on my heart!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Enjoy the sweet bite & raise your teacup in a toast with all four '
                                   'friends',
                          'player_text': "Delicious! Here's to afternoon tea with the best friends from "
                                         'Fontaine!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Cheers to our Fontaine tea party!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s2_ex2',
  'char_id': 'furina',
  'stage': 2,
  'order': 6,
  'scenario_num': 6,
  'is_extra_cameo': True,
  'cameo_cast': ['Chiori'],
  'cameo_dynamic_tier': 'Stage 2 Matching Outfit Wingman Cameo (Furina, Aether & Chiori)',
  'allow_custom_input': True,
  'title': "Chiori's Starlight & Sapphire Wardrobe Fitting",
  'subtitle': 'Stage 2 - Genshin Cameo 2 - Chioriya Boutique',
  'location': 'Chioriya Boutique Rodeo Branch',
  'cg_url': '/dating-media/furina_s2_ex2_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s2_ex2_cg4.jpg',
  'ending_scene_label': '4/4 Cameo: Walking Out of Chioriya Boutique in Matching',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s2_ex2_cg1.jpg',
                   'label': '1/4 Opening: Visiting Chioriya Boutique with Aether for Custom Stage'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s2_ex2_cg2.jpg',
                   'label': '2/4 Developing: Chiori Holding Up Gold-and-Starlight Silk Accents'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s2_ex2_cg3.jpg',
                   'label': "3/4 Climax: Aether Fastening the Gold Starlight Brooch on Furina's"},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s2_ex2_cg4.jpg',
                   'label': '4/4 Cameo: Walking Out of Chioriya Boutique in Matching'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Accompanied Furina to Chioriya Boutique where Chiori teased her for secretly requesting '
                'gold-and-starlight accents matching your Traveler attire.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s2_ex2_cg1.jpg',
             'scene_label': '1/4 Opening: Visiting Chioriya Boutique with Aether for Custom Stage',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Inside the elegant Rodeo Drive branch of Chioriya Boutique, silk bolts and '
                          'mannequins glimmer under crystal chandeliers. Designer Chiori stands beside a '
                          'three-way mirror with a measuring tape over her shoulder as Furina steps out of '
                          'the fitting room in a new sapphire stage coat.',
             'inner_thought': "Salon Solitaire's Whisper: I asked Chiori to weave golden starlight "
                              "embroidery into my sapphire lapels so my outfit matches Aether's...",
             'action_cue': 'Twirls in front of the mirror as Chiori crosses her arms with a sharp, knowing '
                           'smirk.',
             'speaker_line': '"The sapphire silk fits like a glove, Furina," Chiori remarks dryly, glancing '
                             'toward you on the velvet sofa. "Though since you insisted on \'Traveler-gold '
                             "starlight trim and a matching golden cravat pin,' why don't we ask the "
                             'inspiration himself what he thinks?"',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Stand up to admire her up close & praise how the gold and sapphire',
                          'player_text': 'The sapphire silk with golden starlight trim looks incredible on '
                                         "you, Furina - I'm honored to match colors with my favorite star.",
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Blushes brightly in the three-way mirror while Tamoto floats '
                                             'by snipping a loose thread.',
                          'reaction_reply': "C-Chiori, you didn't have to reveal my design brief out loud! "
                                            '...Though hearing Aether loves our matching colors makes me '
                                            'very happy!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': "Compliment both Chiori's craftsmanship and Furina's elegance",
                          'player_text': 'Masterpiece tailoring, Chiori - and Furina makes it shine like a '
                                         'true premiere!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, you have an eye for high fashion, Aether!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s2_ex2_cg2.jpg',
             'scene_label': '2/4 Developing: Chiori Holding Up Gold-and-Starlight Silk Accents',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Chiori hands you a velvet tray holding a handcrafted golden star-flower brooch '
                          "and gestures toward Furina's ribboned collar.",
             'inner_thought': "Salon Solitaire's Whisper: Chiori is telling Aether to pin the brooch on my "
                              'collar himself...!',
             'action_cue': 'Lifts her chin slightly in front of the mirror, her pulse fluttering visibly at '
                           'her throat as you step right in front of her.',
             'speaker_line': '"Go ahead, Aether," Chiori says, adjusting a sleeve on a nearby mannequin. "A '
                             "matching couple's accessory should be fastened by the partner who inspired "
                             'it."',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Step close in front of the mirror & gently fasten the golden star brooch',
                          'player_text': 'Hold still for a moment, Furina - there, pinned right over your '
                                         'collar so a piece of my starlight is always with you.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Touches the golden star brooch on her collar with a tender, '
                                             'lovestruck blush.',
                          'reaction_reply': 'It feels so warm right here near my heart, Aether...'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Fasten the brooch carefully & adjust her sapphire lapel with a warm '
                                   'smile',
                          'player_text': 'Perfect fit! Now our outfits are officially a matched set, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Officially a matched duo on and off the stage!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s2_ex2_cg3.jpg',
             'scene_label': "3/4 Climax: Aether Fastening the Gold Starlight Brooch on Furina's",
             'scene_progress': 'SCENE 3/4',
             'narration': 'Before you leave the boutique, Chiori tosses you a matching sapphire-blue silk '
                          "pocket ribbon woven from the exact same bolt as Furina's coat.",
             'inner_thought': "Salon Solitaire's Whisper: Now Aether is wearing my sapphire blue and I'm "
                              'wearing his starlight gold!',
             'action_cue': 'Ties the sapphire silk ribbon neatly onto your outfit herself, smoothing your '
                           'chest with both hands.',
             'speaker_line': "There! Now you're wearing my sapphire ribbon and I'm wearing your golden star "
                             'brooch! Thank you for the custom pieces, Chiori!',
             'mood': 'Playful',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Thank Chiori & escort Furina out of the boutique arm-in-arm',
                          'player_text': "Thanks for the craftsmanship, Chiori! Come on, Furina - let's show "
                                         'off our matching colors down the boulevard.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Hooks her arm happily through yours as Chiori waves from the '
                                             'boutique doorway.',
                          'reaction_reply': 'Best wardrobe fitting ever, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Pose together in the boutique mirror & wave goodbye to Chiori',
                          'player_text': 'Look at us in the mirror, Furina - we look ready for any gala!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Ten out of ten style harmony!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s3_ex1',
  'char_id': 'furina',
  'stage': 3,
  'order': 5,
  'scenario_num': 5,
  'is_extra_cameo': True,
  'cameo_cast': ['Lyney', 'Lynette', 'Freminet'],
  'cameo_dynamic_tier': 'Stage 3 Romantic Wingman Illusion (Furina, Aether, Lyney, Lynette & Freminet)',
  'allow_custom_input': True,
  'title': "Lyney & Lynette's Romaritime Magic Trick",
  'subtitle': 'Stage 3 - Genshin Cameo 1 - House of the Hearth Magic',
  'location': 'Grand Opera Epiclese Stage',
  'cg_url': '/dating-media/furina_s3_ex1_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s3_ex1_cg4.jpg',
  'ending_scene_label': "4/4 Cameo: Aether Pinning the Romaritime Flower in Furina's Hair as",
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s3_ex1_cg1.jpg',
                   'label': '1/4 Opening: Attending a Magic Show Rehearsal at Opera Epiclese with'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s3_ex1_cg2.jpg',
                   'label': '2/4 Developing: Lyney & Lynette Inviting Aether & Furina to the'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s3_ex1_cg3.jpg',
                   'label': '3/4 Climax: Lyney Producing a Glowing Blue Romaritime Flower Right'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s3_ex1_cg4.jpg',
                   'label': "4/4 Cameo: Aether Pinning the Romaritime Flower in Furina's Hair as"}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': "Visited Lyney, Lynette, and Freminet's magic rehearsal with Furina, where Lyney conjured a "
                'glowing Romaritime Flower between you and a blushing Furina.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s3_ex1_cg1.jpg',
             'scene_label': '1/4 Opening: Attending a Magic Show Rehearsal at Opera Epiclese with',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Inside the grand theater hall during an afternoon magic rehearsal, master '
                          'magician Lyney tips his top hat while Lynette and Freminet adjust a shimmering '
                          'water-tank prop. Spotting you and Furina walking down the aisle together, Lyney '
                          'grins and leaps down to the stage edge.',
             'inner_thought': "Salon Solitaire's Whisper: Lyney, Lynette, and Freminet are rehearsing a "
                              'brand-new illusion - and Lyney is looking at Aether and me with that '
                              "mischievous magician's grin!",
             'action_cue': 'Waves warmly to the three siblings as Freminet hugs Pers shyly and Lynette '
                           "offers a deadpan 'Ta-da'.",
             'speaker_line': '"Lady Furina! Aether!" Lyney bows with a flourish of playing cards. "What '
                             'impeccable timing! We need two volunteers whose hearts are already in sync to '
                             'test our finale illusion!"',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Take Furina's hand & step up onto the stage together as volunteers",
                          'player_text': 'Hearts in sync? Sounds like the cue was written specifically for '
                                         'Furina and me. Lead the way, Lyney!',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Furina blushes rosily as you lace your fingers with hers '
                                             'walking up the stage steps.',
                          'reaction_reply': 'A-Aether! Admitting our hearts are in sync right in front of '
                                            'the magic trio?!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Smile & escort Furina up the steps to help test the magic trick',
                          'player_text': "We'd love to see the new illusion up close - ready when you are, "
                                         'Lyney and Lynette!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "Let's see if your sleight of hand can impress a veteran "
                                            'director!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s3_ex1_cg2.jpg',
             'scene_label': '2/4 Developing: Lyney & Lynette Inviting Aether & Furina to the',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Standing face-to-face at center-stage while Lynette rings a silver chime and '
                          'Freminet releases a gentle mist of frost-and-water sparkles, Lyney asks you and '
                          'Furina to hold both hands together and close your eyes for three counts.',
             'inner_thought': "Salon Solitaire's Whisper: Holding both of Aether's hands with my eyes closed "
                              'while sparkles drift around us... I can hear my own heartbeat!',
             'action_cue': 'Stands close in front of you holding both your hands, her eyelashes fluttering '
                           'open on the count of three.',
             'speaker_line': '"One... two... three - open your eyes!" With a snap of Lyney\'s fingers, a '
                             'luminous, dew-kissed blue Romaritime Flower materializes floating right in the '
                             "narrow space between your lips and Furina's!",
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Catch the glowing Romaritime Flower & gently tuck it behind Furina's ear",
                          'player_text': 'A flower that only blooms for true devotion - it belongs right '
                                         'here in your hair, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Touches the glowing blue petals in her hair with a '
                                             'breathtaking crimson blush while Freminet claps and Lynette '
                                             "gives a thumbs-up: 'Romance level: maximum'.",
                          'reaction_reply': "Aether... you're an even bigger heart-stealer than the "
                                            'magician!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Admire the magic trick & present the flower to Furina with a bow',
                          'player_text': 'Incredible sleight of hand, Lyney! For you, my lady.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "Hehe, I'll treasure this Romaritime Flower forever!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s3_ex1_cg3.jpg',
             'scene_label': '3/4 Climax: Lyney Producing a Glowing Blue Romaritime Flower Right',
             'scene_progress': 'SCENE 3/4',
             'narration': 'As Lyney tips his hat and jokes that no magic trick could ever outshine the real '
                          'spark between the two of you, Furina links her arm tightly through yours.',
             'inner_thought': "Salon Solitaire's Whisper: Even Lyney, Lynette, and Freminet can tell how "
                              'head-over-heels we are for each other!',
             'action_cue': 'Wears the glowing Romaritime Flower proudly in her hair and leans her cheek '
                           'against your shoulder.',
             'speaker_line': '"The magic never lies," Lyney winks as Lynette nods in agreement. Well, Aether '
                             "- since everyone backstage already knows how special you are to me, let's "
                             'treat the trio to cake after rehearsal!',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Kiss Furina's flower-adorned hair lightly & invite the trio for pastries",
                          'player_text': 'Cake for the whole cast is on me - especially after giving my girl '
                                         'such a beautiful flower.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Beams with pure lovestruck joy as the siblings cheer.',
                          'reaction_reply': 'Best rehearsal cameo ever, mon amour!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Thank Lyney, Lynette & Freminet and head out for celebration sweets',
                          'player_text': "Bravo to the House of the Hearth magic troupe! Let's go celebrate!",
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'To the patisserie, everyone!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s3_ex2',
  'char_id': 'furina',
  'stage': 3,
  'order': 6,
  'scenario_num': 6,
  'is_extra_cameo': True,
  'cameo_cast': ['Hu Tao'],
  'cameo_dynamic_tier': 'Stage 3 Cross-Region Teasing Cameo (Furina, Aether & Hu Tao)',
  'allow_custom_input': True,
  'title': "Hu Tao's Spooky-Comedic Cross-Region Play Pitch!",
  'subtitle': 'Stage 3 - Genshin Cameo 2 - Liyue-Fontaine Directors',
  'location': 'Vinewood Courtyard Tea Lounge',
  'cg_url': '/dating-media/furina_s3_ex2_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s3_ex2_cg4.jpg',
  'ending_scene_label': "4/4 Cameo: Cross-Region Directors' Tea Toast with Hu Tao, Furina &",
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s3_ex2_cg1.jpg',
                   'label': '1/4 Opening: Director Hu Tao Visiting from Liyue to Pitch a'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s3_ex2_cg2.jpg',
                   'label': '2/4 Developing: Boo Tao & Crabaletta Floating Nose-to-Nose as Furina'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s3_ex2_cg3.jpg',
                   'label': "3/4 Climax: Hu Tao Teasing How Tightly Furina Holds Aether's Arm in"},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s3_ex2_cg4.jpg',
                   'label': "4/4 Cameo: Cross-Region Directors' Tea Toast with Hu Tao, Furina &"}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Met Director Hu Tao with Furina for a spooky-comedic Liyue-Fontaine stage play pitch, '
                'holding Furina close when Boo Tao popped out to tease her.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s3_ex2_cg1.jpg',
             'scene_label': '1/4 Opening: Director Hu Tao Visiting from Liyue to Pitch a',
             'scene_progress': 'SCENE 1/4',
             'narration': 'At a lantern-lit courtyard tea lounge, Director Hu Tao of the Wangsheng Funeral '
                          'Parlor waves her arms with theatrical gusto across the table, pitching a '
                          'cross-region Liyue-Fontaine musical comedy to you and Furina.',
             'inner_thought': "Salon Solitaire's Whisper: Director Hu Tao is so full of chaotic poetic "
                              "energy - just please don't let her summon any actual ghosts while I'm "
                              'drinking my tea!',
             'action_cue': 'Sits extra close to your side on the wooden bench as Hu Tao leans forward with '
                           'sparkling plum-blossom eyes.',
             'speaker_line': '"Picture this, Director Furina and Aether!" Hu Tao grins, steepling her '
                             'fingers. "Act One opens in a foggy midnight opera house where a mischievous '
                             'spirit serenades two star-crossed lovers - and Boom! Boo Tao makes his grand '
                             'entrance!"',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Wrap a reassuring arm around Furina's waist as Boo Tao floats out with a",
                          'player_text': "Easy there, Furina - I've got you right here in my arms, and Boo "
                                         'Tao is completely friendly!',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Yelps adorably and buries her face against your chest before '
                                             'peeking out at Boo Tao floating nose-to-nose with Crabaletta.',
                          'reaction_reply': "E-Eep!! Don't pop out of thin air like that! ...Though being "
                                            'held this tightly by Aether is a very effective ghost shield!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Laugh warmly as Crabaletta & Boo Tao spin around each other in midair',
                          'player_text': 'Look, Furina - Crabaletta and Boo Tao are already rehearsing their '
                                         'duet together!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "O-Oh! Well, as long as Crabaletta approves, I suppose I'm not "
                                            'scared at all!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s3_ex2_cg2.jpg',
             'scene_label': '2/4 Developing: Boo Tao & Crabaletta Floating Nose-to-Nose as Furina',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Resting her chin in her palms with a sly, knowing grin, Hu Tao eyes the way '
                          'Furina is still clinging to your arm with both hands.',
             'inner_thought': "Salon Solitaire's Whisper: W-Wait - why is Director Hu Tao looking at my "
                              "hands wrapped around Aether's arm with that teasing smirk?!",
             'action_cue': 'Blushes furiously and tries to look dignified while refusing to let go of your '
                           'bicep.',
             'speaker_line': '"Aiya, aiya!" Hu Tao singsongs playfully. "Look how tightly Director Furina is '
                             "clinging to Aether's arm! Are we sure this script is a spooky comedy and not a "
                             'passionately clingy romance documentary?"',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Hold Furina's hand warmly & tell Hu Tao that romance is always the best",
                          'player_text': 'Every script Furina and I work on naturally turns into a romance, '
                                         'Hu Tao - because I love having her hold onto my arm.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': "Furina's heart melts completely as she leans her rosy cheek "
                                             'against your shoulder.',
                          'reaction_reply': 'Hehe, did you hear that, Director Hu Tao? My leading man '
                                            'officially enjoys my clinging!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Chuckle & tell Hu Tao that Furina is just testing the stage blocking',
                          'player_text': "We're just demonstrating top-tier co-star chemistry for the play, "
                                         'right, Furina?',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'E-Exactly! Purely 100% authentic romantic method acting!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s3_ex2_cg3.jpg',
             'scene_label': "3/4 Climax: Hu Tao Teasing How Tightly Furina Holds Aether's Arm in",
             'scene_progress': 'SCENE 3/4',
             'narration': 'After co-writing a hilarious and heartwarming outline for the Liyue-Fontaine '
                          'stage showcase, the three of you clink teacups while Boo Tao and Mademoiselle '
                          'Crabaletta high-five in midair.',
             'inner_thought': "Salon Solitaire's Whisper: Collaborating with Hu Tao while Aether holds my "
                              'hand under the table made this evening unforgettable!',
             'action_cue': "Clinks her porcelain cup against yours and Hu Tao's while keeping her other hand "
                           'intertwined with yours under the table.',
             'speaker_line': 'To the Liyue-Fontaine Theater Alliance! And thank you for keeping me safe from '
                             'spooky surprises all evening, Aether!',
             'mood': 'Affectionate',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Squeeze her hand under the table & walk her home under the lanterns',
                          'player_text': "Anytime, my fearless Director - I'll always be your personal "
                                         'ghost-shield and leading man.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Giggles happily, leaning into your side as Hu Tao waves '
                                             'goodbye.',
                          'reaction_reply': 'My favorite leading man in all Seven Nations!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Toast to a smash-hit script with Furina & Hu Tao',
                          'player_text': 'Cheers to our two brilliant directors!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Bravo, Encore!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s4_ex1',
  'char_id': 'furina',
  'stage': 4,
  'order': 5,
  'scenario_num': 5,
  'is_extra_cameo': True,
  'cameo_cast': ['Navia', 'Charlotte'],
  'cameo_dynamic_tier': "Stage 4 Lovers' Date Wingman Shield (Furina, Aether, Navia & Charlotte)",
  'allow_custom_input': True,
  'title': "Caught Holding Hands Outside Patisserie 'Pour la Justi",
  'subtitle': "Stage 4 - Genshin Cameo 1 - Navia's Umbrella Shield",
  'location': 'Rodeo Boulevard Twilight Promenade',
  'cg_url': '/dating-media/furina_s4_ex1_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s4_ex1_cg4.jpg',
  'ending_scene_label': '4/4 Cameo: Escaping Hand-in-Hand Down the Harbor Steps Laughing as',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s4_ex1_cg1.jpg',
                   'label': "1/4 Opening: Walking Hand-in-Hand Outside Patisserie 'Pour la"},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s4_ex1_cg2.jpg',
                   'label': '2/4 Developing: Caught on a Date! Charlotte Gasps with Her Kamera as'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s4_ex1_cg3.jpg',
                   'label': '3/4 Climax: Navia Playfully Opening Her Golden Umbrella to Block'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s4_ex1_cg4.jpg',
                   'label': '4/4 Cameo: Escaping Hand-in-Hand Down the Harbor Steps Laughing as'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Were spotted walking hand-in-hand on a twilight date by Charlotte and Navia; Navia '
                'playfully opened her golden umbrella to shield your private kiss.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s4_ex1_cg1.jpg',
             'scene_label': "1/4 Opening: Walking Hand-in-Hand Outside Patisserie 'Pour la",
             'scene_progress': 'SCENE 1/4',
             'narration': 'Strolling down the rose-lit cobblestone promenade outside Patisserie Pour la '
                          'Justice at twilight, you and Furina walk with your fingers openly intertwined, '
                          'Furina leaning happily against your shoulder.',
             'inner_thought': "Salon Solitaire's Whisper: Walking hand-in-hand with Aether at twilight as "
                              "his devoted girlfriend... I don't even care who sees us anymore!",
             'action_cue': 'Swings your joined hands gently between you with a lovestruck smile - until two '
                           'familiar voices call out from the patisserie terrace.',
             'speaker_line': '"Hold the front press!!" Charlotte gasps, lifting her Kamera, while Navia '
                             'beams beside her holding a pastry box. "Is that Lady Furina and Aether walking '
                             'with interlocked fingers on a twilight lovers\' date?!"',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Keep holding Furina's hand proudly & smile warmly at Navia and Charlotte",
                          'player_text': 'No need for investigative theories, Charlotte and Navia - Furina '
                                         "and I are out on a date tonight, and I couldn't be prouder to hold "
                                         'her hand.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': "Furina's eyes shine with pure adoration as she squeezes your "
                                             'hand tighter.',
                          'reaction_reply': 'Aether...! Hearing you announce our date so proudly makes my '
                                            'heart soar!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Pull Furina close to your side with an affectionate grin',
                          'player_text': 'Caught red-handed on our evening date! Good evening, Navia, '
                                         'Charlotte!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "Hehe, yes - he's officially mine!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s4_ex1_cg2.jpg',
             'scene_label': '2/4 Developing: Caught on a Date! Charlotte Gasps with Her Kamera as',
             'scene_progress': 'SCENE 2/4',
             'narration': "As Charlotte's journalist instincts kick into overdrive and she raises her Kamera "
                          "lens for a close-up of Furina's blushing face, Navia steps smoothly forward with "
                          'a mischievous wink and twirls her golden Spina di Rosula umbrella open!',
             'inner_thought': "Salon Solitaire's Whisper: Navia just opened her golden umbrella right in "
                              "front of Charlotte's Kamera to give Aether and me privacy!",
             'action_cue': "Blushes behind the golden canopy of Navia's umbrella as Navia winks back over "
                           'her shoulder at the two of you.',
             'speaker_line': '"Oops! Look how bright the twilight glare is, Charlotte - my umbrella slipped '
                             'open!" Navia whispers back to you and Furina with a grin: "You two lovebirds '
                             'have ten seconds of full umbrella cover before I move - make it count!"',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Pull Furina into your arms behind Navia's golden umbrella & kiss her "
                                   'lips',
                          'player_text': 'Thank you, Boss Navia! Come here behind the umbrella, my love.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Melts into a thrilling, secret kiss behind the golden umbrella '
                                             'canopy, her arms looped tightly around your neck.',
                          'reaction_reply': "Mmm... stealing a kiss behind Navia's umbrella right in the "
                                            'middle of the boulevard is so romantic!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Give Furina a sweet forehead kiss behind the umbrella shield & thank '
                                   'Navia',
                          'player_text': 'Best wingwoman in Fontaine, Navia!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, ten out of ten umbrella choreography!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s4_ex1_cg3.jpg',
             'scene_label': '3/4 Climax: Navia Playfully Opening Her Golden Umbrella to Block',
             'scene_progress': 'SCENE 3/4',
             'narration': 'When Navia folds her umbrella back up and hands you a box of complimentary '
                          'celebration macarons while keeping Charlotte busy with an exclusive Spina di '
                          'Rosula interview, you and Furina slip away hand-in-hand down the harbor steps.',
             'inner_thought': "Salon Solitaire's Whisper: Escaping hand-in-hand into the twilight with a box "
                              "of macarons and my lips still tingling from Aether's kiss...",
             'action_cue': 'Runs lightly down the harbor steps holding your hand, looking back at you with '
                           'radiant, laughing eyes.',
             'speaker_line': 'Remind me to send Navia the biggest bouquet of roses tomorrow, Aether! Now '
                             'come on - the rest of tonight belongs to just the two of us!',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Lace your fingers tightly with hers & lead her toward the moonlit bay',
                          'player_text': 'All ours, my love - with zero cameras and endless starlight ahead.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Kisses your cheek happily as you walk along the bay.',
                          'reaction_reply': 'Best twilight date ever, mon amour!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Carry the macaron box & hold her close down the promenade',
                          'player_text': "Navia really is the ultimate friend! Let's enjoy our macarons by "
                                         'the water, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Lead the way, my darling!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s4_ex2',
  'char_id': 'furina',
  'stage': 4,
  'order': 6,
  'scenario_num': 6,
  'is_extra_cameo': True,
  'cameo_cast': ['Neuvillette'],
  'cameo_dynamic_tier': 'Stage 4 Heartwarming Guardian Cameo (Furina, Aether & Neuvillette)',
  'allow_custom_input': True,
  'title': 'Neuvillette Clears the Rain for Our Anniversary Walk',
  'subtitle': "Stage 4 - Genshin Cameo 2 - Hydro Dragon's Sunshine",
  'location': 'Bayside Ocean Overlook Promenade',
  'cg_url': '/dating-media/furina_s4_ex2_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s4_ex2_cg4.jpg',
  'ending_scene_label': '4/4 Cameo: Walking Beneath a Double Rainbow Over the Bay as',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s4_ex2_cg1.jpg',
                   'label': '1/4 Opening: A Sudden Evening Drizzle Over the Promenade as'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s4_ex2_cg2.jpg',
                   'label': "2/4 Developing: Furina Under Aether's Umbrella Teasing Neuvillette"},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s4_ex2_cg3.jpg',
                   'label': '3/4 Climax: Neuvillette Smiling Gently as Golden Sunset Parting the'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s4_ex2_cg4.jpg',
                   'label': '4/4 Cameo: Walking Beneath a Double Rainbow Over the Bay as'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Shared an umbrella with Furina during a sudden drizzle on your anniversary walk until '
                'Neuvillette fondly parted the rainclouds into a golden double rainbow.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s4_ex2_cg1.jpg',
             'scene_label': '1/4 Opening: A Sudden Evening Drizzle Over the Promenade as',
             'scene_progress': 'SCENE 1/4',
             'narration': 'During a romantic anniversary stroll along the Bayside Ocean Overlook, a sudden '
                          'gentle sun-shower begins to fall. Opening your umbrella over Furina and pulling '
                          'her close against your side, you both spot Neuvillette standing contemplatively '
                          'by the marble balustrade ahead, gazing out at the sea.',
             'inner_thought': "Salon Solitaire's Whisper: Wait a minute - the forecast said clear skies all "
                              "evening! If it's suddenly drizzling right here, that means the Hydro Dragon "
                              'is feeling nostalgic!',
             'action_cue': 'Steps close under your umbrella with her arm around your waist, calling out '
                           'playfully toward Neuvillette.',
             'speaker_line': "Aha! I knew this rain wasn't on the meteorological schedule! Neuvillette, "
                             "don't tell me you're getting sentimental over the ocean right in the middle of "
                             "Aether's and my romantic anniversary walk!",
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Keep Furina warm under your arm & greet Neuvillette with a gentle smile',
                          'player_text': 'Good evening, Neuvillette! Sharing one small umbrella with Furina '
                                         'is pretty cozy, though we hope everything is well with you.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Neuvillette turns with a mild, apologetic expression as the '
                                             'rain immediately softens.',
                          'reaction_reply': '"Forgive me, Aether, Lady Furina. I was merely reflecting on '
                                            'how quickly time passes - I did not mean to dampen your '
                                            'celebration."'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Smile warmly at Neuvillette from beneath the shared umbrella',
                          'player_text': "Don't worry, Neuvillette - even a little rain feels romantic when "
                                         'Furina and I share an umbrella!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Hehe, though golden sunshine for our anniversary photos '
                                            "wouldn't hurt either!"},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s4_ex2_cg2.jpg',
             'scene_label': "2/4 Developing: Furina Under Aether's Umbrella Teasing Neuvillette",
             'scene_progress': 'SCENE 2/4',
             'narration': 'Looking at how closely Furina is nestled against your chest with her hand resting '
                          "over your heart, Neuvillette's serious expression softens into a rare, deeply "
                          'fond smile.',
             'inner_thought': "Salon Solitaire's Whisper: Neuvillette is looking at the two of us like a "
                              'proud guardian watching his dearest family...',
             'action_cue': 'Leans her head affectionately against your shoulder as Neuvillette gazes up '
                           'toward the silver clouds.',
             'speaker_line': '"Seeing the two of you so devoted to one another is enough to brighten any '
                             'sky," Neuvillette murmurs gently. As he lifts his cane slightly, the silver '
                             'rainclouds part above the bay, pouring warm golden sunset light and a '
                             'shimmering double rainbow across the horizon!',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Thank Neuvillette warmly & fold the umbrella as golden light bathes you',
                          'player_text': 'Thank you for the anniversary sunshine - and the double rainbow - '
                                         'Neuvillette. Look at the sky, Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Gazes up in wonder as golden light sparkles on her lashes.',
                          'reaction_reply': 'A double rainbow right over our bay! Even the Hydro Dragon is '
                                            'blessing our romance, Aether!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Admire the breathtaking double rainbow with Furina in your arms',
                          'player_text': "That's a sight we'll never forget - thank you, Monsieur "
                                         'Neuvillette!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Best weather miracle in history!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s4_ex2_cg3.jpg',
             'scene_label': '3/4 Climax: Neuvillette Smiling Gently as Golden Sunset Parting the',
             'scene_progress': 'SCENE 3/4',
             'narration': 'Giving the two of you a respectful nod so you can enjoy your private evening, '
                          'Neuvillette strolls away down the promenade while you hold Furina in the warm '
                          'golden glow beneath the double rainbow.',
             'inner_thought': "Salon Solitaire's Whisper: Held in Aether's arms beneath a double rainbow "
                              'blessed by Neuvillette himself...',
             'action_cue': 'Turns in your embrace by the ocean railing, looping her arms around your neck '
                           'with shining heterochromia eyes.',
             'speaker_line': 'With clear skies and a double rainbow overhead, mon amour... I think our '
                             'anniversary walk deserves a proper kiss right here!',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Kiss her deeply beneath the golden double rainbow',
                          'player_text': 'Happy anniversary, my beloved Furina - every sky is brighter with '
                                         'you in my arms.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Kisses you back with all her heart.',
                          'reaction_reply': 'Happy anniversary, my eternal love!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hold her close & watch the rainbow shimmer over the bay together',
                          'player_text': 'To many more rainbows and anniversaries together, my love!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Forever and always, Aether!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s5_ex1',
  'char_id': 'furina',
  'stage': 5,
  'order': 5,
  'scenario_num': 5,
  'is_extra_cameo': True,
  'cameo_cast': ['Navia', 'Clorinde', 'Lyney', 'Lynette'],
  'cameo_dynamic_tier': 'Stage 5 Grand Celebration Gala (Furina, Aether, Navia, Clorinde, Lyney & Lynette)',
  'allow_custom_input': True,
  'title': 'Fontaine Gala Toast to the Director & Her Leading Man',
  'subtitle': 'Stage 5 - Genshin Cameo 1 - Grand Opening Night Gala',
  'location': 'Grand Opera Ballroom Red Carpet',
  'cg_url': '/dating-media/furina_s5_ex1_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s5_ex1_cg4.jpg',
  'ending_scene_label': '4/4 Cameo: Grand Finale Curtain Call Kiss Applauded by All Their',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s5_ex1_cg1.jpg',
                   'label': '1/4 Opening: Opening Night Gala Red Carpet with Navia, Clorinde,'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s5_ex1_cg2.jpg',
                   'label': '2/4 Developing: The Entire Fontaine Cast Raising a Sparkling Toast'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s5_ex1_cg3.jpg',
                   'label': '3/4 Climax: Furina & Aether Sharing the Centerpiece Spotlight Waltz'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s5_ex1_cg4.jpg',
                   'label': '4/4 Cameo: Grand Finale Curtain Call Kiss Applauded by All Their'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': 'Walked the opening-night gala red carpet with Furina as Navia, Clorinde, Lyney, and Lynette '
                'raised a grand toast to you both as eternal partners.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s5_ex1_cg1.jpg',
             'scene_label': '1/4 Opening: Opening Night Gala Red Carpet with Navia, Clorinde,',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Crystal chandeliers blaze inside the Grand Opera Ballroom on opening night of '
                          "Furina's new musical masterpiece. Walking into the gala with Furina on your arm - "
                          'both of you wearing your matching sapphire-and-gold promise rings - you are '
                          'greeted by thunderous applause from Navia, Clorinde, Lyney, and Lynette!',
             'inner_thought': "Salon Solitaire's Whisper: Walking into the grand gala on Aether's arm with "
                              'our promise rings shining for all our friends to see...!',
             'action_cue': 'Beams with radiant pride, holding your arm closely as Navia, Clorinde, Lyney, '
                           'and Lynette surround the two of you with sparkling crystal flutes.',
             'speaker_line': '"Make way for the Genius Director Lady Furina and her eternal leading man, '
                             'Aether!" Navia cheers, lifting her glass high while Clorinde, Lyney, and '
                             'Lynette applaud.',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': "Hold Furina's ringed left hand up proudly & thank their Fontaine friends",
                          'player_text': 'Every standing ovation tonight belongs to Furina - and standing '
                                         'beside her as her partner is the greatest honor of my life.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Navia gasps at the matching promise rings on your fingers '
                                             'while Furina blushes radiantly.',
                          'reaction_reply': '"Wait - look at their left hands, Clorinde, Lyney! Matching '
                                            'sapphire-and-gold promise rings!!"'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Bow together with Furina & raise a sparkling glass with the whole cast',
                          'player_text': 'Thank you all for celebrating with us tonight - Furina poured her '
                                         'whole heart into this premiere!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'And Aether was my inspiration for every single scene!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s5_ex1_cg2.jpg',
             'scene_label': '2/4 Developing: The Entire Fontaine Cast Raising a Sparkling Toast',
             'scene_progress': 'SCENE 2/4',
             'narration': 'As Lyney and Lynette release a celebratory shower of golden rose petals and '
                          'sparkling Hydro ribbons from the balcony rail, Clorinde steps forward to clink '
                          "her glass respectfully against yours and Furina's.",
             'inner_thought': "Salon Solitaire's Whisper: All of our dearest friends from Fontaine are "
                              'celebrating our love openly!',
             'action_cue': 'Holds her crystal flute in one hand while keeping her ringed hand intertwined '
                           'with yours.',
             'speaker_line': '"A toast," Clorinde says with a warm, rare smile, echoed by Navia, Lyney, and '
                             'Lynette, "to Furina and Aether - may your story together outshine every stage '
                             'in Teyvat and beyond!"',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Clink glasses with everyone & lead Furina onto the ballroom floor for '
                                   'the',
                          'player_text': 'To our friends, and to the love of my life! Shall we take the '
                                         'centerpiece waltz, Furina?',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Steps into your arms at the center of the ballroom floor as '
                                             'the orchestra swells.',
                          'reaction_reply': "Gladly, mon amour - let's show them how soulmates dance!"},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Toast warmly with Navia, Clorinde, Lyney & Lynette',
                          'player_text': 'Cheers to the finest friends across two worlds!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Now dance for us, Director and Leading Man!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s5_ex1_cg3.jpg',
             'scene_label': '3/4 Climax: Furina & Aether Sharing the Centerpiece Spotlight Waltz',
             'scene_progress': 'SCENE 3/4',
             'narration': 'As the ballroom waltz reaches its crescendo under falling golden confetti, the '
                          'entire circle of Fontaine friends applauds as you dip Furina gracefully and kiss '
                          'her at center floor.',
             'inner_thought': "Salon Solitaire's Whisper: Kissing Aether in the center of the ballroom "
                              'surrounded by our cheering friends... my heart could burst with joy!',
             'action_cue': 'Wraps her arms around your neck as you dip her smoothly, kissing you under the '
                           'golden confetti.',
             'speaker_line': 'Best opening night gala in five hundred years, Aether! With you holding my '
                             'hand and our friends cheering us on, I have everything I ever dreamed of!',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Lift her back into a warm embrace & whisper how proud you are of her',
                          'player_text': 'You deserve every cheer in this hall and every ounce of my love, '
                                         'Furina - tonight and forever.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Rests her glowing cheek against yours.',
                          'reaction_reply': 'Forever and ever, my beloved leading man!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Take a joyous curtain-call bow together to the cheering ballroom',
                          'player_text': 'Encore to Director Furina!',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Encore to US, Aether!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]},
 {'id': 'furina_s5_ex2',
  'char_id': 'furina',
  'stage': 5,
  'order': 6,
  'scenario_num': 6,
  'is_extra_cameo': True,
  'cameo_cast': ['Neuvillette'],
  'cameo_dynamic_tier': 'Stage 5 Sacred Soulmate Blessing (Furina, Aether & Neuvillette)',
  'allow_custom_input': True,
  'title': "Neuvillette's Eternal Blessing by the Starlit Fountain",
  'subtitle': 'Stage 5 - Genshin Cameo 2 - Sacred Fontaine Blessing',
  'location': 'Starlit Fountain of Lucine Plaza',
  'cg_url': '/dating-media/furina_s5_ex2_cg1.jpg',
  'ending_cg_url': '/dating-media/furina_s5_ex2_cg4.jpg',
  'ending_scene_label': '4/4 Cameo: Embracing Beneath the Glowing Fountain of Lucine as',
  'cg_sequence': [{'scene_num': 1,
                   'url': '/dating-media/furina_s5_ex2_cg1.jpg',
                   'label': '1/4 Opening: Approaching the Starlit Fountain of Lucine Hand-in-Hand'},
                  {'scene_num': 2,
                   'url': '/dating-media/furina_s5_ex2_cg2.jpg',
                   'label': '2/4 Developing: Neuvillette Noticing Their Sapphire-and-Gold Promise'},
                  {'scene_num': 3,
                   'url': '/dating-media/furina_s5_ex2_cg3.jpg',
                   'label': '3/4 Climax: Neuvillette Offering His Solemn Blessing Over Pure'},
                  {'scene_num': 4,
                   'url': '/dating-media/furina_s5_ex2_cg4.jpg',
                   'label': '4/4 Cameo: Embracing Beneath the Glowing Fountain of Lucine as'}],
  'reward_affection': 35,
  'pass_threshold_score': 20,
  'summary_l2': "Received Chief Justice Neuvillette's solemn, heartfelt blessing over pure Fontaine spring "
                'water at the starlit Fountain of Lucine as eternal soulmates.',
  'nodes': [{'node_idx': 0,
             'cg_url': '/dating-media/furina_s5_ex2_cg1.jpg',
             'scene_label': '1/4 Opening: Approaching the Starlit Fountain of Lucine Hand-in-Hand',
             'scene_progress': 'SCENE 1/4',
             'narration': 'Beneath a canopy of silver stars at the Fountain of Lucine plaza, the luminous '
                          'waters shimmer with gentle blue light. Hand-in-hand with Furina - your matching '
                          'sapphire-and-gold promise rings glinting in the starlight - you approach Chief '
                          'Justice Neuvillette, who awaits beside the fountain basin.',
             'inner_thought': "Salon Solitaire's Whisper: I wanted Neuvillette - who watched over Fontaine "
                              'beside me for five centuries - to be the one to give us his official '
                              'blessing...',
             'action_cue': 'Steps up to the glowing fountain beside you, holding your ringed hand up with a '
                           'tender, emotional smile.',
             'speaker_line': 'Neuvillette... thank you for meeting us by the fountain tonight. Aether and I '
                             "wanted to show you these rings in person - because we've promised our futures "
                             'to each other forever.',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Stand tall beside Furina & vow to Neuvillette that you will cherish her',
                          'player_text': 'You have my solemn word, Neuvillette - for the rest of our lives '
                                         'and across every world, I will protect, love, and cherish Furina '
                                         'with all my heart.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': "Neuvillette's amethyst eyes soften with deep, unmistakable "
                                             'emotion as Furina squeezes your hand tightly.',
                          'reaction_reply': '"I have never once doubted your devotion, Aether - not since '
                                            'the day you stood beside her in Fontaine."'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': "Hold Furina's hand warmly & ask for the Iudex's blessing on your future",
                          'player_text': 'We wanted our closest guardian and friend from Fontaine to bless '
                                         'this new chapter, Neuvillette.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': '"There is no finer duty I could ever be asked to perform."'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 1,
             'cg_url': '/dating-media/furina_s5_ex2_cg2.jpg',
             'scene_label': '2/4 Developing: Neuvillette Noticing Their Sapphire-and-Gold Promise',
             'scene_progress': 'SCENE 2/4',
             'narration': 'Drawing a crystal chalice filled with the purest spring water of the Fountain of '
                          'Lucine, Neuvillette raises his hand as gentle, glowing Hydro droplets rise from '
                          'the fountain to encircle the two of you like a crown of starlight.',
             'inner_thought': "Salon Solitaire's Whisper: The waters of the Fountain of Lucine are singing "
                              'around Aether and me...',
             'action_cue': "Gazes at you with luminous, tear-bright heterochromia eyes as the fountain's "
                           'hydro light swirls around your joined hands.',
             'speaker_line': '"By the pure waters of Fontaine that remember every tear and every joy," '
                             'Neuvillette speaks in a resonant, deeply gentle voice, "I offer my eternal '
                             'blessing to Furina and Aether. May your days together be filled only with '
                             'warmth, music, and unbreakable love."',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Share a sip from the crystal chalice with Furina to seal the blessing',
                          'player_text': 'To a lifetime of warmth, music, and unbreakable love together, '
                                         'Furina.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Takes a sip from the crystal chalice after you, her cheeks '
                                             'glowing with sacred happiness.',
                          'reaction_reply': 'Sealed by the waters of Fontaine and by our hearts, mon amour!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Bow with gratitude to Neuvillette & hold Furina close to your heart',
                          'player_text': 'Thank you from the bottom of our hearts, Neuvillette.',
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': "Thank you, Neuvillette - I've never been happier in my entire "
                                            'life!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]},
            {'node_idx': 2,
             'cg_url': '/dating-media/furina_s5_ex2_cg3.jpg',
             'scene_label': '3/4 Climax: Neuvillette Offering His Solemn Blessing Over Pure',
             'scene_progress': 'SCENE 3/4',
             'narration': 'With a warm, paternal nod, Neuvillette turns and strolls quietly down the starlit '
                          'avenue - leaving the sky clear and sparkling with stars as you pull Furina into a '
                          'tender embrace beside the glowing fountain.',
             'inner_thought': "Salon Solitaire's Whisper: Blessed by Neuvillette, celebrated by all our "
                              "friends, and held in Aether's arms forever...",
             'action_cue': 'Rests her forehead against yours beside the shimmering fountain, her ringed hand '
                           'resting over your heart.',
             'speaker_line': 'Did you see how happy Neuvillette looked when he blessed us, Aether? Our past, '
                             'our present, and our eternity are all at peace... Kiss me under the fountain '
                             'stars, my love.',
             'mood': 'Lovestruck',
             'choices': [{'id': 'c1',
                          'score': 15,
                          'grade': 'BEST',
                          'label': 'Pull her into a deep, soulful kiss beside the starlit fountain',
                          'player_text': 'Every blessing in the world led to this moment, Furina. I love '
                                         'you, now and for all eternity.',
                          'reaction_thought': "Salon Solitaire's Whisper: Aether always knows the exact "
                                              'words to make my heart soar!',
                          'reaction_action': 'Kisses you deeply beneath the starlit waters, her soul '
                                             'completely intertwined with yours.',
                          'reaction_reply': 'And I love you, my eternal Traveler, my Aether - forever and '
                                            'always!'},
                         {'id': 'c2',
                          'score': 10,
                          'grade': 'GOOD',
                          'label': 'Hold her tight in the starlight & kiss her tenderly',
                          'player_text': "Here's to our eternity together, my beloved Furina.",
                          'reaction_thought': "Salon Solitaire's Whisper: He's so gentle and attentive every "
                                              "time we're together.",
                          'reaction_action': 'Smiles warmly and nods with a soft blush.',
                          'reaction_reply': 'Our happiest ever after, mon amour!'},
                         {'id': 'c3',
                          'score': 0,
                          'grade': 'AWKWARD',
                          'label': 'Act distracted or brush off the moment',
                          'player_text': "Sorry, I was checking the time - let's hurry this along.",
                          'reaction_thought': "Salon Solitaire's Whisper: Hmph! How can my leading man be "
                                              'checking the clock during a marquee scene?!',
                          'reaction_action': 'Places her hands on her hips with a theatrical pout.',
                          'reaction_reply': "Ahem! Eyes on the star of the show, Aether! Don't make "
                                            'Mademoiselle Crabaletta pinch your sleeve!'}]}]}]

FURINA_ALL_30_SCENARIOS: list[dict[str, Any]] = sorted(
    FURINA_20_SCENARIOS + FURINA_10_EXTRA_CAMEO_SCENARIOS,
    key=lambda s: (int(s["stage"]), int(s["order"])),
)
