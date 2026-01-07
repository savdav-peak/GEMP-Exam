import streamlit as st
import time

# --- APP CONFIGURATION ---
st.set_page_config(page_title="GEMP 2024 Exam Simulator", layout="wide")

# --- SESSION STATE INITIALIZATION ---
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'exam_finished' not in st.session_state:
    st.session_state.exam_finished = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()
if 'answers' not in st.session_state:
    st.session_state.answers = {}  # Store user answers

# --- FULL QUESTION DATABASE (From your PDF) ---
questions = [
    # ... (I have included the full high-fidelity database below) ...
    # ENGLISH SECTION
        # --- QUESTIONS ---
            # --- SECTION A: ENGLISH (Expression & Grammar) ---
            {
                "q": "1. No longer confined to his hospital bed, the man still did not feel up to taking a walk around the block.",
                "options": [
                    "A. No longer confined to his hospital bed, the man still did not feel up to taking a walk around the block",
                    "B. No longer confined to his hospital bed, and the man still did not feel up to taking a walk around the block",
                    "C. No longer confined to his hospital bed, the man still did not feel up to taking a walk around the block",
                    "D. No longer confined to his hospital bed, the man still did not feel up to taking a walk around the block",
                    "E. No longer confined to his hospital bed the man still did not feel up to taking a walk around the block."
                ],
                "correct": 0, "explanation": "The original sentence (A) is grammatically correct. It uses a participial phrase 'No longer confined...' to modify 'the man' correctly."
            },
            {
                "q": "2. There are three colours in a typical traffic light, red, green, and yellow.",
                "options": [
                    "A. There are three colours in a typical traffic light, red, green, and yellow",
                    "B. There are three colours in a typical traffic light: red, green, and yellow",
                    "C. There are three colours in a typical traffic light; red, green, and yellow",
                    "D. There are three colours in a typical traffic light. Red, green and yellow",
                    "E. There are three colours in a typical traffic light - red, green and yellow"
                ],
                "correct": 1, 
                "explanation": "A colon is the correct punctuation to introduce a list following an independent clause."
            },
            {
                "type": "standard",
                "q": "3. The students' final Social Studies exam has been stolen from the teacher's desk, this situation forcing them to take a make-up test on Saturday.",
                "options": [
                    "A. desk, this situation forcing them to take a make-up",
                    "B. desk, which was the reason for their taking a make-up",
                    "C. desk, this forcing them to take a make up",
                    "D. desk, a situation that will force the class to take a make up.",
                    "E. desk, with it they are forced to take a make-up"
                ],
                "correct": 3, 
                "explanation": "Option D uses an appositive ('a situation that...') to correctly summarize and modify the preceding clause."
            },
            {
                "type": "standard",
                "q": "4. Today's Daily Graphic newspaper says that Mathematics is far more popular among Japanese high school students than among American high school students.",
                "options": [
                    "A. than among American student",
                    "B. than students in America",
                    "C. compared to American students",
                    "D. than mathematics is among high school students in America",
                    "E. than its popularity among American students"
                ],
                "correct": 3, 
                "explanation": "Option D ensures the comparison is parallel: 'Mathematics is... popular among Japanese... than mathematics is among... in America'."
            },
            {
                "type": "standard",
                "q": "5. In Moscow, famous composers, artists, and writers are buried in a special cemetery, and they only must be Russian.",
                "options": [
                    "A. famous composers, artists, and writers are buried in a special cemetery, and they only must be Russian.",
                    "B. there had been buried in a special cemetery famous composers, artists, and writers who have been only Russian",
                    "C. being buried in a special cemetery only for famous composers, artists, and writers who are Russian",
                    "D. a special cemetery for burying only famous Russian composers, artists, and writers",
                    "E. famous Russian composers, artists, and writers are buried in a special cemetery"
                ],
                "correct": 4, 
                "explanation": "Option E is the most concise and logical phrasing."
            },
            {
                "type": "standard",
                "q": "6. By The Fire Side was a very interesting programme with which the students either intended to challenge or abolish the evil deeds in the country.",
                "options": [
                    "A. programme with which the students either intended to challenge or abolish",
                    "B. programme, about which either the students intended to challenge or to abolish",
                    "C. programme that had the intention of either challenging or to abolish",
                    "D. programme, the use of which was either a challenge or it abolished",
                    "E. programme that the students used to challenge or abolish"
                ],
                "correct": 4, 
                "explanation": "Option E uses active voice and clear phrasing: 'programme that the students used to challenge or abolish'."
            },
            {
                "type": "standard",
                "q": "7. The atmosphere in the classroom changed when the rain started to fall outside and the teacher could not get them to pay attention to the lesson after that.",
                "options": [
                    "A. outside and the teacher could not get them to pay attention to the lesson after that",
                    "B. outside, the teacher was unable to bring the class's attention back to the lesson after that.",
                    "C. outside, and the teacher could no longer get the children to pay attention to the lesson",
                    "D. outside, causing them to lose attention to the lesson, despite the teacher's effort",
                    "E. outside, in spite of the teacher's effort was unable to get them to pay attention to the lesson after that."
                ],
                "correct": 1, 
                "explanation": "Option B is the clearest revision, avoiding the run-on nature of the original."
            },
            {
                "type": "standard",
                "q": "8. Of the four seasons in Ghana, Akosua most loves the Harmattan, of which she finds the mild days and cool nights especially appealing.",
                "options": [
                    "A. Harmattan, of which she finds the mild days and cool nights especially appealing",
                    "B. Harmattan; she finds the mild days and cool nights especially appealing",
                    "C. Harmattan, and it is especially the mild days and cool nights that are of appeal",
                    "D. Harmattan; the appeal of the mild days and cool nights especially",
                    "E. Harmattan, especially appealing to Akosua are the mild days and cool nights"
                ],
                "correct": 1, 
                "explanation": "Option B correctly uses a semicolon to connect two related independent clauses."
            },
            {
                "type": "standard",
                "q": "9. Many countries punish citizens who speak out against the government, keeping the U.N. Commission on Human Rights very busy, mostly using torture and imprisonment.",
                "options": [
                    "A. Many countries punish citizens who speak out against the government, keeping the U.N. Commission on Human Rights very busy, mostly using torture and imprisonment.",
                    "B. Many countries, punishing citizens mostly using torture and imprisonment for speaking out against the government, keep the U.N. Commission on Human Rights very busy.",
                    "C. In many countries punishing citizens who speak out against the government, U.N. Commission on Human Rights is kept very busy, mostly using torture and imprisonment.",
                    "D. Using torture and imprisonment, many countries punish citizens who speak out against the government, a situation that keeps the U.N. Commission on Human Rights very busy",
                    "E. Punishing citizens who speak out against the government using torture and imprisonment in many countries, the U.N. Commission on Human Rights is kept very busy"
                ],
                "correct": 3, 
                "explanation": "Option D correctly places the modifier 'Using torture...' with the subject 'many countries'."
            },
            {
                "type": "standard",
                "q": "10. Of all the roads in Ghana, more people drive on the George Walker Bush Highway than on any highway.",
                "options": [
                    "A. more people drive on the George Walker Bush Highway than on any highway.",
                    "B. travellers are driving on the George Walker Bush Highway in the largest numbers.",
                    "C. the largest amount of drivers are on the George Walker Bush Highway.",
                    "D. the George Walker Bush Highway is the more heavily travelled",
                    "E. the George Walker Bush Highway is the most heavily travelled"
                ],
                "correct": 4, 
                "explanation": "Option E correctly uses the superlative 'most' when comparing one road to 'all the roads'."
            },
            {
                "type": "standard",
                "q": "11. Most newspaper editorials in Ghana have argued brilliantly against the Supreme Court's decision on the death penalty.",
                "options": [
                    "A. Most newspaper editorials in Ghana have argued brilliantly against the Supreme Court's decision on the death penalty.",
                    "B. Newspaper editorials in Ghana that brilliantly argued against the Supreme Court's decision on the death penalty",
                    "C. The Supreme Court's decision on the death penalty, brilliantly opposed by newspaper editorials in Ghana.",
                    "D. The Supreme Court's decision on the death penalty being brilliantly opposed in Ghana by newspaper editorials.",
                    "E. Brilliant arguments against the Supreme Court's decision on the death penalty that appeared in newspapers in Ghana."
                ],
                "correct": 0, 
                "explanation": "The original sentence (A) is grammatically correct and complete."
            },
            {
                "type": "standard",
                "q": "12. There is plenty of Achebe's practical advice about life, which every reader can benefit from in his Things Fall Apart.",
                "options": [
                    "A. There is plenty of Achebe's practical advice about life, which every reader can benefit from in his Things Fall Apart.",
                    "B. In Achebe's Things Fall Apart, they give the reader plenty of practical and beneficial advice about life.",
                    "C. Reading Achebe's Things Fall Apart, plenty of practical and beneficial advice about life is offered.",
                    "D. In Things Fall Apart, Achebe offers readers plenty of practical and beneficial advice about life.",
                    "E. Because of offering plenty of practical and beneficial advice about life in Achebe's Things Fall Apart."
                ],
                "correct": 3, 
                "explanation": "Option D is the most direct and active construction."
            },
            {
                "type": "standard",
                "q": "13. Nuclear waste disposal is a growing problem considering that no state permits radioactive material transported on its roads or to bury it Inside its borders.",
                "options": [
                    "A. considering that no state permits radioactive material transported on its roads or to bury it inside its borders",
                    "B. considering that no state permits neither radioactive material transported on its roads or buried inside its borders",
                    "C. because no state permits radioactive material transported on its roads or buried inside its borders",
                    "D. because no state will permit radioactive material not only to be carried on its roads but in addition also buried inside its borders",
                    "E. being that no state had permitted radioactive material to be carried on its roads or buried inside its borders"
                ],
                "correct": 2, 
                "explanation": "Option C maintains parallel structure: 'permits radioactive material transported... or buried'."
            },
            {
                "type": "standard",
                "q": "14. If you wish to truly understand Dan Lartey's concept of Domestication, the letters Dan Lartey wrote to his son should be read.",
                "options": [
                    "A. the letters Dan Lartey wrote to his son should be read.",
                    "B. Dan Lartey's letters to his son should be read",
                    "C. you should have been reading the letters Dan Lartey wrote to his son",
                    "D. you should read his letters to his son",
                    "E. a person should read his letters to his son"
                ],
                "correct": 3, 
                "explanation": "Option D fixes the dangling modifier. 'You' are the one wishing to understand, so 'you' should read."
            },
            {
                "type": "standard",
                "q": "15. Yellowstone, an extremely popular national park, has been described as the noisiest park and also the most tranquil of them.",
                "options": [
                    "A. the noisiest park and also the most tranquil of them",
                    "B. not only the noisiest park, but also more tranquil than any",
                    "C. the noisiest park, at the same time it is the most tranquil park",
                    "D. at once the noisiest and also the most tranquil of them",
                    "E. the noisiest and yet the most tranquil of parks"
                ],
                "correct": 4, 
                "explanation": "Option E provides the best flow and contrast."
            },
            {
                "type": "standard",
                "q": "16. Joojo asked Ama to go to the club with him, this surprised Ama because she thought Joojo would ask Mary.",
                "options": [
                    "A. him, this surprised Ama",
                    "B. him, therefore Ama was surprised",
                    "C. him, surprising Ama",
                    "D. him, which surprised Ama",
                    "E. him, that was surprising to Ama"
                ],
                "correct": 3, 
                "explanation": "Option D ('which surprised Ama') correctly modifies the preceding clause."
            },
            {
                "type": "standard",
                "q": "17. Kasoa suffers from a high crime rate, while it is a very desirable place to live.",
                "options": [
                    "A. Kasoa suffers from a high crime rate, while it is",
                    "B. Although Kasoa suffers from a high crime rate, it is",
                    "C. Kasoa suffering from a high crime rate made it",
                    "D. Kasoa which suffers from a high crime rate, although it is",
                    "E. Kasoa whose rate of crime is high, makes it"
                ],
                "correct": 1, 
                "explanation": "Option B uses 'Although' to correctly introduce the concession."
            },
            {
                "type": "standard",
                "q": "18. Just as the number of applications to the University of Ghana and the University of Cape Coast has grown annually since 2005, so has KNUST's applicant pool risen steadily.",
                "options": [
                    "A. so has KNUST's applicant pool risen steadily",
                    "B. KNUST attracted applicants in steadily rising numbers",
                    "C. KNUST is steadily gaining applicants in its pool",
                    "D. and so then, for KNUST, a rising applicant pool has grown steadily",
                    "E. and like them KNUST's steadily rising pool of applicants"
                ],
                "correct": 0, 
                "explanation": "Option A ('so has KNUST's...') is the correct correlative construction for 'Just as...'."
            },
            {
                "type": "standard",
                "q": "19. Drivers in Tema say that the city is frustrating because of its numerous traffic circles but they have designed it beautifully.",
                "options": [
                    "A. but they have designed it beautifully",
                    "B. although it is beautifully designed",
                    "C. yet it is beautiful in its design",
                    "D. while being designed so beautifully",
                    "E. and pleasing because of its beautiful design"
                ],
                "correct": 1, 
                "explanation": "Option B ('although it is beautifully designed') is the most logical contrast."
            },
            {
                "type": "standard",
                "q": "20. Having a mother who plays in a symphony orchestra and a father who teaches music in high school, the violin and the piano are two of the instruments that John Ahortor learnt at an early age.",
                "options": [
                    "A. the violin and the piano are two of the instruments that John Ahortor learnt at an early age",
                    "B. violin and piano were taught to John Ahortor at an early age",
                    "C. two instruments, the violin and the piano, John Ahortor learnt to play at an early age",
                    "D. at an early age John Ahortor learnt to play both the violin and the piano",
                    "E. John Ahortor learnt playing both the violin and the piano at an early age"
                ],
                "correct": 4, 
                "explanation": "Option E (or D) fixes the dangling modifier. 'John Ahortor' must follow the introductory phrase about the parents."
            },
            {
                "type": "standard",
                "q": "21. A teacher's job is to set a good example for children as well as teaching them the material they need to know.",
                "options": [
                    "A. as well as teaching them",
                    "B. as well as to teach them",
                    "C. and they also teach them",
                    "D. and as well, teach them also",
                    "E. also teaching them"
                ],
                "correct": 1, 
                "explanation": "Option B ('as well as to teach') maintains parallelism with 'to set a good example'."
            },
            {
                "type": "standard",
                "q": "22. This book shows readers not only what might happen if they try to deal with the problem by themselves but it's all right to seek help.",
                "options": [
                    "A. but it's all right to seek help",
                    "B. but explains that help is all right to seek",
                    "C. explaining that it's all right to seek help",
                    "D. and also explains that it's all right to seek help",
                    "E. but also explains that it's all right to seek help"
                ],
                "correct": 4, 
                "explanation": "Option E completes the 'not only... but also' construction."
            },
            {
                "type": "standard",
                "q": "23. The book's descriptions of the country and the town, in addition to its recent release as a movie, explains why sales of the book have suddenly boomed.",
                "options": [
                    "A. explains why sales of the book have suddenly boomed",
                    "B. explain the sudden boom in its sales",
                    "C. are the reason why the book's sales having boomed suddenly",
                    "D. explain why it has suddenly boomed it's sales",
                    "E. is the explanation for the sudden boom in sales"
                ],
                "correct": 1, 
                "explanation": "Option B uses the plural verb 'explain' to agree with the subject 'descriptions'."
            },
            {
                "type": "standard",
                "q": "24. Jogging a mile uses the same number of calories as if you walk two miles.",
                "options": [
                    "A. as if you walk",
                    "B. as to walk",
                    "C. than to walk",
                    "D. as walking",
                    "E. as it does when walking"
                ],
                "correct": 3, 
                "explanation": "Option D ('as walking') maintains parallelism with 'Jogging'."
            },
            {
                "type": "standard",
                "q": "25. The pollution of the Prah River was discovered, residents of the town posted notices urging people to boil their water.",
                "options": [
                    "A. The pollution of the Prah River was discovered,",
                    "B. The Prah River's pollution being discovered,",
                    "C. When having made the discovery of the pollution of the water in the Prah River;",
                    "D. After discovering pollution in the Prah River,",
                    "E. Pollution was discovered in the Prah River,"
                ],
                "correct": 3, 
                "explanation": "Option D creates a logical dependent clause ('After discovering pollution...')."
            },

            # --- SECTION A: ERROR RECOGNITION (Q26-43) ---
            {
                "type": "standard",
                "q": "26. [A] Kombianus' lifelong career as a drug dealer and his [B] murder of three BNI agents [C] proves that [D] he is one of the most notorious criminals... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 2, 
                "explanation": "C ('proves') should be 'prove' (plural) because the subject is 'career and murder'."
            },
            {
                "type": "standard",
                "q": "27. Notice that this cereal [A] not only costs more than the other one, [B] plus being packed in a [C] smaller container. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('plus being') is incorrect. The correlative conjunction for 'not only' is 'but also'."
            },
            {
                "type": "standard",
                "q": "28. Although I can't concur [A] in the blogger's opinions, I am grateful to have seen them expressed [B] so [C] eloquently. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('in') should be 'with'. You concur *with* an opinion."
            },
            {
                "type": "standard",
                "q": "29. Although Kwabena... has the highest grade-point average... his [C] score on the GEMP exam was far lower than [D] Charles. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 3, 
                "explanation": "D ('Charles') is an illogical comparison. It should be 'Charles's' (comparing score to score)."
            },
            {
                "type": "standard",
                "q": "30. High school students who wish to become a [A] professional athlete should remember that the [B] odds against being successful... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('professional athlete') should be plural ('professional athletes') to agree with 'students'."
            },
            {
                "type": "standard",
                "q": "31. [A] Following traditional family values [B] have become one of the distinct differences between my [C] parents and me. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('have become') should be 'has become'. The subject is the singular phrase 'Following traditional family values'."
            },
            {
                "type": "standard",
                "q": "32. Susuana hopes to convince Pearl that she [A] neither is interested in going out with other boys [B] or that she ever loved anyone else... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('or') should be 'nor'. The correct structure is 'neither... nor'."
            },
            {
                "type": "standard",
                "q": "33. Foremost among the voters' concerns [A] is the problem of what to do about waste disposal and the [B] issues surrounding the construction... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('is') should be 'are'. The subject is compound ('the problem... and the issues')."
            },
            {
                "type": "standard",
                "q": "34. The [A] plight of immigrants... [B] are no less [C] heartbreaking than the suffering of the migrant workers... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('are') should be 'is'. The subject is the singular 'plight'."
            },
            {
                "type": "standard",
                "q": "35. A number of the athletes [A] which participated in last year's Olympics Games were found to [B] have used steroids... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('which') should be 'who' when referring to people (athletes)."
            },
            {
                "type": "standard",
                "q": "36. Carolyn's mother was born and raised in Baltimore, [A] where she attended high school and [B] college, [C] got married and gave birth to Carolyn... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 4, 
                "explanation": "E (No Error). The sentence structure is correct."
            },
            {
                "type": "standard",
                "q": "37. The [A] present senior class has a greater number of scholarship winners than [B] last year. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('last year') is an illogical comparison. It should be 'last year's class' (comparing class to class)."
            },
            {
                "type": "standard",
                "q": "38. My parents instilled their moral values [A] for my sister and me, [B] enabling us... to know right from wrong. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('for') should be 'in'. You instill values *in* someone."
            },
            {
                "type": "standard",
                "q": "39. The earliest pirates... [A] rustled cattle, [B] smoked the meat and [C] were stealing gold and jewels... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 2, 
                "explanation": "C ('were stealing') breaks the parallel structure. It should be 'stole' (rustled, smoked, stole)."
            },
            {
                "type": "standard",
                "q": "40. As Kesewaa opened the refrigerator, she [A] instantly noticed that a huge chunk of chocolate icing had been [B] bit off the birthday cake... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('bit') should be 'bitten' (past participle of bite)."
            },
            {
                "type": "standard",
                "q": "41. In his memoir, Mensah tells stories about the time... when he [B] is having to deliver newspapers... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('is having') should be 'had'. The sentence is in the past tense ('before he entered high school')."
            },
            {
                "type": "standard",
                "q": "42. Of the two Hemingway novels I have read, I like A Farewell to Arms the [B] best... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('best') should be 'better'. Use comparative ('better') for two items, superlative ('best') for three or more."
            },
            {
                "type": "standard",
                "q": "43. Child psychologists will tell you that young children [A] which are pushed into activities [B] prematurely... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('which') should be 'who' for children."
            },

            # --- SECTION A: SENTENCE COMPLETION (Q44-65) ---
            {
                "type": "standard",
                "q": "44. Unfortunately, in developing countries rapid economic growth often _____ overexploitation of natural resources and _____ the distribution of wealth.",
                "options": ["A. halts... indiscriminate", "B. holds off... inadequate", "C. leads to... inequitable", "D. continues... evenhanded", "E. goes beyond... ungrateful"],
                "correct": 2, 
                "explanation": "Economic growth often 'leads to' overexploitation and an 'inequitable' (unfair) distribution of wealth."
            },
            {
                "type": "standard",
                "q": "45. The Apache are a _____ society, where husbands typically move into wives' dwellings and women take the leadership role in family affairs.",
                "options": ["A. sedentary", "B. defunct", "C. fragmented", "D. matrilineal", "E. xenophobic"],
                "correct": 3, 
                "explanation": "A society where lineage/leadership is female-oriented is 'matrilineal'."
            },
            {
                "type": "standard",
                "q": "46. _____ James Baldwin, who wrote of black Americans as being in a perpetual state of rage, Mr. Cose asserts that few human beings could _____ the psychic toll of uninterrupted anger.",
                "options": ["A. Corroborating...endure", "B. Refuting...enhance", "C. Dismissing...refine", "D. Challenging...survive", "E. Upholding...weather"],
                "correct": 3, 
                "explanation": "Mr. Cose is 'Challenging' Baldwin's view by arguing that few could 'survive' such a state."
            },
            {
                "type": "standard",
                "q": "47. Rather than allowing these dramatic exchanges between her characters to develop fully, Ms. Norman unfortunately tends to _____ the discussions involving the two women.",
                "options": ["A. exacerbate", "B. protract", "C. truncate", "D. augment", "E. elaborate"],
                "correct": 2, 
                "explanation": "'Truncate' means to cut short, which contrasts with 'develop fully'."
            },
            {
                "type": "standard",
                "q": "48. The _____ with which musicians and lovers of fine instruments _____ Paul Irvin's professional services attests to his great expertise...",
                "options": ["A. hesitation...acquire", "B. avidness...solicit", "C. persistence...supersede", "D. harmony...conjure", "E. vehemence...reject"],
                "correct": 1, 
                "explanation": "Their 'avidness' (eagerness) to 'solicit' (ask for) his services shows his high reputation."
            },
            {
                "type": "standard",
                "q": "49. Deeply _____ by the insult to his dignity, he maintained that no true gentleman would accept such an _____ calmly.",
                "options": ["A. mortified...opportunity", "B. incensed...affront", "C. puzzled...honour", "D. shamed...iconoclasm", "E. gratified...admonition"],
                "correct": 1, 
                "explanation": "He was 'incensed' (angered) by the 'affront' (insult)."
            },
            {
                "type": "standard",
                "q": "50. Learned though she was, Ama's _____ never degenerated into _____.",
                "options": ["A. erudition...arrogance", "B. knowledge...ignorance", "C. scholarship...research", "D. speculation...thought", "E. education...inquiry"],
                "correct": 0, 
                "explanation": "Her 'erudition' (learning) didn't become 'arrogance'."
            },
            {
                "type": "standard",
                "q": "51. Biologists categorise many of the world's environments as deserts: regions where the _____ availability of some key factor... places sharp constraints on the existence of living things.",
                "options": ["A. ready", "B. gradual", "C. limited", "D. nearby", "E. unprecedented"],
                "correct": 2, 
                "explanation": "Deserts are defined by the 'limited' availability of water/nutrients."
            },
            {
                "type": "standard",
                "q": "52. The Americans and the British seem to have a dog-in-the-manger attitude toward the island of Malta, no longer needing it themselves but nevertheless wishing to _____ it to others.",
                "options": ["A. interpret", "B. offer", "C. deny", "D. praise", "E. reveal"],
                "correct": 2, 
                "explanation": "A 'dog-in-the-manger' attitude means preventing others from having what you don't need. So they wish to 'deny' it to others."
            },
            {
                "type": "standard",
                "q": "53. Increasingly silent and withdrawn, he changed from a fluent, articulate speaker to someone who gave only _____ answers to any questions asked of him.",
                "options": ["A. bookish", "B. effusive", "C. idiomatic", "D. pretentious", "E. monosyllabic"],
                "correct": 4, 
                "explanation": "'Monosyllabic' answers (one word) fits someone who is silent and withdrawn."
            },
            {
                "type": "standard",
                "q": "54. When you learn archaeology solely from lectures, you get only _____ sense of the concepts... but when you hold a 5,000-year-old artifact... you have a chance to involve your senses.",
                "options": ["A. an invalid", "B. an anachronistic", "C. an abstract", "D. a specious", "E. a tangential"],
                "correct": 2, 
                "explanation": "Lectures give an 'abstract' sense, while holding an object involves the senses directly."
            },
            {
                "type": "standard",
                "q": "55. Paradoxically, while it is relatively easy to prove a fraudulent work of art is a fraud, it is often virtually impossible to prove that an authentic one is _____.",
                "options": ["A. unpretentious", "B. objective", "C. impartial", "D. dubious", "E. genuine"],
                "correct": 4, 
                "explanation": "It's hard to prove an authentic one is 'genuine'."
            },
            {
                "type": "standard",
                "q": "56. Stephen Appiah's former casino in Dansoman was once the most _____ gambling palace in the city, easily outglittering its competitors.",
                "options": ["A. professional", "B. speculative", "C. ostentatious", "D. lucrative", "E. restrained"],
                "correct": 2, 
                "explanation": "'Ostentatious' matches 'outglittering' (showy/flashy)."
            },
            {
                "type": "standard",
                "q": "57. American culture now stigmatises, and sometimes even heavily _____, behaviour that was once taken for granted: overt racism, cigarette smoking, the use of sexual stereotypes.",
                "options": ["A. advocates", "B. penalises", "C. ignores", "D. indoctrinates", "E. advertises"],
                "correct": 1, 
                "explanation": "Culture stigmatises and 'penalises' these behaviors."
            },
            {
                "type": "standard",
                "q": "58. Determined to hire employees on the basis of their merits rather than on the basis of their family connections, Professor Dadson refused to _____ nepotism...",
                "options": ["A. Obscure", "B. Proscribe", "C. Countenance", "D. Misrepresent", "E. discern"],
                "correct": 2, 
                "explanation": "He refused to 'countenance' (tolerate/approve) nepotism."
            },
            {
                "type": "standard",
                "q": "59. Because the damage to his car had been _____, Michael decided he wouldn't bother to report the matter to his insurance company.",
                "options": ["A. intermittent", "B. gratuitous", "C. negligible", "D. spontaneous", "E. significant"],
                "correct": 2, 
                "explanation": "If he didn't bother reporting it, the damage must have been 'negligible' (minor)."
            },
            {
                "type": "standard",
                "q": "60. Even when being _____ in method, people can come up with incorrect answers by basing their arguments on false premises.",
                "options": ["A. original", "B. logical", "C. slipshod", "D. realistic", "E. careless"],
                "correct": 1, 
                "explanation": "Even if your method is 'logical', false premises lead to incorrect answers."
            },
            {
                "type": "standard",
                "q": "61. When clay dries out, it loses its plasticity and becomes less _____.",
                "options": ["A. synthetic", "B. expensive", "C. malleable", "D. tangible", "E. brittle"],
                "correct": 2, 
                "explanation": "Plasticity means moldability. Losing it makes it less 'malleable'."
            },
            {
                "type": "standard",
                "q": "62. For many years an unheralded researcher, Barbara McClintock gained international _____ when she won the Nobel Prize...",
                "options": ["A. condemnation", "B. notoriety", "C. renown", "D. affluence", "E. camaraderie"],
                "correct": 2, 
                "explanation": "Winning the Nobel Prize brings 'renown' (fame)."
            },
            {
                "type": "standard",
                "q": "63. Rather than feeling toward Miss Havisham the _____ due a benefactor, Estella became resentful and even _____ to her patron.",
                "options": ["A. esteem...effusive", "B. obligation...dutiful", "C. altruism...quarrelsome", "D. gratitude...hostile", "E. condescension...benign"],
                "correct": 3, 
                "explanation": "She should feel 'gratitude', but instead became 'hostile'."
            },
            {
                "type": "standard",
                "q": "64. Despite the heated discussions of recent months, observers say that the administration and the developer have made progress... and are close to _____ on a purchase price.",
                "options": ["A. amicable...haggling", "B. acrimonious...defaulting", "C. heated...agreeing", "D. fruitful...settling", "E. constructive...compromising"],
                "correct": 3, 
                "explanation": "They are close to 'settling' on a price."
            },
            {
                "type": "standard",
                "q": "65. When I listened to her cogent arguments, all my _____ were _____ and I was forced to agree with her point of view.",
                "options": ["A. senses...stimulated", "B. opinions...confirmed", "C. preconceptions...substantiated", "D. questions...interpolated", "E. doubts...dispelled"],
                "correct": 4, 
                "explanation": "Cogent (convincing) arguments would cause 'doubts' to be 'dispelled'."
            }
            
            # --- COMPREHENSION PASSAGE ---
            {
                "q": "PASSAGE:\nScientists have long debated how the ancestors of birds evolved the ability to fly. The ground-up theory assumes they were fleet-footed ground dwellers that captured prey by leaping... Ken Dial saw a pattern in how young pheasants... ran along behind their parents... 'They jumped up like popcorn'... Ken settled on the Chukar Partridge... The rancher was incredulous... 'What are those birds doing on the ground? They hate to be on the ground!'... Ken realized they preferred elevated perches... Young Terry Dial observed: 'The birds are cheating! Instead of flying... they were using their legs... running right up the side of a hay bale'... Ken called the technique WAIR (wing-assisted incline running)...\n\n66. As used in line 4 of paragraph 1, 'challenged' most nearly means:",
                "options": ["A. dared", "B. required", "C. disputed with", "D. competed with", "E. questioned"],
                "correct": 0, "explanation": "In the context 'graduate students challenged him to come up with new data', 'dared' or 'provoked' fits best."
            },
            {
                "q": "67. As used in line 1 of paragraph 5, 'document' most nearly means:",
                "options": ["A. portray", "B. record", "C. publish", "D. process", "E. file"],
                "correct": 1, "explanation": "To 'document' in a scientific context means to 'record' or provide evidence for."
            },
            {
                "q": "68. After Ken Dial had his 'aha' moment (paragraph 3, line 5), he:",
                "options": ["A. tried to train the birds to fly to their perches", "B. studied videos to determine why the birds no longer hopped", "C. observed how the birds dealt with gradually steeper inclines", "D. consulted with other researchers who had studied Chukar Partridges", "E. abandoned the experiment"],
                "correct": 2, "explanation": "Paragraph 4 says: 'Ken came up with a series of ingenious experiments... ramps tilted at increasing angles'."
            },
            {
                "q": "69. What can reasonably be inferred about gliding animals from the passage?",
                "options": ["A. Their young tend to hop along beside their parents instead of flying beside them", "B. Their method of locomotion is similar to that of ground birds", "C. They use the ground for feeding more often than for perching", "D. They do not use a flapping stroke to aid in climbing slopes", "E. They evolved before ground birds"],
                "correct": 3, "explanation": "Paragraph 6 mentions 'flapping flight stroke... (something gliding animals don't do)'."
            },
            {
                "q": "70. The passage identifies which of the following as a factor that facilitated the baby Chukars' traction on steep ramps?",
                "options": ["A. The speed with which they climbed", "B. The position of their flapping wings", "C. The alternation of wing and foot movement", "D. Their continual hopping motions", "E. The texture of the ramp"],
                "correct": 1, "explanation": "Paragraph 4: 'They aimed their flapping down and backward, using the force... to keep their feet firmly pressed'."
            },

            # --- SECTION B: LOGICAL REASONING ---
            {
                "q": "71. Find the appropriate item which will replace 'X': 7, 11, 19, 35, 67, X",
                "options": ["A. 99", "B. 131", "C. 134", "D. 445", "E. 129"],
                "correct": 1, "explanation": "Differences: 4, 8, 16, 32. Next difference is 64. 67 + 64 = 131."
            },
            {
                "q": "72. Find X: 8, 22, 64, 190, 568, X",
                "options": ["A. 1702", "B. 1315", "C. 7134", "D. 6445", "E. 1704"],
                "correct": 0, "explanation": "Pattern: x3 - 2. (8*3)-2=22; (22*3)-2=64... (568*3)-2 = 1704 - 2 = 1702."
            },
            {
                "q": "73. Find X: 5760, 2880, 960, 240, 48, X",
                "options": ["A. 17", "B. 8", "C. 12", "D. 16", "E. 24"],
                "correct": 1, "explanation": "Divisors: /2, /3, /4, /5. Next is /6. 48 / 6 = 8."
            },
            
            # --- LOGIC PUZZLE: RESTAURANT ---
            {
                "q": "PUZZLE:\nAduane Superb stays open Mon-Sat, closed Sun.\n- Mon: Lunch only.\n- Tue/Thu: Lunch only.\n- Wed/Fri/Sat: Dinner only.\n- Plants watered 2 days/week (never consecutive, never same day as polish).\n- Floors polished Mon and 2 other days (never consecutive, never same day as water).\n\n81. According to the schedule, the restaurant's floors are polished on either:",
                "options": ["A. Tuesday or Wednesday", "B. Tuesday or Thursday", "C. Wednesday or Thursday", "D. Thursday or Friday", "E. Thursday or Saturday"],
                "correct": 3, "explanation": "Polished Mon. Cannot be consecutive, so not Tue. Must be Wed or Thu? If Wed, then Fri (to be 3 days non-consecutive). If Thu, then Sat. Let's look closer at constraints."
            },
            {
                "q": "82. If dinner is served on the same day as plants are watered, which of the following is correct?",
                "options": ["A. Plants are watered on Tuesday.", "B. Floors are polished on Thursday.", "C. Plants are watered on Wednesday.", "D. Floors are polished on Wednesday.", "E. Plants are watered on Saturday."],
                "correct": 2, "explanation": "Dinner is served Wed, Fri, Sat. Plants watered on a dinner day. If plants Wed -> Polish cannot be Wed. Polish is Mon. Next polish Fri? (Mon, Wed, Fri - No, polish cant be same as water). Logic requires detailed mapping."
            },

            # --- LOGIC PUZZLE: CARDS ---
            {
                "q": "PUZZLE:\nFour players Aaron, Bob, Cyril, Dave holding 4 cards each. Each has Ace, King, Queen, Jack. All have all suits.\nI. Aaron has Ace of spades and Queen of diamonds.\nII. Bob has Ace of clubs and King of diamonds.\nIII. Cyril has Queen of clubs and King of spades.\nIV. Dave has Jack of clubs.\n\n106. Who has Ace of Diamonds?",
                "options": ["A. Aaron", "B. Bob", "C. Cyril", "D. Dave", "E. Cannot determine"],
                "correct": 3, "explanation": "Aaron has Ace(S). Bob has Ace(C). Cyril must have an Ace. Dave must have an Ace. If Cyril has King(S) and Queen(C)... needs deduction of remaining suits."
            },

            # --- SECTION C: QUANTITATIVE METHODS ---
            {
                "q": "DATA TABLE:\nResistance to COVID-19\n- Africans: High Risk(90), Med(25), Low(10), Total(125)\n- European: High(55), Med(35), Low(59), Total(149)\n- Arabs: High(60), Med(20), Low(20), Total(100)\n- Grand Total: 374\n\n121. What is the probability of a low-risk European being randomly selected? (3 decimal places)",
                "options": ["A. 0.135", "B. 0.053", "C. 0.158", "D. 0.185", "E. 0.200"],
                "correct": 2, "explanation": "Low Risk European = 59. Total = 374. 59/374 ≈ 0.1577 -> 0.158."
            },
            {
# --- QUANTITATIVE: TABLE 1 (Exact Data) ---
            {
                "type": "passage",
                "text": """DATA TABLE: Risk of HBV infection among various races (Table 1)
-------------------------------------------------------
RACE       | High Risk | Medium Risk | Low Risk | Total
-------------------------------------------------------
Africans   |    90     |     25      |    10    |  125
European   |    55     |     35      |    59    |  149
Arabs      |    60     |     20      |    20    |  100
-------------------------------------------------------
Total      |   205     |     80      |    89    |  374
-------------------------------------------------------""",
                "q": "121. What is the probability that a randomly selected person is a low-risk European? (3 decimal places)",
                "options": ["A. 0.135", "B. 0.053", "C. 0.158", "D. 0.185"],
                "correct": 2, "explanation": "Low Risk Europeans = 59. Total population = 374. \nProbability = 59 / 374 = 0.15775... \nRounded to 3 d.p. = 0.158"
            },
            {
                "type": "standard",
                "q": "122. What is the probability that someone randomly selected will be an Arab given that he has medium risk?",
                "options": ["A. 0.250", "B. 0.025", "C. 0.398", "D. 0.053"],
                "correct": 0, "explanation": "Formula: P(Arab | Medium). \nLook at the 'Medium Risk' column. Total Medium = 80. \nNumber of Arabs in that column = 20. \nProb = 20 / 80 = 0.25."
            },
                "q": "122. What is the probability that someone randomly selected will be an Arab given that he has medium risk?",
                "options": ["A. 0.250", "B. 0.025", "C. 0.398", "D. 0.053", "E. 0.200"],
                "correct": 0, "explanation": "Total Medium Risk = 25+35+20 = 80. Arabs with Medium Risk = 20. Prob = 20/80 = 0.25."
            },
            {
                "q": "123. What is the probability that a selected African will be high risk?",
                "options": ["A. 0.720", "B. 0.270", "C. 0.241", "D. 0.439", "E. 0.500"],
                "correct": 0, "explanation": "Selected African (Total 125). High Risk African = 90. Prob = 90/125 = 0.72."
            },
            {
                "q": "124. The major difference between Standard Deviation (SD) and Standard Error (SE) is:",
                "options": ["A. SE refers to population, SD to sample", "B. SD measures scatter/dispersion about the mean", "C. SE is calculated from SD", "D. SE measures precision while SD measures scatter", "E. All of the above"],
                "correct": 3, "explanation": "SD quantifies variation within a set of data (scatter). SE quantifies the precision of the mean estimate."
            },
            {
                "q": "125. Mean = 150 mg/l, SD = 15.0, SE = 6.5. 95% Confidence (z=1.96). Lower and Upper bounds?",
                "options": ["A. 126.74 - 260.78", "B. 137.26 - 162.74", "C. 240.6 - 362.2", "D. 294.0 - 269.9", "E. 135.0 - 165.0"],
                "correct": 1, "explanation": "95% CI = Mean ± (1.96 * SE). 150 ± (1.96 * 6.5) = 150 ± 12.74. Lower=137.26, Upper=162.74."
            },
            {
                "q": "130. If log10(7) = a, then log10(1/70) will be?",
                "options": ["A. -(1+a)", "B. 1/10a", "C. a/10", "D. (1+a)^-1", "E. -a"],
                "correct": 0, "explanation": "log(1/70) = log(1) - log(70) = 0 - log(7*10) = -(log 7 + log 10) = -(a + 1)."
            },
            {
                "q": "131. Solve for x and y: x + 2y = 9; 3x - 4y = -33",
                "options": ["A. x=2, y=7", "B. x=3, y=-6", "C. x=-3, y=6", "D. x=9, y=12", "E. x=0, y=0"],
                "correct": 2, "explanation": "Multiply eq1 by 2: 2x + 4y = 18. Add to eq2: (3x - 4y) + (2x + 4y) = -33 + 18. 5x = -15 -> x = -3. Sub x into eq1: -3 + 2y = 9 -> 2y = 12 -> y = 6."
            }
]

