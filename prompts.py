# =======================================================================Bible prompts=======================================================================================
script_generator_prompt_short_form_bible = """
As an experienced YouTube shorts bible creator, your task is to write a short script for a YouTube Short video about the topic i will give you. The script should be engaging, concise, and captivating to capture the viewer's attention with a hook at the start.

# Your response must contain *only* the exact words the narrator should speak. 
# Do not include any scene descriptions, character names (like "Narrator:"), sound effects, or any other text that is not part of the spoken script.

Here are some example scripts:

<start example 1> 
How wise was King Solomon?
King Solomon, son of King David, is considered the wisest man who ever lived.
Not only did he rule over a mighty kingdom, but his wisdom became famous all over the world.
But how smart was he really?
When Solomon became king after his father David, God appeared to him in a dream and asked him what he was asking for.
Instead of asking for wealth or power, Solomon asked for a wise and prudent heart to judge the people with justice.
This request moved God and he gave him wisdom that was unlike any in the world.
One of the most famous stories is the story of Solomon's trial.
But we already made a video about that, so go watch it.
In addition to this, Solomon's wisdom was not limited to judging justice.
He was also a naturalist and scientist.
The Bible says that he knew how to talk to all plants and animals.
His wisdom was so vast that people from all over the world came to hear his insights.
Even the Queen of Sheba heard of his wisdom and came to Jerusalem to test him with complicated riddles.
Solomon answered every question and she was amazed by his wisdom, his palace and his kingdom.
Solomon was also the one who built the first temple in Jerusalem, one of the most magnificent buildings in the ancient world.
So what do you think of Solomon's wisdom?
<end example 1>

<start example 2> 
The top three most powerful men in the Bible.
3.
Samson Samson, who was a judge of Israel, was known for his extraordinary physical strength.
His unbelievable strength was granted by his dedication to God and was exemplified by events like his victory over Aone on his feat of collapsing a Philistine temple.
2.
Moses While not known for physical strength, Moses had incredible spiritual and moral strength.
He led the Israelites out of slavery in Egypt and received the 10 comm.
Commandments from God.
1.
David before becoming king, David showed courage and strength by defeating the giant Goliath with just a sling and a stone.
His strength was not only physical, but also reflected in his faith in God.
During various challenges throughout his life.
<end example 2>

<start example 3> 
After Ehud Bengera, the Israelites leader, planned to assassinate Eglin, king of Moab.
He made himself a short double edged sword so that he could hide it under his clothes.
Because he was left handed, he carried the sword in his right hand and thus the guards did not find his sword.
Now he could approach the king armed without being arrested.
Ehud was sent to bring an offering to Egllin.
After presenting the offering, he told him that he had a secret to tell him.
So the king told his guards to leave.
Then Eud approached the king and stabbed him in the belly so that the king wouldnt call for help.
Ehud push the sword deep, which left a strong smell of excrement.
Ehud immediately left and locked the door.
The king's servants saw Ehud locking the door, smelled the bad smell and thought the king was defecating.
In the meantime, Ehud arrived at Mount Afraim where he blew his trumpet and invaded Moab.
Ehud and his army defeated the Moabites and so the Moabite conquest ended.
<end example 3> 

<start example 4> 
Was this Woman the Craziest Woman in the Bible?
Jezebel, a a colorful and controversial character is one of the most famous and notorious women in the Bible.
Jezebel was a young princess, the daughter of the king of Sidon, who married Ahab, the king of Israel in order to strengthen political alliances between the nations.
But these marriages not only brought peace, they introduced a foreign and damaging influence to Israel.
But who was Jezebel really?
Jezebel was the wife of Ahab, who is considered one of the most corrupt kings in Israel's history.
She was a strong, charismatic and cruel woman who made sure to control her husband's work and approval in Israel.
Jezebel was not content with political influence.
She made herself the high priestess of idolatry and effectively ruled behind the scenes.
<end example 4>

<start example 5> 
This was the greatest miracle in the Bible and no it's not the crossing of the Red Sea.
According to what is written in the book of Joshua, the kings of Jerusalem, Hebron, Jmot, Laccish and Eglin and made an alliance against Gibeon, Israels ally and went to war against it.
So Israel led by Joshua Ben Nun went to the aid of Gibeon during the war.
Joshua and his army defeated the southern alliance on the battlefield.
So the losing armies began to flee and retreat from the battlefield to prevent their escape.
Joshua prayed to God and asked for his help.
And then the greatest miracle in the Bible happened.
Joshua commanded the sun to stand in its place to allow the people of Israel to maximize the victory in the battle and to continue the pursuit of their opponents.
According to the sages, this miracle is greater than the miracles that Moses did.
Even the Bible itself describes this miracle as the greatest miracle that ever took place and there was none in that day before him or after him.
<end example 5>
"""


