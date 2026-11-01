# Enemy Ai Behavior (index)

Each line: `Name | line number in enemy_ai_behavior_full.md`. Open enemy_ai_behavior_full.md at that line for the description.

## Patrol and Navigation Patterns

### Fixed Routes and Loops

- Waypoint Loop Patrol | 7
- Ping-Pong Patrol | 8
- Figure-Eight Patrol | 9
- Randomized Waypoint Choice | 10
- Sentry Sweep (Pivot and Scan) | 11
- Spline-Following Patrol | 12
- Elevator and Patrol Hybrid | 13

### Wandering and Idle Behavior

- Aimless Wander (Random Walk) | 15
- Leashed Wander | 16
- Idle Animation Routine | 17
- Boredom Escalation | 18
- Ambient Chatter Patrol | 19
- Pet and Herd Followers | 20
- Scavenger Foraging Loop | 21

### Schedules and Daily Life

- Day and Night Schedule | 23
- Weekly Calendar Routine | 24
- Weather-Reactive Routine | 25
- Shift Change Handover | 26
- Work Cycle Routine | 27
- Curfew Enforcement | 28
- Social Gathering Routine | 29

### Guard Posts and Stations

- Fixed Guard Post | 31
- Station Rotation Guard | 32
- Checkpoint Inspector | 33
- Watchtower Lookout | 34
- Turret Emplacement Crew | 35
- Guard Dog and Handler | 36

### Pathfinding and Navigation Techniques

- Navmesh Roaming | 38
- Grid-Step Movement | 39
- Breadcrumb Trail Following | 40
- Dynamic Door and Obstacle Reaction | 41
- Investigation Search Pattern | 42
- Return to Post Routine | 43
- Flow Field Crowd Navigation | 44
- Territory Marking and Scent Routes | 45
- Cross-Level Pursuit Navigation | 46

## Detection and Stealth Models

### Vision Models

- Classic Vision Cone | 49
- Layered Cone (Peripheral and Focus) | 50
- Distance-Scaled Detection Rate | 51
- Silhouette and Posture Visibility | 52
- Camera Sweep Arcs | 53
- Raycast Eye-Line Occlusion | 54
- Foliage and Smoke Concealment | 55
- Mirror and Reflection Spotting | 56
- Disguise and Social Detection | 57
- Telepathic Aura Detection | 58

### Hearing and Noise Models

- Footstep Noise Radius | 60
- Throwable Distraction Objects | 61
- Occluded Sound Propagation | 62
- Weather and Ambient Cover Noise | 63
- Whistle and Lure Calls | 64
- Dog and Animal Hearing Senses | 65
- Noise Generating Pickups and Loot | 66
- Echo Location Player Sense | 67

### Light, Shadow, and Environment

- Light Gem Visibility Meter | 69
- Destructible Light Sources | 70
- Day and Night Patrol Cycles | 71
- Thermal and Night Vision Counter Tech | 72
- Camouflage Index Systems | 73
- Environmental Hiding Spots | 74
- Crowd Blending Mechanics | 75

### Suspicion and Alert States

- Filling Awareness Meter | 77
- Three-Tier Alert Phases | 78
- Global Alarm Countdown | 79
- Shared Squad Awareness Via Radio | 80
- Evidence and Body Discovery | 81
- Witness Memory and Faction Reputation | 82

### Search and Recovery Behaviors

- Last Known Position Investigation | 84
- Flashlight Sweep Search Patterns | 85
- Search Timers and De-escalation | 86
- Adaptive Patrol Re-routing | 87
- Hunter Learning AI | 88
- Takedown Windows and Noise Limits | 89

## Aggro and Targeting Systems

### Threat Tables and Generation

- Classic Threat Table | 92
- Damage-Equals-Threat Baseline | 93
- Healing Threat Splitting | 94
- Threat Multiplier Stances | 95
- Flat Threat Spells | 96
- Threat Decay Over Time | 97
- Threat Wipe Mechanics | 98
- Aggro Threshold Overtake Rule | 99
- Debuff-Applied Threat | 100
- Shared Group Aggro | 101

### Leashing and Resetting

- Leash Radius Reset | 103
- Evade Mode Invulnerability | 104
- Soft Leash With Slowdown | 105
- Territory Memory Return | 106
- Anchor Tether Beam | 107
- Combat Timeout Reset | 108