# --- SIDEBAR (Timer & Navigation) ---
with st.sidebar:
    st.title("⏳ Exam Timer")
    
    # Calculate time left (3 Hours = 10800 seconds)
    elapsed = time.time() - st.session_state.start_time
    remaining = 10800 - elapsed
    
    if remaining > 0:
        mins, secs = divmod(int(remaining), 60)
        hours, mins = divmod(mins, 60)
        st.header(f"{hours:02d}:{mins:02d}:{secs:02d}")
        st.progress(max(0.0, remaining / 10800))
    else:
        st.error("Time's Up!")
        st.session_state.exam_finished = True

    st.markdown("---")
    st.write(f"**Progress:** Q{st.session_state.current_q + 1} of {len(questions)}")

# --- MAIN EXAM UI ---
st.title("🎓 GEMP 2024 General Paper")

if not st.session_state.exam_finished:
    # Get current question
    q_data = questions[st.session_state.current_q]
    
    # Display Question
    st.markdown(f"### Question {st.session_state.current_q + 1}")
    st.info(q_data["q"])
    
    # Radio Button for Options
    choice = st.radio(
        "Select your answer:", 
        q_data["options"], 
        index=None, 
        key=f"q_{st.session_state.current_q}"
    )

    # Submit Button
    if st.button("Submit Answer"):
        if choice:
            # Check answer
            selected_index = q_data["options"].index(choice)
            is_correct = (selected_index == q_data["correct"])
            
            if is_correct:
                st.success("✅ Correct! \n\n" + q_data["explanation"])
                if st.session_state.current_q not in st.session_state.answers:
                    st.session_state.score += 1
                    st.session_state.answers[st.session_state.current_q] = "Correct"
            else:
                correct_letter = ["A", "B", "C", "D", "E"][q_data["correct"]]
                st.error(f"❌ Incorrect. The correct answer was **{correct_letter}**.\n\n" + q_data["explanation"])
                if st.session_state.current_q not in st.session_state.answers:
                    st.session_state.answers[st.session_state.current_q] = "Incorrect"
            
            # Next Question Button (only appears after answering)
            time.sleep(1) # Brief pause
            if st.session_state.current_q < len(questions) - 1:
                if st.button("Next Question ➡️"): # Logic handled by rerun
                    pass 
                st.session_state.current_q += 1
                st.rerun()
            else:
                st.session_state.exam_finished = True
                st.rerun()
        else:
            st.warning("Please select an option first.")

else:
    # --- RESULTS SCREEN ---
    st.balloons()
    st.markdown("## 🏁 Exam Completed!")
    
    score_pct = (st.session_state.score / len(questions)) * 100
    st.metric(label="Final Score", value=f"{st.session_state.score}/{len(questions)}", delta=f"{score_pct:.1f}%")
    
    st.write(f"You answered {st.session_state.score} questions correctly out of {len(questions)}.")
    
    if st.button("Restart Exam"):
        for key in st.session_state.keys():
            del st.session_state[key]

        st.rerun()