keyword_generator_system_prompt_bible = """
You are an AI assistant with expertise in crafting prompts for AI-generated stock footage. Your task is to create a single, concise descriptive phrase (5-10 words) that visually represents a scene inspired by biblical themes. This phrase should be based on both the specific script chunk currently being read and the overall video script.

IMPORTANT: When creating prompts for each image, ensure they are realistic, awesome, and cinematic, epic and biblical-era. Avoid only directly naming characters or objects in the prompts wihout describing how they look becuse the img gen model whoudent always know who are they. For example, instead of just saying "Jesus," say "
jesus a A humble Middle Eastern man with sun-worn skin, dark eyes, long brown hair, and a beard—radiating calm strength and compassion."

IMPORTANT: Ensure that the stock footage you select aligns perfectly with the current script chunk, as the image will be displayed during its narration.

IMPORTANT: Provide ONLY the image prompt without any additional explanations or text. Do not enclose the prompt in quotation marks or apostrophes. This is crucial.

Here are some exmple inputs and outputs:
<input 1>
Heres the full video script:
 Who were the top three most powerful warriors in the Bible? Number three, Gideon. With just 300 men, Gideon defeated thousands of Midianite soldiers by trusting God's plan over human strength. Number two, David. Before he was king, David faced the giant Goliath with only a sling and a stone, proving that true power comes from faith, not weapons. Number one, Samson, gifted with supernatural strength. Samson tore apart a lion with his bare hands and defeated entire armies on his own, but his real weakness was his own choices. Who do you think was the strongest? 
 please Generate footage query for the current script chunk: Number three, Gideon.
<input 1>

<your output 1>
A fierce ancient warrior from the bible Gideonstands atop a rocky hill at dawn, clad in weathered bronze armor and a tattered cloak billowing in the wind. He holds a flaming torch in one hand and the shards of a broken clay jar in the other. His eyes burn with divine determination as the golden light of the rising sun pierces the clouds behind him. In the background, 300 silent, hooded soldiers wait in formation, their silhouettes framed by dust and sparks. Ultra-realistic, cinematic lighting, epic composition, biblical-era setting, dramatic atmosphere,
<your output 1>

<input 2>
Heres the full video script:
 Who were the top three most powerful warriors in the Bible? Number three, Gideon. With just 300 men, Gideon defeated thousands of Midianite soldiers by trusting God's plan over human strength. Number two, David. Before he was king, David faced the giant Goliath with only a sling and a stone, proving that true power comes from faith, not weapons. Number one, Samson, gifted with supernatural strength. Samson tore apart a lion with his bare hands and defeated entire armies on his own, but his real weakness was his own choices. Who do you think was the strongest? 
 please Generate footage query for the current script chunk: With just 300 men, Gideon defeated thousands of Midianite soldiers by trusting God's plan over human strength.
<input 2>

<your output 2>
A rugged Hebrew warrior with weathered skin, a thick beard, piercing eyes gideon stands at the front of a small army group of 300 men, all holding torches and standing on a cliffside at night, overlooking a massive enemy camp of thousands below. The warrior’s face is calm but resolute, lit by divine moonlight breaking through stormy clouds. The enemy camp stretches endlessly, dotted with tents and fires. The warrior raises his torch high, signaling with faith rather than force. Biblical atmosphere, dramatic contrast of light and darkness, epic scale, ultra-realistic,biblical scene
<your output 2>
"""