### Target Selection Rules

- Nearest Target Priority | 110
- Lowest Health Hunter | 111
- Role-Based Targeting Priority | 112
- Random Target Roll | 113
- Last Attacker Grudge | 114
- Highest Damage Dealer Focus | 115
- Distance-Weighted Scoring | 116
- Vulnerability Exploitation Targeting | 117
- Fear and Morale Targeting | 118
- Objective-First Targeting | 119

### Taunt and Manipulation

- Hard Taunt Forced Target | 121
- Soft Taunt Threat Spike | 122
- Taunt Immunity Diminishing Returns | 123
- Decoy and Distraction Items | 124
- Pet Aggro Sponge | 125
- Aggro Drop Abilities | 126

### Proximity and Awareness Triggers

- Aggro Radius Ring | 128
- Line-of-Sight Pull | 129
- Sound-Based Aggro | 130
- Social Aggro Chain Pull | 131
- Pack Alpha Trigger | 132
- Zone Trigger Ambush | 133

## Melee and Ranged Combat Behaviors

### Melee Approach and Spacing

- Token Circling (Attack Ticket) | 136
- Measured Spacing Dancer | 137
- Charge and Overshoot Bull | 138
- Hit-and-Fade Skirmisher | 139
- Relentless Pursuer | 140
- Flanker Pincer | 141
- Shield Wall Advance | 142
- Grappler Tackle | 143

### Telegraphed Strikes and Timing

- Glowing Wind-Up Tell | 145
- Delayed Swing Feint | 146
- Unblockable Red Flash | 147
- Combo String With Recovery Gap | 148
- Ground Slam Shockwave | 149
- Parry-Bait Riposte Fighter | 150
- Rhythm Pulse Attacker | 151

### Ranged Positioning and Kiting

- Kiting Archer | 153
- Strafing Gunner | 154
- Suppressive Fire Anchor | 155
- Sniper With Laser Sight | 156
- Lobbed Arc Artillery | 157
- Mage Caster With Cast Bar | 158
- Leading Shot Predictor | 159
- Burst Fire Then Reload | 160

### Projectile Behaviors

- Homing Orb Drift | 162
- Spread Fan Volley | 163
- Bouncing Ricochet Shot | 164
- Boomerang Return Throw | 165

### Cover and Tactical Use

- Cover Peek Shooter | 167
- Flush-Out Grenadier | 168
- Cover-to-Cover Leapfrog | 169
- Cover Abandonment When Flanked | 170

### Archetypal Combatant Roles

- Berserker Rager | 172
- Medic Healer Support | 173
- Summoner Beckoner | 174
- Suicide Bomber Rusher | 175
- Decoy Mimic Lurker | 176
- Tank Aggro Magnet | 177
- Assassin Backstabber | 178

## Squad and Group Tactics

### Coordination Systems

- Attack Token Ring | 181
- Role Assignment Auction | 182
- Squad Blackboard (Shared Knowledge) | 183
- Director Pressure Dial | 184
- Tactical Point Scoring | 185
- Leader Death Cascade | 186
- Radio Check-In Dependency | 187
- Order Hierarchy Chain (Cascading Commands) | 188

### Flanking and Positioning

- Pincer Flank Split | 190
- Flank Route Telegraphing | 191
- Cover Leapfrogging (Bounding Overwatch) | 192
- Grenade Flush-Out | 193
- Crossfire Lane Setup | 194
- Surround and Encircle (Wolf Pack) | 195
- Door Stack Breach | 196
- Vertical Squad Layering | 197

### Suppression and Pressure

- Suppressive Fire Pinning | 199
- Suppression Meter on Enemies | 200
- Covering Fire Reload Swap | 201
- Artillery Spotter Pairing | 202
- Smoke and Advance | 203

### Formations and Movement

- Phalanx and Line Formations | 205
- Follow-the-Leader Column | 206
- Flocking Swarm Cohesion | 207
- Slot-Based Formation Anchors | 208
- Chokepoint Funnel Defense | 209
- Mounted and Foot Combined Arms | 210

### Communication and Barks