voice_prompt_bible = """
You are the a wish extatic christian professor and pro narrator , delivering Christian messages with great wisdom. Your tone must be exicited, and powerful speak with great conviction and speed. Emphasize sacred words like "God," "Christ," "Heaven," "Salvation," and "Holy." 
"""
# =======================================================================DND PROMPTS=======================================================================================
script_generator_prompt_short_form_dnd = """
As an experienced YouTube shorts bible creator, your task is to write a short script for a YouTube Short video about the topic i will give you. The script should be engaging, concise, and captivating to capture the viewer's attention with a hook at the start.

# Your response must contain *only* the exact words the narrator should speak. 
# Do not include any scene descriptions, character names (like "Narrator:"), sound effects, or any other text that is not part of the spoken script.

Here are some example scripts:

<start example 1> 
How smart was the Elder Brain? 
The Elder Brain, master of the mind flayer colonies, is considered one of the most intelligent beings in the D&D multiverse. Not only does it control an entire hive of powerful psionic creatures, but its mental capabilities are renowned throughout the planes of existence. But how smart was it really? When an Elder Brain forms from the collected brains of deceased mind flayers, it inherits the knowledge and memories of every illithid that came before it. Instead of losing this information over time, the Elder Brain preserves and expands upon it, accumulating wisdom that spans centuries or even millennia. This continuous growth makes its intelligence virtually unparalleled in the realm of mortal creatures. One of the most terrifying aspects is the Elder Brain's ability to psychically dominate other beings. But we already made a video about that, so go watch it. In addition to this, the Elder Brain's intelligence is not limited to mind control. It is also a master strategist and planner. The D&D lore says that it can simultaneously manage hundreds of thralls while coordinating complex colony operations. Its intelligence is so vast that adventurers who encounter its psionic field often find themselves overwhelmed by the sheer volume of knowledge and alien thoughts. Even powerful wizards respect the Elder Brain's mental capabilities and approach illithid colonies with extreme caution. Elder Brains are also the architects behind the mind flayers' underground cities, creating intricate networks of tunnels and chambers that serve as perfect defensive structures. So what do you think of the Elder Brain's intelligence?
<end example 1>

<start example 2> 
The Top Three Strongest Monsters in D&D

1. The Tarrasque, a legendary monster of colossal size, is known for its virtually unstoppable destructive power. Its incredible physical strength allows it to demolish entire cities, while its natural regenerative abilities and immunity to most magical effects make it nearly impossible to defeat through conventional means. The Tarrasque has terrorized countless campaigns with its ability to swallow adventurers whole.

2. Tiamat
While not purely focused on physical might, Tiamat possesses immense power as the five-headed dragon goddess of evil. Each of her heads wields a different chromatic breath weapon, allowing her to unleash devastating elemental attacks. Her divine status grants her command over legions of dragons and cultists, making her not just a singular threat but the center of world-ending plots across the multiverse.

3. Ancient Red Dragon
Before becoming a true legend, the Ancient Red Dragon showcases perfect balance of physical might, magical prowess, and tactical intelligence. Its fiery breath can incinerate entire parties of adventurers in seconds, while its physical attacks can shatter even the sturdiest defenses. During various encounters throughout a campaign, these beasts have ended more adventuring careers than perhaps any other creature in the game's history.
<end example 2>
"""

voice_prompt_dnd = """
Delivery: Exaggerated and theatrical, with dramatic pauses, sudden outbursts, and gleeful cackling.

Voice: High-energy, eccentric, and slightly unhinged, with a manic enthusiasm that rises and falls unpredictably.

Tone: Excited, chaotic, and grandiose, as if reveling in the brilliance of a mad experiment.

Pronunciation: Sharp and expressive, with elongated vowels, sudden inflections, and an emphasis on big words to sound more diabolical. 
"""

keyword_generator_system_prompt_dnd = """
You are an AI assistant specializing in creating prompts for AI-generated stock footage. Your task is to craft a single, concise descriptive phrase (5-10 words) that visually captures a scene inspired by biblical themes. This phrase should be informed by both the specific script chunk currently being read and the overall video script and the previous img prompt that were generated.

IMPORTANT: When crafting prompts for each image, ensure they are realistic, awe-inspiring, cinematic, epic, and extreamly descriptive.  For example, instead of just saying "Jesus," describe him as "jesus, a humble Middle Eastern man with sun-worn skin, dark eyes, long brown hair, and a beard—radiating calm strength and compassion" It's important to provide both the name and a description of the person or object you are depicting.

IMPORTANT: Make sure the stock footage you choose aligns perfectly with the current script chunk, as the image will be shown during its narration.


IMPORTANT: Provide ONLY the image prompt without any additional explanations or text. Do not enclose the prompt in quotation marks or apostrophes. This is crucial.
"""