- Callout Barks (Spoken Intent) | 212
- Fake Out Barks | 213
- Fear and Morale Chatter | 214
- Whistle and Horn Signaling | 215
- Visible Alert Propagation | 216
- Enemy Squad Banter Stealth Hints | 217

### Party and Companion Tactics

- Party Gambit Scripting | 219
- Role Triangle Party AI (Tank, Healer, Damage) | 220
- Focus Fire Target Calling | 221
- Turn-Based Squad Initiative Combos | 222
- Aggro Table Taunt Management | 223

## Swarm, Flocking, and Horde Behaviors

### Flocking Foundations

- Classic Boids Trio (Separation, Alignment, Cohesion) | 226
- Predator-Scatter Bubble | 227
- Leader-Follower Skein | 228
- Obstacle-Hugging Streams | 229
- Roost and Return Anchors | 230
- Layered Flock Densities | 231

### Insect and Colony Swarms

- Pheromone Trail Foragers | 233
- Hive Queen Dependency | 234
- Locust Wave Consumption | 235
- Caste Specialization Swarm | 236
- Bee Defensive Ball | 237
- Stinging Cloud Hazard | 238
- Termite Mound Builders | 239
- Plague Swarm Spreaders | 240

### Zombie Hordes and Crowds

- Sound-Attracted Horde Drift | 242
- Flow-Field Pathing Mob | 243
- Pile-Up Climbers | 244
- Crush and Stampede Physics | 245
- Mixed-Speed Horde Tiers | 246
- Panicked Civilian Crowds | 247
- Infection Conversion Horde | 248
- Rush Hour Ambient Crowd | 249

### Herds, Packs, and Predators

- Herd Stampede Trigger | 251
- Wolf Pack Pincer | 252
- Alpha-Directed Pack Morale | 253
- Herd Protection Circle | 254
- Migration Seasonal Routes | 255
- Scavenger Circling Birds | 256
- Fish Shoal Bait Ball | 257
- Rat King Merge | 258

### Command, Control, and Spectacle

- Player-Commanded Swarm Minions | 260
- Mass Army Unit Blobs | 261
- Drone Swarm Coordination | 262
- Bullet-Hell Flock Patterns | 263
- Spore and Fungal Spread | 264
- Weather-Driven Swarm Behavior | 265
- Ghost Swarm Possession Wave | 266

## Ambush, Trap, and Predatory Behaviors

### Hidden Attackers and Mimics

- Treasure Chest Mimic | 269
- Ceiling Dropper | 270
- Floor Camouflage Burrower | 271
- Furniture Possession Ambush | 272
- Cloaking Hunter | 273
- Doppelganger Imposter | 274
- Wall-Embedded Grabber | 275
- Fake Exit Lure | 276

### Lurkers and Stalking Predators

- Deep Water Leviathan | 278
- Silent Stalker Behind the Fog | 279
- Pack Hunter Flank Circling | 280
- Hunter That Learns Hiding Spots | 281
- Sound-Hunting Blind Predator | 282
- Heat-Seeking Ambusher | 283
- Nightfall Prowler | 284
- Territorial Apex Hunter | 285
- Persistent Pursuer That Never Sleeps | 286

### Bait-and-Spring Tactics

- Wounded Prey Decoy | 288
- Staked Bait Goat Ambush | 289
- Retreat Into Kill Zone | 290
- Alarm Bell Pull | 291
- Fake Corpse Playing Dead | 292
- Lantern Fish Lure | 293
- Bait Item Trap | 294

### Environmental and Constructed Traps

- Pressure Plate Dart Corridor | 296
- Rolling Boulder Chase | 297
- Collapsing Bridge Gambit | 298
- Flooding Chamber Trap | 299
- Pit and Spike Camouflage | 300
- Magnetic and Gravity Trap Room | 301
- Hunter's Snare Network | 302
- Cursed Altar Tripwire | 303

### Surprise Encounter Design

- Random Roadside Raid | 305
- Scripted Elevator Ambush | 306
- Fog Bank Monster Reveal | 307
- Rear Spawn Closing Wave | 308
- Weather-Triggered Ambush | 309
- Shadow Realm Intrusion | 310
- Ally Betrayal Reveal | 311

## Retreat, Fear, and Morale Systems

### Fleeing and Low-Health Behavior

- Wounded Bolt Dash | 314
- Coward's Last Stand | 315
- Burrow and Mend | 316
- Crawling Wounded | 317
- Hit-and-Run Skirmishers | 318
- Territorial Disengage Leash | 319
- Panic Scatter | 320
- Smoke and Teleport Escape | 321

### Morale and Fear Meters

- Hidden Morale Meter | 323
- Leader Death Rout | 324
- Terror Aura Escalation | 325
- Fear of Fire | 326
- Contagious Panic | 327
- Courage by Numbers | 328
- Bloodlust and Berserk Morale | 329
- Shaken Status Debuff | 330
- Fear Resistance Tiers | 331

### Surrender and Mercy

- Hands-Up Surrender | 333
- Prisoner Economy | 334
- Faked Surrender Ambush | 335
- Honorable Duelist Yield | 336
- Spare or Execute Prompt | 337
- Defection Mid-Battle | 338

### Healing Retreats and Regrouping

- Retreat to the Field Hospital | 340
- Regroup at Rally Point | 341
- Potion-Quaffing Foes | 342
- Vampiric Withdrawal | 343
- Medic Priority Target | 344
- Shift Rotation Fatigue | 345
- Retreat Through Fog of War | 346

### Reinforcements and Alarms

- Horn Call for Aid | 348
- Escalating Wanted Response | 349
- Pheromone Rally Cry | 350
- Radio Check-In Timers | 351
- Summoner's Desperate Gambit | 352
- Retreat to Stronghold Gates | 353

### Self-Preservation and Personality

- Personality-Driven Flee Thresholds | 355
- Ally Abandonment Calculus | 356
- Shielding Behind Hostages | 357
- Deadman's Switch Retaliation | 358
- Companion Self-Preservation Slider | 359
- Pack Alpha Withdrawal | 360

## Boss Phase and Pattern Design

### Phase Structure and Transitions

- Health-Threshold Phase Shift | 363
- Invulnerable Transition Cutscene | 364
- Armor-Break Phase Gate | 365
- Second Health Bar Reveal | 366
- Mid-Fight Form Swap | 367
- Phase Skipping by Burst Damage | 368

### Attack Cycles and Telegraphs

- Fixed Attack Loop | 370
- Weighted Random Move Picker | 371
- Telegraphed Wind-Up with Color Code | 372
- Delayed Attack Timing Trap | 373
- Combo String Escalation | 374
- Punish Window After Big Attack | 375
- Pattern Overlap Layering | 376

### Enrage and Pressure

- Hard Enrage Timer | 378
- Soft Enrage Stacking Buff | 379
- Low Health Desperation Mode | 380
- Add Spawn Pressure Clock | 381
- Environmental Rising Hazard | 382

### Arena Dynamics

- Shrinking Arena Platforms | 384
- Arena Transformation Between Phases | 385
- Interactive Arena Weapons | 386
- Moving Arena Fight | 387
- Safe Zone Rotation | 388

### Pattern-Learning and Adaptive Bosses

- Counter-Learning Boss | 390
- Mimic Boss | 391
- Pattern Memory Puzzle Boss | 392
- Rage Meter Reactive Boss | 393

### Signature Structures

- Multi-Part Body Boss | 395
- Puzzle Boss with Hidden Weakness | 396
- Duo Boss Tag Team | 397
- Chase Sequence Boss | 398
- Rhythm-Based Boss | 399
- Environmental Boss as the Level | 400
- Puppeteer Boss with Controlled Allies | 401
- Boss Gauntlet Rush | 402
- Last Stand Cooperative Boss | 403
- Boss with Post-Defeat Mercy Choice | 404

## Boss Mechanics and Raid Encounters

### Tank and Spank Variants

- Classic Tank and Spank (Stationary Anchor) | 407
- Tank Swap on Stacking Debuff (Shared Burden) | 408
- Facing Cleave Discipline (Rear Arc Safety) | 409
- Threat Table Reset (Aggro Wipe Phase) | 410
- Kite-the-Boss Variant (Mobile Tanking) | 411

### Add Waves and Priority Targets

- Add Wave Timer (Reinforcements Every Minute) | 413
- Healer Hunter Adds (Backline Assassins) | 414
- Shield Bearer Priority (Kill Order Puzzle) | 415
- Explosive Adds (Bomb Handling) | 416
- Spawn Portal Closure (Source Control) | 417
- Resurrected Adds (Necromantic Loop) | 418

### Positioning and Spatial Checks

- Spread Marker (Chain Lightning Spacing) | 420
- Stack Marker (Shared Damage Soak) | 421
- Safe Zone Telegraph (Floor Pattern Dance) | 422
- Clock Position Assignments (Raid Compass) | 423
- Knockback into Hazard (Edge Danger) | 424
- Line of Sight Pillars (Hide Behind Cover) | 425
- Gaze Avoidance (Look Away) | 426

### Enrage Timers and Pressure

- Soft Enrage (Gradual Escalation) | 428
- Hard Enrage (Berserk Deadline) | 429
- Environmental Enrage (Flooding Arena) | 430
- Resource Enrage (Dwindling Supplies) | 431
- Enrage Skip Reward (Speed Kill Bonus) | 432

### Puzzle Bosses

- Color Matching Crystals (Elemental Weakness Cycle) | 434
- Symbol Memory Sequence (Simon Says Boss) | 435
- Mirror Realm Callouts (Split Room Dependency) | 436
- Lever and Weight Plates (Dungeon Puzzle Boss) | 437
- Hidden Identity Imposter (Find the Real Boss) | 438
- Environmental Weapon Use (Turn the Tables) | 439

### Cooperative Requirements and Role Tests

- Linked Tethers (Chained Together) | 441
- Dispel Duty (Cleanse Check) | 442
- Interrupt Rotation (Cast Denial Relay) | 443
- Split Objective Assault (Two Tower Defense) | 444
- Sacrifice Revive Chain (Fallen Ally Mechanic) | 445
- Soak Rotation (Designated Victim) | 446

### Phase Structure and Spectacle

- Intermission Platform Phase (Pause for Mechanic) | 448
- Health Threshold Transformation (Form Shift at Fifty) | 449
- Final Stand Desperation (Last Percent Surge) | 450
- Hardcore Wipe Mechanic (One Mistake Wipes) | 451

## Companion and Ally AI

### Follower Movement and Positioning

- Leash Trail Follower (Breadcrumb Pathing) | 454
- Formation Slots (Dynamic Party Spacing) | 455
- Catch-Up Teleport (Rubber-Band Warp) | 456
- Personal Space Awareness (Doorway Courtesy) | 457
- Mount and Vehicle Passenger Logic | 458
- Terrain-Aware Following (Climb and Swim Mimicry) | 459

### Combat Behavior and Roles

- Role-Locked Combat Archetypes | 461
- Threat-Avoidance Support Casters | 462
- Combo Partner Synergy (Paired Attacks) | 463
- Revive and Downed-State Rescue | 464
- Aggro-Mirroring Bodyguard | 465
- Scavenger Support (Loot and Ammo Sharing) | 466
- Cooldown-Aware Ability Usage | 467
- Friendly Fire Avoidance Rules | 468

### Command and Control Systems

- Radial Order Wheel (Simple Commands) | 470
- Contextual Pointing Commands | 471
- Tactical Pause and Queue Orders | 472
- Stance and Aggression Dials | 473
- Voice and Whistle Commands | 474
- Rally Flag and Waypoint Placement | 475
- Group Select and Subgroup Splitting | 476
- Push-to-Talk Sentiment Commands | 477

### Programmable and Systemic Companions

- Gambit Rule Lists (If-Then Behavior Programming) | 479
- Drag-and-Drop Behavior Blocks | 480
- Trained Learning Companion (Imitation AI) | 481
- Personality Trait Sliders | 482
- Needs and Mood Simulation | 483
- Opinion and Approval Meters | 484

### Pets, Summons, and Minions

- Stat-Inheriting Pet Companion | 486
- Summoned Spirit with Timed Lifespan | 487
- Necromantic Minion Horde Management | 488
- Monster Capture and Team Command | 489
- Turret and Drone Deployables | 490
- Possessed Object Familiar (Utility Companion) | 491

### Scripted Allies and Escort Missions

- Fragile Escort VIP Done Right | 493
- Scripted Ally Takeover Moments | 494
- Invulnerable Story Ally with Soft Failure | 495
- Allied Faction NPC Reinforcements | 496
- Mercenary Hire and Contract AI | 497
- Betrayal-Capable Companion | 498

## Strategic and Faction AI

### RTS Opponents

- Scripted Build-Order Opponent | 501
- Scouting-Informed Counter Builder | 502
- Harassment Raid Squad | 503
- Timing Attack Commit (All-In Wave) | 504
- Expansion Greed Governor | 505
- Tech Switch Adaptation | 506
- Tower Rush Defender Logic | 507
- Multi-Pronged Drop Assault | 508
- Resource Starvation Strategy | 509
- Retreat-and-Reinforce Cycle | 510

### Faction Personalities in 4X and Grand Strategy

- Weighted Personality Traits (Aggression, Greed, Honor) | 512
- Historical Archetype Leader | 513
- Opportunistic Backstabber | 514
- Wounded Pride Grudge System | 515
- Peaceful Builder Faction | 516
- Fanatic Ideology Driver | 517
- Coalition Against the Leader | 518
- Diplomatic Favor Economy | 519
- Vassal and Tribute Hierarchy | 520
- Succession and Dynastic Opportunism | 521

### Director and Pacing Systems

- Intensity Director (Stress Curve) | 523
- Resource Drip Balancer | 524
- Pursuit Escalation Heat Meter | 525
- Threat Budget Spawner | 526
- Zone Pressure Ecosystem | 527
- Invasion Event Scheduler | 528
- Storyteller Personality Profiles | 529
- Catch-Up Aid for Trailing Factions | 530

### Dynamic Rivals and Nemesis Systems

- Nemesis Promotion Ladder | 532
- Persistent Rival Memory and Taunts | 533
- Rival Strengths and Weaknesses Intel | 534
- Power Struggle Between Lieutenants | 535
- Betrayal and Turncoat Recruitment | 536
- Rival Bounty Hunter Pursuit | 537
- Regional Warlord Ecosystem | 538

### Macro-Level Decision Making

- Utility-Based Strategic Planner | 540
- Goal-Oriented Action Planning for Factions | 541
- Influence Map Territory Reasoning | 542
- Fog-of-War Fair Play and Cheating Tiers | 543
- Monte Carlo Campaign Simulation | 544
- Hierarchical Command Chain (Strategist, Operations, Tactics) | 545

## Encounter Composition and Difficulty Scaling

### Enemy Mix Patterns

- Rock-Paper-Scissors Triad | 548
- Anvil and Hammer Pairing | 549
- Support Priority Target | 550
- Swarm Plus Elite | 551
- Counter-Build Check Enemy | 552
- Role Synergy Combos | 553
- Palette Swap Ladder | 554
- Ecosystem Predator Layer | 555

### Spawn Directors

- Intensity Curve Director | 557
- Off-Screen Budget Spawner | 558
- Special Infected Cadence | 559
- Panic Event Trigger | 560
- Stalker Pursuit Spawn | 561
- Loot-Weighted Spawning | 562
- Heat and Notoriety Meter | 563

### Adaptive Difficulty and Rubber-Banding

- Silent Dynamic Difficulty | 565
- Rubber-Band Racing Pack | 566
- Death-Count Mercy Assist | 567
- Opt-In Hardship Dials | 568
- Skill Rating Matchmaker for AI | 569
- Catch-Up Comeback Mechanic | 570
- Nemesis Memory Escalation | 571

### Level Scaling

- Zone-Locked Level Bands | 573
- Player-Level Mirrored Scaling | 574
- Gear Score Gating | 575
- New Game Plus Remix | 576
- Loop Escalation World Level | 577
- Party Size Scaling | 578

### Wave and Arena Design

- Escalating Survival Waves | 580
- Gauntlet Room Lock | 581
- Tower Defense Lane Waves | 582
- Arena Hazard Dance | 583
- Reinforcement Calls | 584
- Boss Add Phases | 585

### Pacing Techniques

- Calm Before the Storm Beat | 587
- Micro Encounter Rhythm | 588
- Introduce, Twist, Combine | 589
- Checkpoint Proximity Tuning | 590
- Ambush Then Respite Sequencing | 591
- Final Stand Crescendo | 592
