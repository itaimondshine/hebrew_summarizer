import re


output = """
[{'summary_text': 'העיתונאי דודו טופז, שכתב את המשפט מנאום הצחצחים של מנחם בגין, היה היחיד שפירסם את הדברים לאחר העצרת של הליכוד'}]
40
Your max_length is set to 3000, but your input_length is only 1548. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=774)
[{'summary_text': '"מעריב" ממשיך לקדם את הבחירות | "ידיעות אחרונות" ממשיך לקדם את הבחירות | "גלובס" ממשיך לקדם את אי.די.בי'}]
41
[{'summary_text': 'האם עיתונאי יכול להשמיע ביקורת פומבית על מקום העבודה שלו, לחשוף משהו מהקרביים של המערכת, אינה עולה בפעם הראשונה?'}]
35
Your max_length is set to 3000, but your input_length is only 2227. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1113)
[{'summary_text': '"ידיעות אחרונות" ממשיך לקדם את המחאה החברתית | "הארץ" ממשיך לקדם את המחאה החברתית | "ישראל היום" לא נחים על זרי הדפנה'}]
43
Your max_length is set to 3000, but your input_length is only 674. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=337)
[{'summary_text': '"ידיעות אחרונות" מתנצל בפני טוביה סוקולסקי | "ישראל היום" מגיש תסריט פסימי באשר לסיכויי ראש הממשלה לחמוק מכתב אישום | ומרדכי גילת מגיש טור דעה בוטה נגד עמיתיו העיתונאים'}]
60
Your max_length is set to 3000, but your input_length is only 2675. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1337)
[{'summary_text': 'פורום הארגונים למען הפסיכולוגיה הציבורית מציע קווים מנחים לגבי קיום ראיונות עם מי ששרדו את התופת • "הקשבה לראיון המכיל תיאורי זוועה וחוסר אונים, עלול לפגוע בחוסנם של המראיין ושל המאזינים, ולהביא לפיתוחה של טראומטיזציה משנית מצדם"'}]
82
Your max_length is set to 3000, but your input_length is only 1262. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=631)
[{'summary_text': 'ערוץ 4 הבריטי, שחגג 30 שנים להקמתו, התבקש להיות הילד השובב של השידור הציבורי, שיוכיח שאפשר לייצר איכות, אבל גם חדשנות ומקוריות. וגם להרגיז, לבעוט מחוץ לקונסנזוס'}]
60
[{'summary_text': 'בית-המשפט העליון הפך בימים אלה פסיקה של הילה גרסטל מבית-המשפט המחוזי בתל-אביב'}]
30
[{'summary_text': '"ישראל היום" ממשיך לדווח על שיחות הגרעין בלוזאן | "ידיעות אחרונות" ממשיך לדווח על רפורמה בבנקים | שי אספריל ממשיך לדווח על ניקוי שמי'}]
50
Your max_length is set to 3000, but your input_length is only 2777. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1388)
[{'summary_text': '"מעריב" מעניק ציטוט של בנימין בן-אליעזר | "ידיעות אחרונות" מעניק ציונים נמוכים במיוחד במקצועות הירוקים | ו"ישראל היום" מעניק ציונים נמוכים במיוחד במקצועות הירוקים'}]
54
Your max_length is set to 3000, but your input_length is only 1391. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=695)
[{'summary_text': '"ידיעות אחרונות" ממשיך לקדם את הכלכלה | "ישראל היום" ממשיך לקדם את תוכנית אובמה | "ישראל היום" ממשיך לקדם את תוכנית אדלסון'}]
41
Your max_length is set to 3000, but your input_length is only 1442. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=721)
[{'summary_text': 'הביקורת על צריבת צארנייב בתודעה הקולקטיבית כ"אובייקט יפה" מבטאת דרישה להגמוניה ולבלעדיות על השיח ועל ייצוגו החזותי'}]
44
Your max_length is set to 3000, but your input_length is only 354. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=177)
[{'summary_text': 'במשרד החקלאות טוענים כי העבירו טיוטת תקנות בנושא גרירת רשתות מכמורת בקרבת תשתיות גז ונפט לעיון משרד האנרגיה. במשרד טוענים כי "סוכם על הנעת מהלך תיקון הפקודה והתקנות בהיבט איכון הספינות, כבר בשבועות הקרובים"'}]
75
[{'summary_text': '"הפוליגרף": חיים זיסוביץ על סיקור עסקת השבויים, יוסי תמם על שאלות אישיות ורגישות, מנשה סמירה על הרשות השנייה, ו"ידיעות אחרונות" על קמפיין הדמעות'}]
56
Your max_length is set to 3000, but your input_length is only 2348. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1174)
[{'summary_text': '"הארץ" מרקחה את נתניהו | "ישראל היום" ממשיך לנסות למנוע פיוס | "הארץ" ממשיך לנסות למנוע את הירי מעזה'}]
39
Your max_length is set to 3000, but your input_length is only 909. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=454)
[{'summary_text': 'החקירה התנהלה בעצלתיים, והתבססה בעיקר על אמצעים טכנולוגיים. בימים שבהם איתרה המשטרה את החשודים בביצוע הממשי של ההתקפה על מרגלית, שמו של דודו טופז היה אחד מבין שמות רבים של אנשים שייתכן וביקשו להזמין תקיפה שכזו, אולם בדרכה האטית של המשטרה תיכננו החוקרים לבצע עוד מהלכי חקירה ולנסות לאתר את המזמינים'}]
98
Your max_length is set to 3000, but your input_length is only 751. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=375)
[{'summary_text': 'הבמאי ניר טויב היה מאותם יחידי סגולה שכשסרטו היה מוכן, החל מבחינתם המאבק האמיתי – על הזכות לשדרו'}]
35
Your max_length is set to 3000, but your input_length is only 1942. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=971)
[{'summary_text': 'איל ההון והבעלים של "ישראל היום" שלדון אדלסון: "הקמתי את העיתון כדי לתת לישראל, לישראלים, חדשות ודעות מנקודת מבט הוגנת ומאוזנת"'}]
47
Your max_length is set to 3000, but your input_length is only 1174. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=587)
[{'summary_text': 'הפייסבוק הפיקטיבי של הכדורגל ממשיך למלא את שגרת יומם של צרכני תקשורת הספורט | העיתונות האזרחית ממשיך למלא את שגרת יומם של צרכני תקשורת הספורט | וכולם ממשיכים למלא את שגרת יומם'}]
60
[{'summary_text': 'הבחירה שלכן בזנות אינה סיבה חזקה מספיק כדי לפטור דווקא את תופעת הזנות מהניתוב הזה, ולעצור את קידום החוק להפללת לקוחות בגלל ההתנגדות שלכן'}]
44
[{'summary_text': 'העיתונים מדווחים על חגיגה של שיא | "דה-מרקר" ממשיך לחגיגה | ו"מעריב" ממשיך לחגיגה'}]
37
Your max_length is set to 3000, but your input_length is only 2193. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1096)
[{'summary_text': '"ידיעות אחרונות" מעניק תקווה ליועץ משפטי לעומתי לנתניהו | "ישראל היום" מעניק תקווה להליכוד | "דה-מרקר" מסביר את האופן שבו מתנהלת המשטרה'}]
50
Your max_length is set to 3000, but your input_length is only 568. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=284)
[{'summary_text': '"ישראל היום" מציג את עמדת ארה"ב | "ידיעות אחרונות" מציג את עמדת משרד החינוך | "כלכליסט" מציג את תוכנית משרד החינוך'}]
40
[{'summary_text': 'פרוייקט 100 ימים של שקיפות פנה ליאיר לפיד ולשרי יש עתיד המפוטרים וכן לציפי לבני כדי לבדוק אם יהיו מוכנים להחזיר את כספי הציבור. לכתבה בצינור לילה'}]
51
Your max_length is set to 3000, but your input_length is only 1157. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=578)
[{'summary_text': 'העיתונים מדווחים על יום-האדמה | "ידיעות אחרונות" ו"מקור ראשון" מדווחים על גדר | "ישראל היום" ממשיך לנסות לנגח את נתניהו'}]
44
[{'summary_text': 'התיקונים של "התיקונים" 2010: מה קורה במונדיאל, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה, מה קורה בעזה'}]
1084
[{'summary_text': '"ידיעות אחרונות" ממשיך להדיר נשים | "מעריב" ממשיך להדיר נשים | "דה-מרקר" ממשיך להדיר את נוחי דנקנר'}]
39
Your max_length is set to 3000, but your input_length is only 2516. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1258)
[{'summary_text': 'העיתונים מדווחים על מלחמה בעזה | העיתונים מדווחים על מלחמה בכלל | ו"ידיעות אחרונות" מדווח על מלחמה בעזה'}]
38
Your max_length is set to 3000, but your input_length is only 675. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=337)
[{'summary_text': 'העיתונות המודפסת מתמקדת בסיקור הבחירות לנשיאות ארה"ב | ברם עמנואל מתעלם מ"מעריב" | רון מיברג כותב על עתיד העולם'}]
47
Your max_length is set to 3000, but your input_length is only 2010. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1005)
[{'summary_text': 'ארגון העיתונאים והעיתונאית הגיש התנגדות לתזכיר החוק המעניק לשב"כ הרשאות נוספות לריגול אחר אזרחים ישראלים'}]
34
[{'summary_text': 'הגזבר הקודם של ועד עפולה-נצרת פרסם מכתב לעובדי התחנות בו הוא טען כי עקב חילוקי דעות בין ראשי הוועד של תחנות עפולה-נצרת לבין ראשי הוועד הארצי, עלה צורך בעיניו לפצל את הוועדים. "אתה לא חושב פעמיים על כך שאנשים הקדישו שעות ושנים מזמנם כדי לסייע לעובדים, לפני שאתה פועל כדי לבייש אותם ולהטיל בהם דופי"'}]
105
[{'summary_text': 'החשבון הטוויטר של "נועה מלמד" נמחק מ-2013, והפעם מבלי להזכיר שמות. מה הקשר בין מין לתקשורת?'}]
40
Your max_length is set to 3000, but your input_length is only 2249. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1124)
[{'summary_text': 'העיתונים מדווחים על שריפת הענק בכרמל | "ידיעות אחרונות" ממשיך לנסות לקדם את המדיניות הכלכלית | יואב צור ממשיך לנסות לקדם את המדיניות הכלכלית'}]
49
Your max_length is set to 3000, but your input_length is only 887. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=443)
[{'summary_text': 'העיתונים מתכוננים לבחירות שופטים | "ישראל היום" ממשיך לנסות למנוע פוליטיזציה | ורוני שקד ממשיך לנסות למנוע את השתילתו'}]
41
Your max_length is set to 3000, but your input_length is only 1044. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=522)
[{'summary_text': 'לבד מן התכיפות היומיומית של הידיעות שיש לטפל בהן באזור זה, הקושי העיקרי העומד בפני כתב זר בישראל ובשטחים הפלסטיניים הינו במיון הידיעות והמסרים המגיעים אליו'}]
47
Your max_length is set to 3000, but your input_length is only 817. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=408)
[{'summary_text': 'ישעיהו ד, רופא בכיר בכפר גלעדי, כתב על התנהלות טרומפלדור בכפר גלעדי, וכתב על מצבו של טרומפלדור ומותו'}]
41
Your max_length is set to 3000, but your input_length is only 1195. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=597)
[{'summary_text': 'יותר ויותר נראית העיתונות הישראלית כמי שעסוקה במסעות פרסום ויחסי-ציבור במקום למלא את תפקידה כמדווחת חסרת פניות על המתרחש'}]
41
Your max_length is set to 3000, but your input_length is only 1914. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=957)
[{'summary_text': 'מיזם סמלי יכול לשפר את המצב הקיים ולעזור לחברות וחברי הכנסת לקדם שוויון הזדמנויות. בעיה: "הח"כים לא יסכימו - הם דואגים רק לעצמם" • פתרון: להיות ח"כ זה תפקיד קשה ותובעני. חברות וחברי כנסת חדשים נאלצים לוותר על עבודתם ולהיכנס לתפקיד חדש ומאתגר, לפעמים מתגמל פחות ומלא בביקורת ציבורית קשוחה - לעיתים מעליבה ומאיימת. בסוף, רובם לא מושחתים. ההיפך. רובם אכפתי מטבעם ורוצים לעשות טוב. המערכת לעומת זאת, מאפשרת להם לפעול בחוסר שקיפות ולקדם בקלות רבה את מה שחשוב להם ולמקורביהם. לכן התכנית שלנו מתאימה בול: הרצון לעזור לאזרחיות ואזרחי ישראל - קיים'}]
186
Your max_length is set to 3000, but your input_length is only 2528. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1264)
[{'summary_text': 'העיתונים האמריקאיים מפרסמים פרס פולק לעיתונות, אבל לא רק על סיקור הירואי, אלא גם על סיקור הצבא והמלחמה'}]
34
Your max_length is set to 3000, but your input_length is only 2532. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1266)
[{'summary_text': '"הארץ" שוב מכר את שערו למרבה במחיר | "ידיעות אחרונות" ו"ישראל היום" שותים מים | ארי שמאי מבקר אצל זונות'}]
39
Your max_length is set to 3000, but your input_length is only 1194. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=597)
[{'summary_text': 'העיתונות הישראלית מתמסרת בלא ניד עפעף. למה? כי זה כל-כך יותר נוח מהפיגועים הקטנים והשגרתיים שלנו, וכאן יש סיכוי לתוצאה ברורה וחד-משמעית יותר מאשר בסכסוך המתמשך וחסר התוחלת בבית'}]
66
Your max_length is set to 3000, but your input_length is only 975. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=487)
[{'summary_text': 'הפעם הראשונה שהוועדה מוזכרת היא בספר האזרחות האחרון. הפסקה מתוך הספר מולכם: אפילו השתמשו בנוסח שחזרנו עליו בשנים האחרונות שוב ושוב: שהוועדה חורצת את גורל החוקים. כאמור, הוועדה לא מופיעה בהליך החקיקה בכלל בהמשך הספר. אבל גם זו תחילתה של התעוררות'}]
78
Your max_length is set to 3000, but your input_length is only 2958. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1479)
[{'summary_text': '״תמיכה שוטפת בילדים נזקקים בפנימיות״ הוא סעיף חשוב במיוחד בתקציב משרד הרווחה - והוא אכן תופס מקום משמעותי • גורם בכיר במשרד: מדובר בסוד גלוי במשרד וכי הסעיף הוא למעשה תולדה של הסכמים קואליציוניים, אשר גוזרים בשורה התחתונה כסף משמעותי מתקציב התמיכות למטרות שנדמות פוליטיות'}]
83
Your max_length is set to 3000, but your input_length is only 2822. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1411)
[{'summary_text': 'העיתונים מדווחים על תינוקת התורמת | "מעריב" מעניק שער אנונימי | ו"ידיעות אחרונות" מעניק שער אנונימי'}]
38
Your max_length is set to 3000, but your input_length is only 556. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=278)
[{'summary_text': 'התקשורת הרוסית אמרה "נייט" גדול ומזלזל לתוכנית ההתנתקות. העיתונאים הרוסים לא אוהבים את התוכנית של שרון, אבל לא ממש מצליחים לפענח את ההיגיון שלה'}]
48
Your max_length is set to 3000, but your input_length is only 248. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=124)
[{'summary_text': 'הבחירות 2019: מה קרה עם התקציבים? מה קרה עם התקציבים? מה קרה עם התקציבים? ומה קרה עם הבחירות?'}]
40
[{'summary_text': 'זה תקופה ארוכה שהתקשורת הישראלית משתנה. גופים חדשים רבים התווספו לתחום התקשורתי, שהלך והתמסחר. יחד עם ריבוי הגופים – רבו גם האינטרסים'}]
42
[{'summary_text': 'העיתונים מדווחים על מחיר השחרור של גלעד שליט | "מעריב" ממשיך לנסות לטפל בפוליטיקאים | ו"גלריה" של "הארץ" מעניק הצצה נדירה לאלבום התמונות האישי שלו'}]
55
Your max_length is set to 3000, but your input_length is only 1430. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=715)
[{'summary_text': 'העיתונים מדווחים על פרישה מפתיעה של נגיד בנק ישראל | "ישראל היום" ממשיך להנאה | "ידיעות אחרונות" ממשיך להנאה'}]
39
[{'summary_text': 'השרים יואב גלנט, יפעת שאשא-ביטון, יצחק וקנין, וסגן השר להגנת הסביבה לשעבר, ירון מזוז עדיין לא הגישו את הצהרות ההון שלהם. השרים עדיין לא הגישו את הצהרות ההון שלהם, ולמה הם לא מגישים אותן בזמן?'}]
73
Your max_length is set to 3000, but your input_length is only 1336. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=668)
[{'summary_text': 'העיתונים מדווחים על חילוקי הדעות בין נתניהו לארדן | "ידיעות אחרונות" ממשיך להגיש לקוראים סיקור מתמשך של סכסוך עבודה | "ישראל היום" ממשיך לקדם את הסכם איראן'}]
53
Your max_length is set to 3000, but your input_length is only 2222. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1111)
[{'summary_text': 'התקשורת אינה אמורה לשקול מראש את האינטרסים המנוגדים, של פרטיות החשוד ושל שמו הטוב. היא כן אמורה לדווח על תלונה ועל מעצרו של אדם כאשר יש בכך עניין ציבורי'}]
45
Your max_length is set to 3000, but your input_length is only 1485. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=742)
[{'summary_text': 'העיתונים מדווחים על הבחירות לנשיאות ארה"ב | "הארץ" ממשיך לספק לקוראיו מידע ודעות | ו"ידיעות אחרונות" ממשיך לספק לקוראיו מידע ודעות'}]
50
Your max_length is set to 3000, but your input_length is only 892. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=446)
[{'summary_text': 'מחקר חדש של ד"ר נורית גוטמן ופרופ יחיאל קלר מלמד כי קמפיינים מקדמים את תחושת האיום והפחדה בדרכים אינם יעילים יותר מקמפיינים המציגים מידע והמלצות רלבנטיות ומעודדים בקרב הציבור ערכים ונורמות חברתיות ראויים'}]
69
[{'summary_text': 'עורך וכתב הטכנולוגיה של "ישראל היום" אילן גטניו מקדם את תחום הטכנולוגיה בעיתונו, אך לא מקדם את ענייניו'}]
36
Your max_length is set to 3000, but your input_length is only 1967. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=983)
[{'summary_text': 'העיתונים מדווחים על כישלון מבצעי של מחמוד מבחוח | "הארץ" מצטט את הרב מוטי אלון | ו"מעריב" מציע עדות עצובה למצבו הרעוע'}]
49
[{'summary_text': '"היהודים באים" היתה תוכנית הבידור החדשה של ערוץ 1, שהייתה אמורה להיות תחילה לערוץ 10. האם היא היתה א-פוליטית?'}]
39
Your max_length is set to 3000, but your input_length is only 1838. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=919)
[{'summary_text': '"ידיעות אחרונות" מקדיש את 13 העמודים הראשונים לסיכום מפורט של המעשה הפלילי ונסיבות פענוחו | "מעריב" ממשיך לקדם את דמותו של שר האוצר | ו"ישראל היום" ממשיך לקדם את תקציב התקציב'}]
64
Your max_length is set to 3000, but your input_length is only 975. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=487)
[{'summary_text': 'אמיר תיבון על הציר שבין הסיפורים האנושיים לשאלות הנוקבות והעדכונים • ראיון עם עיתונאים ערבים-ישראלים על המלחמה • שיחה עם עיתונאים ערבים-ישראלים על המלחמה'}]
51
Your max_length is set to 3000, but your input_length is only 2983. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1491)
[{'summary_text': 'הפוליטיקה חרגה מזמן מגבולות הפעילות הממסדית המוכרת והמקובלת. שדה הפעילות השתנה, ואיתו גם חוקי המשחק והכללים'}]
38
[{'summary_text': 'העיתונים מדווחים על מבוכות בצה"ל | "מעריב" מדווח על כך שהקצין נגנבו פרטי כרטיס האשראי | ו"הארץ" מציג חוש הומור'}]
44
Your max_length is set to 3000, but your input_length is only 2794. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1397)
[{'summary_text': 'ביום שישי הראשון של שנת 2002, כאשר פתח פרופ גד שני מאוניברסיטת בן-גוריון שבנגב את מוסף "7 ימים" של "ידיעות אחרונות", ציפתה לו הפתעה מצערת'}]
53
[{'summary_text': 'בדיקות פנימיות ברשות השידור מלמדים עד כמה הרשות זקוקה לשינוי מהותי בעבודתה מול הספקים, ובכך היא זקוקה לשינוי מהותי בתקציבים'}]
43
[{'summary_text': '"ידיעות אחרונות" ו"הארץ" מדווחים על מהלך פוליטי דרמטי | "ישראל היום" ממשיך לחזור לשגרה | "מעריב" מציג סדר יום עצמאי'}]
44
[{'summary_text': '"ישראל היום" ו"ידיעות אחרונות" ממשיכים לחשוף שקר מופרך | ניר ברקת ממשיך לחשוף את מדיניותו | "הארץ" ממשיך לנסות לקדם את הסכם הוויתורים עם הטייקונים'}]
56
[{'summary_text': 'העיתונים הכלכליים ניסו לפזר עבורם את הערפל הפיננסי, אבל הצלחתם היתה חלקית. בכלי התקשורת האחרים, ובכלל זה במדוריהם הכלכליים, בחרו שלא להיכנס לעובי הקורה'}]
51
Your max_length is set to 3000, but your input_length is only 2537. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1268)
[{'summary_text': 'אילן שילוח, בעל הון שמתפרנס מהשקעות, העיד אתמול בבית-המשפט המחוזי בירושלים על הקשר עם נתניהו • השופטים הפגינו אגרסיביות, אך לא הצליחו למנוע את הדיון בתיק 4000 • אייל חיימובסקי, מנהל לשכת ראש הממשלה בשנים 2012–2014, העיד על הקשר האישי עם המיליארדר ארנון מילצן • השופטים הפגינו אגרסיביות, אך לא הצליחו לנטוש אותו'}]
121
Your max_length is set to 3000, but your input_length is only 495. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=247)
[{'summary_text': 'העיתונים מדווחים על חילופי השבויים | "ידיעות אחרונות" ממשיך לפוטו-זורנליזם | ומישל קרמרמן מראיינת ל"ממון"'}]
43
Your max_length is set to 3000, but your input_length is only 2814. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1407)
[{'summary_text': 'מדור חופש המידע של "הגנזך", מדור חופש המידע של "העין השביעית" בשיתוף "הצלחה", מוצגים מסמכים על עמותת יתדות'}]
38
[{'summary_text': 'לפובליציסטיקה בעיתונות הישראלית יש כלים לשוניים ופולמיים מיוחדים לטיפול בדתיים. במיוחד אמורים הדברים בעיתונות הליברלית והאיכותית'}]
37
Your max_length is set to 3000, but your input_length is only 348. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=174)
[{'summary_text': 'התאבדותו של יצחק הרשקוביץ ז"ל, והקשר – העולה ממכתב ההתאבדות – בינה לבין שידור כתבת התחקיר "תיק מע"צ" בערוץ 2, עלולים ליצור עכבות שחובה להשתחרר מהן אם רוצים לבחון את אותה כתבה באופן ענייני ומפוכח'}]
72
[{'summary_text': 'מיכל בירן, ח"כ ממפלגת העבודה, אישרה את הפרטים מפרופיל ההיכרויות שלה באתר "גלובס", אולם התגובות לא נמחקו'}]
38
Your max_length is set to 3000, but your input_length is only 2652. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1326)
[{'summary_text': '"ישראל היום" מפגין שער לא פטריוטי בעליל | "מעריב" מפגין שער לא פטריוטי בעליל | יאיר לפיד ממשיך להעמיד פנים שלא אכפת לו'}]
44
[{'summary_text': 'התביעה נגד תומס דרייק: הכתבת סיובאן גורמן סירבה להגיב על העמדתו לדין. העיתונים האמריקאיים מנסים להטיל אימה על עובדי מדינה שיש להם מידע שהם סבורים שחשוב לשתף בו את הציבור'}]
58
Your max_length is set to 3000, but your input_length is only 1138. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=569)
[{'summary_text': 'העיתונות הישראלית מנסה לפענח את מראית העין של ניקור העיניים, אבל לא את העיניים המנוקרות'}]
29
Your max_length is set to 3000, but your input_length is only 481. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=240)
[{'summary_text': 'המתקפה של ניקי פינק על "וראייטי" חשפה בעיקר את החולשות של המדיה הישנה מול המדיה החדשה'}]
29
Your max_length is set to 3000, but your input_length is only 2123. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1061)
[{'summary_text': 'חברת תכלת הודיעה כי אינה מוכנה להמשיך ולממן את שכר עובדי החברות שהוציאו לאור את "מעריב" ו"מקור ראשון"'}]
34
Your max_length is set to 3000, but your input_length is only 1825. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=912)
[{'summary_text': 'הלוביסט עומר כרמי, ששכר לאחרונה שירותי לובינג בכנסת, קיבל את זכות הדיבור • "שקוף" בחר לשפוך אור על שבעה, בהם התאחדות חברות לביטוח חיים, התאחדות קבלני כוח אדם המעסיקים עובדים זרים והחברה לפיתוח הגליל • העיתוי הרגיש עשוי לתת לנו אינדיקציה מסוימת'}]
82
[{'summary_text': 'הקפיטליזם חזק יותר מהאנשים שמסמלים אותו. יש רק כוח אחד שיכול לרסנו – הציבור'}]
25
[{'summary_text': '"מעריב" ממשיך לספק סיקור נרחב של האירועים הטרגיים בנגב | "ידיעות אחרונות" ממשיך לסקר את המחאה החברתית | בן כספית ממשיך לנסות להגן על אהוד ברק'}]
53
[{'summary_text': 'עובדי חברת החדשות של ערוץ 10 מתכוננים ליום חמישי להפגנה מול שר האוצר, ושר התקשורת. העובדים מתכוננים ליום חמישי להציל את הערוץ, אך המצב לא מאפשר להם להמשיך להתפרנס'}]
56
Your max_length is set to 3000, but your input_length is only 606. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=303)
[{'summary_text': 'ה"ניו-יורק טיימס" מציג את הצל האפל של אימפריית העיתונות הבריטית שלו, שמתנהלת במקביל משני עברי האוקיאנוס'}]
41
Your max_length is set to 3000, but your input_length is only 911. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=455)
[{'summary_text': 'העיתונאים הזרים חזרו לשדר מדמשק בימים האחרונים, תחת פיקוחה ההדוק של הממשלה הסורית. העיתונאים הזרים: "אנחנו נמצאים בסוריה כעת משום שנתנו לנו ויזה"'}]
48
Your max_length is set to 3000, but your input_length is only 1309. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=654)
[{'summary_text': 'שרון גל, שדר טלוויזיה ידוע, הודה בראיונות עיתונאיים, אך אישר שהתייחס לכפופים אליו באופן בוטה. המשטרה הגיעה למסקנה שמחוסר ראיות היא אינה מעמידה אותו לדין'}]
49
Your max_length is set to 3000, but your input_length is only 1126. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=563)
[{'summary_text': 'חברת הכנסת ענבר בזק שלום, מה שלומך? ראיתי שהצטלמת עם ספרה של דפנה ליאל ופרסמת אותו בטוויטר. יצא לך לקרוא אותו? "עוד לא. הייתה לי יומולדת לפני שבוע והבנות קנו לי מתנה, עוד לא יצא לי לקרוא. אני עוקבת אחרי הפודקאסט ושומעת כל בוקר, כל פעם באה ומספרת לצוות שלי תקשיבו לזה ותקשיבו לזה, אז הם עשו לי הפתעה וקנו אותו". אני מבינה שרצית לפרגן לה. "כן. נתתי לה לחתום לי עם הקדשה". אני מתקשרת כי הסתכלתי על זה ולי זה נראה כמו סוג של פרסומת, משהו שבעבר ועדת האתיקה אסרה על חברי כנסת לעשות. "למה זה פרסום אם היא כותבת על פוליטיקה?"'}]
184
[{'summary_text': 'הלך הרוח ההומופובי של הקהילה חושף את כוחה ההרסני של ההומופוביה. האם הלך רוח ההומופובי של הקהילה חושף את כוחה ההרסני של ההומופוביה?'}]
53
Your max_length is set to 3000, but your input_length is only 1192. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=596)
[{'summary_text': 'העיתונים מדווחים על פצצת מרגמה | "ישראל היום" ו"ידיעות אחרונות" מדווחים על פצצת מרגמה | "דה-מרקר" ו"כלכליסט" מדווחים על שיעור הריבית'}]
56
Your max_length is set to 3000, but your input_length is only 642. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=321)
[{'summary_text': 'כיל: המכון הישראלי לדמוקרטיה ביטל את השתתפותו של הסמנכ"ל הבכיר בפאנל יזמי אקלים, למרות מאמציו • בכיל: "התקפה האישית היא מכוערת ואינה מכבדת את תומכי שקוף"'}]
64
Your max_length is set to 3000, but your input_length is only 620. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=310)
[{'summary_text': 'מגישי התוכנית "המלה האחרונה" בגל"צ, המתפקדים בתוכנית גם כפובליציסטים, גם כבדרנים וגם כעיתונאים מראיינים, דנים לא פעם בנושאים מבלי שטרחו ללמוד את העובדות ולגבש עמדה על בסיס ידע'}]
62
Your max_length is set to 3000, but your input_length is only 1266. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=633)
[{'summary_text': 'עיתונאים ישראלים נקלעים בתקופה זו לדילמה לא פשוטה: הסתייגותם ממדיניות ממשלתם כה גדולה, שהם מוצאים את עצמם לא פעם מזדהים עם טענותיהם של בני הפלוגתא שלה'}]
51
Your max_length is set to 3000, but your input_length is only 1345. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=672)
[{'summary_text': 'מוסף הספורט של "ידיעות אחרונות" ממשיך במסורת מופלאה של 40 שנה | מדור הספורט של "ידיעות" ממשיך במסורת מופלאה של 40 שנה | וריח לוואי'}]
49
Your max_length is set to 3000, but your input_length is only 1514. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=757)
[{'summary_text': 'חברת הפרסום מקאן-אריקסון הגישה כתב הגנה בתיק תביעת הדיבה שהגיש אבי בניהו נגדה. החברה טוענת לחסיון מקורות ונוקטת עמדה פובליציסטית לעצם הסוגיה השנויה במחלוקת בפרשת גלנט-הרפז'}]
66
Your max_length is set to 3000, but your input_length is only 1341. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=670)
[{'summary_text': 'מדד הייצוג: ערוץ 2 וחברת החדשות שלו מידרדרים למקום האחרון במדד הייצוג • במקביל, ערוץ 1 ורשת ב מידרדרים למקום האחרון במדד הייצוג • במקביל, התוכניות המובילות של כלי התקשורת בישראל מידרדרות למקום האחרון במדד הייצוג'}]
74
[{'summary_text': 'באיזו מידה העיתונות הישראלית מסייעת בלא מודע לטשטוש המסוכן הזה בין סיבתיות לצורכי צידוק פוליטי (ואידיאולוגי) לבין סיבתיות לצורכי טיפול יעיל בסכנות ובעיות אמיתיות?'}]
51
Your max_length is set to 3000, but your input_length is only 1073. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=536)
[{'summary_text': '"ידיעות אחרונות" ממשיך לקדם את תוכנית הבראה | "הארץ" ממשיך לקדם את המאבק במשרד הבריאות | ו"הארץ" ממשיך לקדם את המאבק במשרד הבריאות'}]
46
Your max_length is set to 3000, but your input_length is only 2112. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1056)
[{'summary_text': '"גלובס" יוצא חוצץ נגד שכר הבכירים, אך נראה כי את סוגיית ה"שכר עוקף דיבידנד" הוא משתדל לעקוף'}]
38
Your max_length is set to 3000, but your input_length is only 2295. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1147)
[{'summary_text': 'העיתונים מדווחים על תקציב הקשר עם הציבור, אך לא על תקציב הוצאות קשר עם הציבור | ב"ישראל היום" מנסים ליצור טבלת בושה | וב"מעריב" מנסים לטפוח לעצמו על השכם'}]
54
Your max_length is set to 3000, but your input_length is only 1874. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=937)
[{'summary_text': 'מוסטפא שלאעטה, מגיש תוכניות אקטואליה ברדיו א-שמס, על העיתונות העברית ועל האופן שבו היא מתמודדת עם מצוקתם של ערבים'}]
44
Your max_length is set to 3000, but your input_length is only 2384. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1192)
[{'summary_text': 'איגוד תעשיות המזון שכר את שירותיו של סמנכ"ל תכנון וכלכלה ברשות המיסים בועז סופר, לשעבר סמנכ"ל תכנון וכלכלה ברשות המיסים • חוות הדעת של בועז סופר: "ייתכן שיש נזק ממשקאות דיאט אבל הוא בוודאי לא נגרם מקיומו של סוכר" • משרד הבריאות: "יש חשש שהיא תימנע מהטלת מס מקביל בשטחה"'}]
101
Your max_length is set to 3000, but your input_length is only 1035. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=517)
[{'summary_text': 'ארגון "חותם" תומך במפלגת נעם, אך תוקף את הרב צבי טאו • דובר הארגון: "התנצלות בה יובהר כי בוחרים במשפחה היא תנועה חברתית ולא קשורה לשום מפלגה בכלל ולתנועת נעם בפרט"'}]
67
Your max_length is set to 3000, but your input_length is only 2858. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1429)
[{'summary_text': 'מרוב ניסיון לטפח את הזקיפות ההיא, יצאנו מה זה קטנים, והטורקים יצאו אנשי הכבוד'}]
28
Your max_length is set to 3000, but your input_length is only 993. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=496)
[{'summary_text': 'השרה להגנת הסביבה הבטיחה להשקיף נתונים, לקצר זמני אכיפה, לקצר זמני אכיפה והתייחסה למשרדה לטיפול רוחבי בגובה הקנסות • המשרד להגנת הסביבה: "אנחנו לא מכירים הקלות" • השרה סילמן: "אנחנו לא מכירים הקלות" • המשרד להגנת הסביבה: "אנחנו לא מכירים הקלות" • המשרד להגנת הסביבה: "אנחנו לא מכירים הקלות"'}]
104
[{'summary_text': 'תביעת פיצויים של 3.5 מיליון דולר שהגישה רשת אל-גזירה נגד סוכנות הצילומים והחדשות רמאטאן בעזה: רמאטאן לא מילאה את התחייבויותיה המקצועיות'}]
48
[{'summary_text': 'העיתונות הישראלית אינה מתייצבת כחוד חנית בהקשר של חוק חופש המידע. היא אינה מתייצבת כחוד חנית בהקשר של חוק חופש המידע'}]
35
Your max_length is set to 3000, but your input_length is only 2574. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1287)
[{'summary_text': '"ידיעות אחרונות" ממשיך להיטיב עם בעלי ההון | "ישראל היום" ממשיך להיטיב עם הדור הצעיר | "הארץ" ממשיך להיטיב עם צה"ל'}]
43
Your max_length is set to 3000, but your input_length is only 1758. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=879)
[{'summary_text': 'בית-המשפט המחוזי קובע כי הרשות הפלסטינית וראשיה השמיעו דברי הסתה נגד יהודים ונגד ישראל, אולם לא הוכיחו מדיניות הסתה מכוונת'}]
42
Your max_length is set to 3000, but your input_length is only 907. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=453)
[{'summary_text': 'מוסף הספורט של "ידיעות אחרונות" מעניק כבוד לכדורסל הנשי | "מעריב" מעניק כבוד לנבחרת הכדורגל | ו"הארץ" מעניק כבוד לנבחרת הכדורגל'}]
52
[{'summary_text': 'בן כספית, כתב "סופהשבוע", הצביע על רקע תביעה של בנק אוף ציינה, שסירב להעיד נגדו במשפט שבו נטען כי כספי טרור סייע לחמאס ולגיהאד-האסלאמי לממן פעולות טרור באמצעות הלבנת כספים'}]
67
Your max_length is set to 3000, but your input_length is only 2563. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1281)
[{'summary_text': '"ידיעות אחרונות" מציג את הצעת אובמה | "הארץ" מציג את הצעת החוק החדשה | "מעריב" מציג את הביקורת הנוקבת ביותר על רשות השידור'}]
45
Your max_length is set to 3000, but your input_length is only 1538. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=769)
[{'summary_text': '"ישראל היום" ממשיך לספק תמונה מורכבת של הנעשה במפלגה | "מעריב" מתעלם מדמות קדושה | "הארץ" ממשיך לחשוף את התוכנית "האח הגדול"'}]
50
Your max_length is set to 3000, but your input_length is only 835. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=417)
[{'summary_text': 'מיקי גנור, הנאשם בשוחד בפרשת הצוללות וכלי הטיס, הגיש בקשה לקבל מידע על קשריה של המשטרה עם עיתונאים שסיקרו עם הפרשה'}]
41
Your max_length is set to 3000, but your input_length is only 453. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=226)
[{'summary_text': 'החפיפה בתחום התקשורת היא כחוזה שבשתיקה, שפרטיו המעורפלים לא כתובים, הסכם שמשאיר את כל הכוח אצל המעביד. המנהל יכול להודיע לך אחרי שבועיים או שלושה שלא התקבלת לתפקיד, ולא לספק הסברים'}]
58
[{'summary_text': '"מעריב" מינה כתב קבוע במרוקו. איש יחסי-הציבור עופר שטרית: "הניסיון לקשור אותי כגורם בעל אינטרס מסחרי לעניין כתב החוץ במרוקו הוא מקומם ולא צודק בעיני"'}]
52
Your max_length is set to 3000, but your input_length is only 909. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=454)
[{'summary_text': '"מעריב" ו"ידיעות אחרונות" מדווחים על שביתה בנתב"ג | "גלובס" ממשיך לקדם את נוחי דנקנר | "ישראל היום" מדווח על גיהאד'}]
48
Your max_length is set to 3000, but your input_length is only 1985. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=992)
[{'summary_text': 'אורי זר אביב: "אני יודע שיש לא מעט אנשים שהאזינו ל"מכורים" ואהבו. אם אתם האנשים האלה, אני מבקש שתתנגדו לסגירת התאגיד, תחתמו על עצומות, תחליפו את הקאבר או את תמונת הפרופיל, שתפו פוסטים או תכתבו פוסטים משלכם, אנלא יודע"'}]
84
Your max_length is set to 3000, but your input_length is only 1934. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=967)
[{'summary_text': 'העיתונות הספורט מנסה לכתוב מלה רעה על אריאל מקדונלד, אבל היא לא ממש עיתונות'}]
29
Your max_length is set to 3000, but your input_length is only 1243. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=621)
[{'summary_text': 'חברת כימוטל הגישה כעת בקשה להיתר בנייה בנמל אשדוד במטרה להקים חווה לאחסון, פריקה וטעינה של חומרים מסוכנים • המשרד להגנת הסביבה קבע כי מדובר באירוע חריג, אך לא קבע כי מדובר בפעילות חלופית • המשרד: "האיגוד נמצא בשלב בחינה ראשונית של כלל ההיבטים הסביבתיים"'}]
87
[{'summary_text': 'דו"ח הוועדה הציבורית לבחינת אירועי המשט הטורקי: צה"ל העביר לידיה את כל חומרי הגלם שצולמו על סיפון המאבי-מרמרה והיו רלבנטיים לחקירה'}]
52
Your max_length is set to 3000, but your input_length is only 501. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=250)
[{'summary_text': '"כלכליסט" מדווח על ירידה במכירות דירות יוקרה | "דה-מרקר" מדווח על אורי שני, מקורבו של שר האוצר, שהחל לנהל את תוכנית הדיור | טוני היילי מסביר כיצד ניתן לקבל מידע בזמן אמת על התנהגות גולשיהם'}]
66
Your max_length is set to 3000, but your input_length is only 1015. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=507)
[{'summary_text': 'העיתונות הצרפתית היתה ערש העיתונות המודרנית, והשתמשה בעיקר בענייני פוליטיים. במאה ה-19 התקבל נוהג זה גם ברוסיה, והיה פופולרי במיוחד ברוסיה'}]
49
Your max_length is set to 3000, but your input_length is only 1191. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=595)
[{'summary_text': 'האגודה הישראלית לתקשורת מזהירה במילים חריפות מפני תוכנית נתניהו-קרעי לחיסול השידור הציבורי בישראל • "פגיעה בתאגיד שידור ציבורי משמעה פגיעה אנושה בתפקידה של התקשורת במדינה דמוקרטית"'}]
53
[{'summary_text': 'עיתונאי, כתב ועורך. היה כתב ועורך בגלי צה"ל, כתב ועורך במחלקת החדשות של הערוץ הראשון, חבר מערכת בתכנית האירוח בערוץ הראשון "עלי כותרת", והגיש תכנית שבועית על תקשורת, "בין השורות", בגלי צה"ל. היה שותף מרכזי בהרחבה העיתון דרך השקת מוספים חדשים כמו "גלריה" ו"קפטן אינטרנט". היה שותף מרכזי בפיתוח פלטפורמת האינטרנט של "הארץ" והוביל את המהלך ליצירת מהדורה אנגלית של העיתון, בדפוס וברשת'}]
131
Your max_length is set to 3000, but your input_length is only 1293. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=646)
[{'summary_text': 'אילן ישועה העיד כי פעל מול יוסי ורשבסקי כדי למנוע פרסום כתבה על בזק • "האמת היא שקר, אבל זה לא זה", השיב עו"ד חן • "האמת היא שקר, אבל זה לא זה", השיב אבי אלקלעי • "האמת היא שקר, אבל זה לא זה", העיד ישועה • "האמת היא שקר, אבל זה לא זה", השיב אבי אלקלעי'}]
100
Your max_length is set to 3000, but your input_length is only 1600. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=800)
[{'summary_text': 'הניסיון להזהיר את הציבור מפני בלוגרים שמקבלים תשלום הוא לא ניסיון תמים. מגישי וכתבי החדשות מנסים, בעקיפין, לרמוז משהו על אובייקטיביות נטולת פניות'}]
49
Your max_length is set to 3000, but your input_length is only 1744. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=872)
[{'summary_text': 'בית-הדין לעבודה חייב את רשות השידור בפיצויים בשל פיטורים שלא כדין של עובד הרשות, תוך שהוא מותח ביקורת על נסיבות הפיטורים וקובע כי נבעו משיקולים זרים'}]
49
[{'summary_text': 'קשה להבין את הצורך הקפריזי של מראיינים בטלוויזיה לכעוס על מרואיינים שלא עונים בדיוק, אבל בדיוק, את התשובה שבה חפצו'}]
37
Your max_length is set to 3000, but your input_length is only 1617. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=808)
[{'summary_text': '"ידיעות אחרונות" ממשיך להפגין | "מעריב" ממשיך להפגין | "ישראל היום" ממשיך להפגין'}]
32
[{'summary_text': 'התיעוד המתפרסם במלחמת יום הכיפורים מוכיח שוב שהם ומערכותיהם נפלו קורבן להטעיה שלטונית גם במהלך הימים הראשונים למלחמה'}]
37
Your max_length is set to 3000, but your input_length is only 1515. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=757)
[{'summary_text': '"ישראל היום" לא מתכונן לשנות את דרכם | "ידיעות אחרונות" ממשיך לחגוג את ראש השנה | סבר פלוצקר מסביר למה כוונתו ל"מאבק על מתווה הגז"'}]
49
[{'summary_text': 'הדס קליין, העוזרת האישית של ארנון מילצן וגיימס פאקר, היתה מעין קניינית של מתנות למשפחת נתניהו. מתנות שעל פי כתב האישום מגיעות לסך של לפחות 700 אלף שקל'}]
54
Your max_length is set to 3000, but your input_length is only 107. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=53)
[{'summary_text': '"ישראל היום" ממשיך לנסות להסביר את עיתוי הדלפת קלטת החטיפה | "ידיעות אחרונות" ממשיך לנסות להסביר את עיתוי הדלפת קלטת החטיפה | רון לאודר ממשיך לנסות להגן על ערוץ 10'}]
65
[{'summary_text': 'יעל געתון התארחה בתוכנית "הזמן הירוק" עם יפעת גליק בכאן 11 כדי לספר על מעקב "שקוף" אחר הנושא שמשפיע על תושבי רמלה והסביבה'}]
48
Your max_length is set to 3000, but your input_length is only 1910. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=955)
[{'summary_text': 'פרשת תנובה, בכיכובה של מיה קוך, התרחשה כשהייתי תלמיד תיכון. לא הייתי מתוודע לַחברה, מעבר להיכרות היומיומית עם מוצריה ועם סיפורה של מיה, אלמלא שבה זו ומילאה תפקיד מפתיע בחיי בשלב מאוחר יותר'}]
66
Your max_length is set to 3000, but your input_length is only 1338. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=669)
[{'summary_text': 'אחרי שידור האייטם הזה אני הולך לקבל יופי של טלפונים עצבניים מלשכת השרה, אבל העיקר שיהיה תחקיר שווה'}]
34
Your max_length is set to 3000, but your input_length is only 2679. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1339)
[{'summary_text': 'חברי הכנסת הסכימו כי יש להטיל סנקציות על חברות שמפיצות דיסאינפורמציה ומידע מטעה במכוון לתכניות הלימודים • יו"ר הוועדה שרן השכל הודיעה כי היא דורשת לסמן את הגופים שנכנסים לבתי הספר לי שלוש קטגוריות: גופים מסחריים יסומנו באדום, גופים פוליטיים בשחור • ועדת החינוך: "לא יכול להיות שיש 6,000 תכניות ואין לי שום יכולת לבדוק אם הן עומדות בסטנדרטים מדעיים"'}]
119
Your max_length is set to 3000, but your input_length is only 1561. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=780)
[{'summary_text': 'אילנה דיין, העיתונאית שכתבה על מוצב גירית שבציר פילדלפי, הגנה על פסק הדין שניתן בעניינה. "אני יכולה לחלוק עליו, אני יכולה לערער עליו, אבל אני צריכה להכיר בו"'}]
55
[{'summary_text': 'שרי התקשורת רוקדים על שתי החתונות ומאמצת לחלופין החלטות סותרות: פעם על הקמת גוף חוץ-ממשלתי ופעם פנים-ממשלתי'}]
41
Your max_length is set to 3000, but your input_length is only 1461. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=730)
[{'summary_text': 'העיתונים מדווחים על השבעת אובמה | העיתונים מדווחים על סיקור המלחמה בעזה | ו"כלכליסט" ממשיך לקדם את הכלכלה הפלסטינית'}]
43
Your max_length is set to 3000, but your input_length is only 2726. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1363)
[{'summary_text': 'השילוב בין מתקפת הקדימונים לפופולריות של הטחינה עשה את שלו. רק שככל שהתקדמה הצפייה, האוויר הלך ויצא מבלון הציפיות הגדולות והותיר תחושת ריקנות שניתן לתמצת במלים "זה הכל?"'}]
58
[{'summary_text': 'המצב הפרוע בתעשייה זו - שהיא חסרת אמנה ואתיקה מקצועית אך מלובה בלהט של מערכת בחירות פוליטית ושל תחרות מסחרית קשה - מטיל על העיתונות תפקיד של מתווך סלקטיבי וביקורתי'}]
53
Your max_length is set to 3000, but your input_length is only 982. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=491)
[{'summary_text': 'העיתונים מדווחים על מהפכה צבאית במצרים | בן-דרור ימיני מסביר את המצב | "גלריה" מציג גישה אלטרנטיבית'}]
41
[{'summary_text': 'קרן פורד תרמה מיליוני דולרים למיזמים חברתיים פורצי דרך ברחבי העולם. תרומות יוצאות דופן אלו מעלות שאלות מעולם התקשורת ומהעולם הפילנתרופי ומספקות נקודת מבט נוספת על המתח הקבוע בין התקשורת לבעלי ההון'}]
62
Your max_length is set to 3000, but your input_length is only 743. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=371)
[{'summary_text': '"מעריב" מציג את התמיכה הגדולה ביותר במבצע הגירוש | "הארץ" מציג את התמיכה הגדולה ביותר במבצע | "ישראל היום" מציג את התמיכה הגדולה ביותר במבצע'}]
44
[{'summary_text': 'כתב האישום נגד ראש עיריית אשקלון: שמעוני שקע בחובות של כמיליון שקל כשנדרש לממן שני הסכמי פיצויים לנשים שטענו כי פגע בהן מינית'}]
45
Your max_length is set to 3000, but your input_length is only 2221. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1110)
[{'summary_text': 'מדור חופש המידע של "הגנזך", מדור חופש המידע של "העין השביעית" בשיתוף "הצלחה", מוצגים מסמכים על רשות השידור, רשות השידור ומשרד האוצר'}]
47
Your max_length is set to 3000, but your input_length is only 1530. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=765)
[{'summary_text': 'אורי משגב, עיתונאי "הארץ", מתאר כיצד התערבו באופן קשה בעבודתו העיתונאית כדי לשרת אינטרסים ורצונות זרים מטעמם של העורך האחראי ובעל השליטה בעיתון. "אני מקווה שנסלחת", כתב משגב'}]
63
[{'summary_text': 'הדיון בוועדת העבודה והרווחה בוועדת העבודה והרווחה עורר התרגשות גדולה - אך הצדה גם מודעות לחוסר ההתעניינות התקשורתית בנושא החשוב • ח"כ נירה שפק: "הצעת החוק הייתה עוזרת לי מאד"'}]
60
Your max_length is set to 3000, but your input_length is only 2709. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1354)
[{'summary_text': 'העיתונים מדווחים על פקעת סבוכה | העיתונים מדווחים על פקעת סבוכה | ו"ידיעות אחרונות" ו"ישראל היום" מנסים למנוע פרסום שקר'}]
46
Your max_length is set to 3000, but your input_length is only 1925. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=962)
[{'summary_text': 'משפחת אלונה בר-און מבקשת מבית-המשפט לעצור את הליך מכירת מניותיו של אליעזר פישמן ב"גלובס" • אלונה בר-און: "התנהלות הכונסים מנעה מהם הלכה למעשה להגיש את הצעתם"'}]
61
Your max_length is set to 3000, but your input_length is only 1649. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=824)
[{'summary_text': '45 מתים במירון, מאחוריהם 43 משפחות שעולמן חרב עליהם ורוצות לדעת איך זה קרה. איך אירוע שמחה דתי הפך לטרגדיה מבלי שקרה שום דבר חריג - שום שריפה לא פרצה, טרור לא קרה, אפילו טריבונה לא קרסה. אנשים פשוט הלכו ונמחצו למוות. שורה של מסרים יכולים לעזור לך: זה לא הזמן למצוא אשמים, "קודם נקבור את מתינו", "ניתן למשפחות לקום מהאבל" ועוד מיני קשקושים. כל אלו יעזרו למרוח זמן – והזמן עושה את שלו'}]
133
[{'summary_text': 'מנכ"לית בנק לאומי נראתה לפתע כה שברירית ומעוררת אמפתיה אל מול מטר השאלות. האם זו האישה הקשוחה שמנהלת עשרות אלפי עובדים?'}]
44
Your max_length is set to 3000, but your input_length is only 1009. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=504)
[{'summary_text': 'בן כספית ממשיך לטפל באולמרט | "מעריב" ממשיך לטפל באם-תרצו | "ידיעות אחרונות" ממשיך לטפל באולמרט'}]
42
Your max_length is set to 3000, but your input_length is only 134. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=67)
[{'summary_text': 'כולנו המומים ודואבים ומרכינים ראשים, מיקרופונים, פונטים – גם מצלמות! בוודאי! – מול הרצח הנתעב, רצח של ילדים חפים מפשע שעלינו, על כולנו, לגנות, ולהזדעזע מהאקט האלים הזה, החשוך, חשוך אפילו עוד יותר מן הארון שנפתח כך, בלי התראה'}]
84
[{'summary_text': 'ח"כ חיים כץ מואשם בכך שעזר לחברו, איש שוק ההון מוטי בן-ארי, בקידום חקיקה שתסייע לבן-ארי ישירות, בזמן שהוא מרוויח מהצד כסף באמצעות טיפים של בן-ארי'}]
56
Your max_length is set to 3000, but your input_length is only 1299. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=649)
[{'summary_text': 'העיתונים הכלכליים מדווחים על דו"ח העוני של הביטוח הלאומי | "מעריב" קורא לנתניהו להחרים את ישיבת עוד-יוסף-חי | "הארץ" ממשיך לנסות לחשוף את רפי אדר'}]
57
Your max_length is set to 3000, but your input_length is only 2552. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1276)
[{'summary_text': 'התמונה החוזרת של חבורת הגברים שעומדת במרכז הסדרה מגלמת את מושג "החברות הגברית" שעומד ביסוד הסדרה. מובן שאין כאן חברות שאינה תלויה בדבר'}]
44
Your max_length is set to 3000, but your input_length is only 1822. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=911)
[{'summary_text': '"המדיום הוא המסר", אומר מרשל מקלוהן, "המדיום הוא המסר". תגובה למאמרו של ארמנד בלום'}]
34
Your max_length is set to 3000, but your input_length is only 2584. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1292)
[{'summary_text': 'העיתונות המסחרית, ש"ידיעות אחרונות" הוא המלך הבלתי מעורער שלה בישראל, אם להשתמש במונחי הזאנר, מחפיצה נשים ביד אחת ומגנה את ניצולן באחרת'}]
50
Your max_length is set to 3000, but your input_length is only 2983. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1491)
[{'summary_text': '"ידיעות אחרונות" ממשיך לחשוף את הקלות שבה יכול כל אדם להגיע לאיש הציבור המאובטח | "ישראל היום" ממשיך לחשוף את האפשרות שעיתונאים ייגשו לאנשי ציבור עם אקדחי צעצוע | ו"הארץ" ממשיך להעניק את הכותרת הראשית לפעילות הצבאית בעזה'}]
77
Your max_length is set to 3000, but your input_length is only 301. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=150)
[{'summary_text': 'העיתונות הערבית מאמצת לעצמה אוצר מלים חדש ועקיף כדי לתאר את המצב לאשורו'}]
27
[{'summary_text': 'חוקר "תיק 4000" הסביר את ההיגיון מאחורי חקירת הפרשה: "אפשר לחקור את כל הפוליטיקאים שאין סיבה לחקור אותם ואין חשד נגדם. למה שנחקור אותם? אפשר לחקור את כל חברות התקשורת ולבדוק מי עשה כמה". פרק 1'}]
71
Your max_length is set to 3000, but your input_length is only 1769. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=884)
[{'summary_text': 'התוכנית הלילה הפופולרית "הלילה" של ארנולד שוורצנגר היתה הפעם הראשונה ששוורצנגר לא הרגיש בנוח להשחיל באמצע הראיון את הביטוי "אסטה לה ויסטה, בייבי".'}]
53
Your max_length is set to 3000, but your input_length is only 1677. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=838)
[{'summary_text': 'ערוץ הספורט וצרלטון מצטמצמים בכעס | ב-one לא מרוצים מהקיומו של ערוץ הספורט | ורוצים לשחרר את המבוגר האחראי מהמרתף'}]
44
Your max_length is set to 3000, but your input_length is only 2050. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1025)
[{'summary_text': 'המו"ל והעורך הראשי של "מעריב" ו"מקור ראשון" התווה את חזונו לעיתון חדש שייווצר מאיחוד שני היומונים שתחת אחריותו'}]
38
Your max_length is set to 3000, but your input_length is only 1467. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=733)
[{'summary_text': 'העיתונות הישראלית מפחדת שיאשימו אותם בחוסר נאמנות ופטריוטיות, אבל גם מי שבטוח שחמאס הוא האשם הבלעדי במצבם של תושבי הרצועה, צריך לדעת אל נכון מהו אותו מצב'}]
50
Your max_length is set to 3000, but your input_length is only 1193. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=596)
[{'summary_text': 'המדינה חייבת לשמור על סודותיה. עיתונות טובה בענייני צבא וביטחון לא תוכל למלא את תפקידה הציבורי ללא מדליפים וללא מקורות חסויים'}]
39
Your max_length is set to 3000, but your input_length is only 866. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=433)
[{'summary_text': 'עיתונאי "הארץ" אמיר אורן ועיתון "מעריב" הגיעו להסכם גישור: "חופש הביטוי והשמירה על עיתונות חופשית, מדווחת, מבקרת וחוקרת, הינו נר לרגלם"'}]
58
Your max_length is set to 3000, but your input_length is only 2209. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1104)
[{'summary_text': 'ועדת האתיקה בכנסת ה-23 היא ועדה מורכבת משני נציגים מהקואליציה ושניים מהאופוזיציה. ההחלטות שמתקבלות בה מתקבלות בקונצנזוס והיא זהירה, יש שיגידו זהירה מדי, בהחלטות נגד חברי כנסת. כלומר, צריך ממש להגזים באופן קבוע כדי להיענש מעבר ל"הערה"'}]
84
Your max_length is set to 3000, but your input_length is only 902. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=451)
[{'summary_text': 'במלחמת המאסף של עיתונות האיכות בשדה מערכה רב־ערוצי, צפוף מתחרים, עתיר טכנולוגיות תקשורת חדשניות, זה היה אולי אחד הקרבות האחרונים'}]
41
Your max_length is set to 3000, but your input_length is only 2231. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1115)
[{'summary_text': 'לשכת ראש הממשלה מתכוונת לקבוע מי יהיו הבלוגרים הראשונים שיקבלו תעודת עיתונאי. האם הם יהיו "רציניים ומובילים"?'}]
34
Your max_length is set to 3000, but your input_length is only 1826. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=913)
[{'summary_text': 'לא חשוב כמה שנים אדם עוסק בעריכת עיתונים: החוויה של קבלת העיתון המודפס־טרי בבוקר ופרישתו בלב דופק אינה מתקהה עם השנים'}]
40
Your max_length is set to 3000, but your input_length is only 718. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=359)
[{'summary_text': 'תשלום בעבור קומקום ושולחן המוצבים בלובי הבניין לשימוש המאבטח לא צריך לעמוד על יותר משקלים בודדים בחודש – ודאי לא על יותר מ-1,000 שקל לחלק מהחודשים, כפי שעולה מההזמנות הספורדיות שמופיעות בדו"חות ההתקשרות הפומביים. מה שכן, נראה שמשתלם להיות שכן של דרעי: תושבי הבניין לא רק זכו לשומר צמוד – אלא גם לתשלומים מופרכים על חשבון הציבור'}]
110
Your max_length is set to 3000, but your input_length is only 2949. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1474)
[{'summary_text': 'האם בית-המשפט פסל את שידור התחקיר שהכין שמעון קופר על שמעון קופר? האם התקשורת הישראלית סומכת על כך שתקבל חומרי גלם מהנעשה בהפגנות מצלמים מקומיים? ומה קורה עם שרה ב"ק?'}]
60
[{'summary_text': 'טיוטת כתב האישום בפרשת מנופים-פיננסיים אינה מעלה חשד כלשהו בנוגע להתנהלותם של גולן חזני ו"כלכליסט"'}]
38
Your max_length is set to 3000, but your input_length is only 815. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=407)
[{'summary_text': 'העיתונים מדווחים על העלאת שכר המינימום | "ידיעות אחרונות" ממשיך לטפל במאבקי השכר | "ישראל היום" ממשיך לטפל במאבקי השכר'}]
45
Your max_length is set to 3000, but your input_length is only 1120. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=560)
[{'summary_text': 'התוכנית "ימי חיינו" ו"צעירים חסרי מנוח" הורדה מהמרקע של אופרות סבון. הוט: לא צפוי לה להודיע על כך'}]
37
Your max_length is set to 3000, but your input_length is only 988. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=494)
[{'summary_text': 'מנכ"ל הכנסת אלברט סחרוביץ הודיע כי יש להחזיר מיידית את ההגבלות המחמירות באופן מיידי. "הכנסת צריכה להגיב עכשיו", אמר לשקוף. "יש משמעות למהירות התגובה"'}]
53
Your max_length is set to 3000, but your input_length is only 2614. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1307)
[{'summary_text': 'העיתונות העולמית מספידת את ה"ניו-יורק אובזרבר", ה"ניו-יורק טיימס" מספיד את "ניוזוויק", ה"ניו-יורק אובזרבר" מספיד את "ניוזוויק", ועוד חדשות טובות מהרשת העולמית'}]
66
Your max_length is set to 3000, but your input_length is only 1380. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=690)
[{'summary_text': 'סיקור השלב הנוכחי במלחמה הישראלית-פלסטינית הוא אתגר לא פשוט: שני הצדדים תובעים במפגיע את תפקיד הקורבן, ולכל אחד מהם יש ראיות טובות לבסס את התביעה שלו'}]
45
Your max_length is set to 3000, but your input_length is only 560. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=280)
[{'summary_text': 'יואב קרני, הומניסט שכמותו, אינו מבקש פגיעה אישית גופנית ("אל נא תיפול שערה משערות ראשו של הבוגד"), ומסתפק בדרישה-תקווה שלוי יוקע אל עמוד הקלון'}]
54
[{'summary_text': 'מעכשיו מפרסם משרד המשפטים את התייצבויותיו של היועמ"ש אביחי מנדלבליט באופן שקוף, לעיתים גם לצד ההחלטה שהתקבלה לבסוף בבית המשפט. השקיפות הזו מאפשרת לכל אחד לגשת לחומר הגלם וללמוד ממקור ראשון מה עמדת המדינה בהליכים שעשויים להשפיע על כולנו'}]
75
Your max_length is set to 3000, but your input_length is only 324. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=162)
[{'summary_text': 'סוכן מוכשר שמשיג לכוכביו חוזים מרשימים למדי בהתחשב בתנאי השוק. הוא אכן מילא תפקיד מפתח בהדחתו של אבי ברזילי וגם סייע בהכשרת הקרקע להדחתו של אורי שנער מ"קשת". מצד שני, אלמלא תמך מודי פרידמן בפיטוריו של ברזילי, כל המאמץ שהשקיע נשר היה לשווא'}]
91
Your max_length is set to 3000, but your input_length is only 1066. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=533)
[{'summary_text': 'אתרי האקטואליה המובילים מדווחים על רעידת אדמה קטלנית בסין, אך לא על המקרה. מה קורה עם העיתונים החשובים בעולם?'}]
41
[{'summary_text': 'ב"מעריב" מכחישים כי מתקיים חרם מודעות על העיתון. ב"ישראל היום" לא פירסמו מודעות לרשת שופרסל. ב"מעריב" מכחישים כי מתקיים חרם מודעות על העיתון'}]
55
[{'summary_text': 'העיתונאים דן מרגלית ומרדכי גילת שומרים על עקביות ביחסם לראש הממשלה, אך לא מנסים להתפטר ממנו'}]
34
Your max_length is set to 3000, but your input_length is only 753. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=376)
[{'summary_text': '"ישראל היום" לא מדווח על המתים בעזה | "ידיעות אחרונות" ו"מעריב" מדווחים על מלחמה | דרור אידר מאשים את "הארץ" בהסתה ועלילת דם'}]
50
Your max_length is set to 3000, but your input_length is only 2293. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1146)
[{'summary_text': 'לאחר סערה ציבורית בנושא הוצאות הרשויות המקומיות ביום העצמאות, מינה השר אריה דרעי ועדה שתבדוק את הנושא. הוועדה המליצה על שורת צעדים, והשר הבטיח שיגביל את הסכומים שיותרו לרשויות להוציא על הופעות, כבר ביום העצמאות 2020'}]
73
Your max_length is set to 3000, but your input_length is only 1497. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=748)
[{'summary_text': 'ניב רסקין, המנחה החדש של "יציע העיתונות", מגיש את "נכון להבוקר" ארבעה ימים בשבוע | ערוץ הספורט ממשיך לשלם את המחיר על פרסום סמוי | ו"ישראל היום" ממשיך לשלם את המחיר על העיתונות'}]
61
Your max_length is set to 3000, but your input_length is only 1658. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=829)
[{'summary_text': '"ידיעות אחרונות" ממשיך לחפש את הפוליטיקאים | אבי נמני ממשיך לחפש את שירלי בר-דיין | ו"מעריב" ממשיך לקדם את ליגת הנוער'}]
45
Your max_length is set to 3000, but your input_length is only 2188. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1094)
[{'summary_text': 'העיתונים מדווחים על טור של גלעד שליט, אבל לא על טור של אריק הניג | "ידיעות אחרונות" ממשיך לספק טור של גלעד שליט'}]
44
[{'summary_text': 'אילן שילוח, יו"ר משרד הפרסום מקאן-אריקסון, מצהיר כי הוא האדם העומד מאחורי תוכנה של מודעה שפורסמה בעיתונים נגד דובר צה"ל לשעבר אבי בניהו'}]
51
Your max_length is set to 3000, but your input_length is only 499. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=249)
[{'summary_text': '"העיר" של רשת "העיר" ו"תל אביב" של "ידיעות אחרונות" סיקרו שתי מערכות בחירות לראשות עיריית תל-אביב ולמועצתה בינואר-אפריל 1998 וינואר-אפריל 2008'}]
58
Your max_length is set to 3000, but your input_length is only 1297. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=648)
[{'summary_text': 'האם משהו משתנה ביחסן הסלחני של רשויות החוק לתחנות הרדיו הפיראטיות? לאחר שנים שבהן עשרות תחנות פעלו כמעט ללא הפרעה'}]
37
Your max_length is set to 3000, but your input_length is only 463. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=231)
[{'summary_text': 'הכנסת ממשיכה במגמה, אך עדיין לא התקיימו בה דיונים על חוק התקציב הספיקה להפעיל את השימוש בסעיף 98. היועצת המשפטית של הכנסת שגית אפיק התריעה כי: "יש כאן פירצה של השימוש בסעיף. מספר ההסתייגויות שהוגשו, נמוך ביותר. נכון יותר להגיע להבנות"'}]
77
[{'summary_text': 'האם עיתונאי "מעריב" קלמן ליבסקינד מבקר את האלוף יואב גלנט? האם עיתונאי "מעריב" מבקר את האלוף יואב גלנט? ומה קרה עם האלוף יואב גלנט?'}]
54
Your max_length is set to 3000, but your input_length is only 1876. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=938)
[{'summary_text': 'העיתונים מדווחים על יום אחד של שטייניץ | "מעריב" מעניק כבוד לענת קם | "ידיעות אחרונות" מבקר את רביב דרוקר'}]
41
Your max_length is set to 3000, but your input_length is only 1128. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=564)
[{'summary_text': 'ארגון זכויות הפרט האלקטרוניות EFF מצא את הדרך לערער על הסרה של סרטון מחאה של חברת קונסטנטין. המערכת מאפשרת לבעלי זכויות יוצרים לבחור בפשרה: האם הסרטון להוריד ואילו לא, על-פי שיקולים פוליטיים או מסחריים'}]
67
Your max_length is set to 3000, but your input_length is only 575. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=287)
[{'summary_text': 'יעקב אילון, מגיש החדשות המרכזי של ערוץ 10, מתאר את האופן שבו התנהלו הגורמים הרלבנטיים בחברה, על האופן שבו בחר לקיים את מהדורת החדשות בירושלים'}]
50
[{'summary_text': 'המשטרה מפרסמת נתונים פנימיים שמראים שזמן התגובה הולך ומתארך בכל שנה. המשטרה: "הנתונים מודדים תהליכים בארגון בתחום השירות ואינם מהווים מדד למענה מבצעי"'}]
49
Your max_length is set to 3000, but your input_length is only 568. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=284)
[{'summary_text': 'השינוי במוסף סוף-השבוע של "גלריה" יביא לחורבן על המערכת, יביא לשינוי בתנאי עבודתם ויגרום לתגובה שלילית מצד המנויים'}]
41
[{'summary_text': 'בית-הדין לעבודה קבע כי ארגון העיתונאים של ההסתדרות הוא ארגון העובדים היציג בחברת וואן ספורט שירותי טלוויזיה בע"מ'}]
37
Your max_length is set to 3000, but your input_length is only 2221. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1110)
[{'summary_text': 'יפעת בן-חי שגב, יו"רית מועצת הכבלים והלוויין לשעבר, הגיעה לבית-המשפט המחוזי בירושלים בתביעה שהגישה נגד נתניהו • "אני מצטערת מאוד לומר, אבל מכיוון שהתחייבתי להגיד פה את האמת ורק את האמת – החקירה שעברתי היתה חקירה חובבנית, רשלנית ומגמתית, תוך כדי הטלת מורא ופחד, בתנאים אנושיים לא מקובלים שצריכים להטריד כל אזרח במדינת ישראל"'}]
115
Your max_length is set to 3000, but your input_length is only 1589. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=794)
[{'summary_text': 'הכנסת אישרה בקריאה שנייה ושלישית את חוק המאבק בטרור, המכונה גם "חוק המחשבות". החוק אוסר על צריכה שיטתית וממושכת של פרסומי טרור, אך ייבחנו גם הנסיבות בהן נעשתה צריכה שיטתית ומתמשכת של פרסומי טרור'}]
66
Your max_length is set to 3000, but your input_length is only 2084. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1042)
[{'summary_text': 'ההרשעה בתיק הולילנד היא הישג אסטרטגי במאבק בשחיתות בישראל; לא רק בגלל מעמדם הרם והנישא של המושחתים, אלא בעיקר בגלל האופי המאפיוזי המובהק של שחיתותם'}]
54
Your max_length is set to 3000, but your input_length is only 1015. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=507)
[{'summary_text': 'הוועדה הציבורית לשכר הח"כים ותנאיהם החליטה לאשר את תקציב הכיבוד והתקשורת ישירות לתלוש המשכורת של הח"כים, שיוכלו לבחור כיצד להוציא את הכסף מחשבון הבנק שלהם • המהלך יעלה לציבור כפול, אך לא יאפשר לציבור לשלם את הוצאות התקשורת • תקציב הקשר עם הבוחר: 98 אלף שקלים להוצאות לשכה, כנסים וקידום ברשתות החברתיות'}]
102
[{'summary_text': 'בעקבות חשיפת "שקוף": במשרד החינוך הקפיאו את תוכנית הלומדות שמממנות חברות האנרגיה קצא"א ודוראד בבתי ספר בדרום. בשבוע שעבר חשפנו כי החברות מעבירות ב6 השנים האחרונות את תוכנית "אנרגיה צעירה", המציגה לומדות בשבחי הגז, מבלי לציין את הנזקים, ובניגוד לכללים של משרד החינוך'}]
87
Your max_length is set to 3000, but your input_length is only 457. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=228)
[{'summary_text': 'דן שכטמן, האיש האמון על מחקר, יוצא לדרך ללא הכנה, היטלטל וניגף כמעט בכל צעד שעשה. המערכת הפוליטית לא עושה הנחות לאף אחד'}]
45
[{'summary_text': 'דו"ח המבקר הפנימי של ההסתדרות מפרט פעולות שיש בהן סטייה מעקרונות החיסכון והיעילות או פגיעה בטוהר המידות, שלדעתו מן הראוי לדווח עליהן'}]
49
Your max_length is set to 3000, but your input_length is only 994. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=497)
[{'summary_text': 'פרשני "ישראל היום" ו"ידיעות אחרונות" מדווחים על ניצחון לנתניהו | "הארץ" מדווח על כתובות גזעניות בבת-ים | "הארץ" מדווח על כתובות גזעניות בבת-ים'}]
58
Your max_length is set to 3000, but your input_length is only 1475. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=737)
[{'summary_text': 'מיזם החאמסות של עורך "ידיעות אחרונות" רון ירון הוא פרסום סמוי למוצר של זרוע אחרת של הקבוצה? הקדמה: אתמול התפרסם בעיתון שער אחורי בפריסה חגיגית ומיוחדת, שהוקדש כולו לאיור בשחור-לבן של חאמסה'}]
70
[{'summary_text': 'צרלטון מנסה להפוך את באר-שבע לעיר ה"נידחת" | צרלטון מנסה להפוך את קריית-שמונה לעיר ה"נידחת" | ו-one מנסה להפוך את one לעיר ה"נידחת"'}]
63
[{'summary_text': 'העיתונים מדווחים על פסק דין קצב | "כלכליסט" מדווח על משבר האיטליה | "ישראל היום" מוצא פתרון לבעיה האיראנית'}]
40
Your max_length is set to 3000, but your input_length is only 805. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=402)
[{'summary_text': 'מבקר המדינה מתניהו אנגלמן מציג תמונה מטרידה שלפיה המפלגות הכפילו את שכר חלק מהעובדים לפני תקופות הבחירות, והוציאו כספים לכאורה שלא כדין - על חשבון הציבור • הבעיה - אין לנו דרך להעריך את מימדי התופעה או לדעת על אילו מפלגות מצביע המבקר, מכיוון שלטענתו הוא לא מצא דרך לגלות מי אחראי • המפלגות עצמן מכחישות את הדבר'}]
101
[{'summary_text': 'העיתונאים בהאיטי ממשיכים לשלם חינם למנויים שלהם, אבל לא רק לעיתונאים, אלא גם לעיתונאים אחרים. מה קורה בסרי-לנקה, מה קורה באסה, ומה קורה בארצות-הברית'}]
55
Your max_length is set to 3000, but your input_length is only 1952. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=976)
[{'summary_text': 'העיתונים מתכוננים לפריצתה של אינתיפאדה שלישית | "ישראל היום" מתכונן למלחמה בפלסטינים | "כלכליסט" ממשיך לחגוג את הפרוטוקולים של ועדת טרכטנברג'}]
52
[{'summary_text': '"העניין מתעצם בעניינו של קינן, שכן לא הסתפק ששי בעיר בפרסום הכתבה, אלא טרח וצרף את תמונתו בגודל של ¼ עמוד"'}]
43
Your max_length is set to 3000, but your input_length is only 998. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=499)
[{'summary_text': 'העיתונים מדווחים על יום ירושלים | "ישראל היום" מצטט את יהודים דתיים מבקרים בהר-הבית | "מעריב" מצטט את נוחי דנקנר'}]
43
Your max_length is set to 3000, but your input_length is only 200. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=100)
[{'summary_text': 'מדוע הלשכה הממשלתית מחרימה את העיתון "דו-עט" ואינה מוסרת לו מודעות לפרסום?'}]
30
[{'summary_text': 'עיתונאי הספורט אביעד פוהורילס, עורך ומגיש את "גולאסו", חשף את פרופיל הפייסבוק שלו. שלושת הטוקבקים נמחקו'}]
41
Your max_length is set to 3000, but your input_length is only 2080. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1040)
[{'summary_text': 'הנהלת "ידיעות אחרונות" מנסה למנוע את המעבר לחוזים אישיים, אך לא מצליחה למנוע את המעבר'}]
30
[{'summary_text': 'הסיקור התקשורתי של אולימפיאדת בייגינג מחדד שוב את הכשלים בהתנהלותה של תקשורת הספורט בארץ, זו שביומיום מקצה שטחים מופרזים לסיקור כדורגל, מעלה שחקנים לדרגת מלאכים, ומתעלמת ממאות ספורטאים בעשרות ענפים, שעובדים קשה כדי לגרד כמה גרושים מהאגודות'}]
80
Your max_length is set to 3000, but your input_length is only 2433. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1216)
[{'summary_text': 'גון מילוורד, עורך תחקיר על 10,000 כוכבי פורנו, מנסה לפענח את האופן שבו הוא מפיק את המידע העצום על תעשיית המין'}]
47
[{'summary_text': 'אריאל שרון, בלי שום כוונת עלבון, הוא מותג לאומי ממש כמו השוקולד הקלאסי של "עלית", ההוא עם ציור הפרה והעטיפה האדומה: נדמה שהיה כאן תמיד'}]
47
Your max_length is set to 3000, but your input_length is only 2569. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1284)
[{'summary_text': '"מעריב" ו"ידיעות אחרונות" מדווחים על גלעד שליט | "מעריב" ו"ידיעות אחרונות" מדווחים על גלעד שליט | בן כספית תוקף את "ישראל היום"'}]
53
Your max_length is set to 3000, but your input_length is only 800. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=400)
[{'summary_text': 'העיתונים מדווחים על פרישתו של ברק | ברק לא פורש | ו"הארץ" ממשיך לצאת ללא חלק ב'}]
32
Your max_length is set to 3000, but your input_length is only 2115. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1057)
[{'summary_text': 'דובר צה"ל דניאל הגרי הציג תדרוך לתקשורת בו התייחס באופן מפורט ונרחב לפיצוץ הקטלני בבית החולים בעזה. הדובר הציג במהלך התדרוך פרטים שונים מתוך הבדיקות שבוצעו על ידי צה"ל בקשר לסיבות שהובילו לפיצוץ עתיר הנפגעים'}]
74
[{'summary_text': 'הודעתו של רונן משה על חופשה זמנית מדירקטוריון חברת החדשות הישראלית אינה בבחינת פתרון כלשהו לבעיית ניגוד העניינים הנוצרת בשל עיסוקיו השוטפים'}]
45
Your max_length is set to 3000, but your input_length is only 270. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=135)
[{'summary_text': 'העיתונות הזרה של מחלקת המדינה האמריקאית היא זו שצריכה לבדוק את העובדות. מישל אוסטין ברוקס, מנהלת הניו-מדיה בבית הלבן, סיקרה את הבחירות לנשיאות ב-2008, וכתבה על הקשר הישיר בין פוליטיקאים לקהל הבוחרים הפוטנציאלי שלהם'}]
76
Your max_length is set to 3000, but your input_length is only 1287. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=643)
[{'summary_text': 'חיים זיסוביץ על הדלפות של תמלילי החקירה של אהוד אולמרט | יאיר גרבוז על הטלוויזיה כמשק אוטרקי | יאיר גרבוז על הפוליגרף'}]
47
Your max_length is set to 3000, but your input_length is only 1631. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=815)
[{'summary_text': 'פרשת הפלגיאט: ה"ניו-יורק טיימס" מתלונן על כך שהאינטרנט בוזז את חומריו, ה"ניו-יורק טיימס" מתלונן על כך שהאינטרנט בוזז את חומריו, ועוד חדשות תקשורת מהרשת העולמית'}]
66
[{'summary_text': 'הבחירה בהכחשה מוחלטת וגורפת מתנגשת לכאורה עם תמונת המציאות כפי שהיא הולכת ומצטיירת, ולכן עלולה לפגוע באופן אנוש באמינותם המקצועית של שני העיתונאים הידועים האלה'}]
51
Your max_length is set to 3000, but your input_length is only 393. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=196)
[{'summary_text': 'העיתונות הכלכלית הישראלית התייחסה אליעזר פישמן לעיתונות הכלכלית כמי שפעל נגד האינטרסים של בעל השליטה ב"גלובס" אליעזר פישמן. העיתונות הכלכלית בישראל התייחסה אליו כמי שפעל נגד האינטרסים של בעל השליטה ב"גלובס" אליעזר פישמן'}]
75
[{'summary_text': 'עיתון העוסק בענייני תקשורת צריך לדעת, שאת הכותרות של הידיעות המתפרסמות בעמודי החדשות מנסחים, בדרך-כלל, עורכי הלילה, ולא הכתבים שמסרו אותן'}]
47
Your max_length is set to 3000, but your input_length is only 1191. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=595)
[{'summary_text': '"ידיעות אחרונות" ממשיך לחשוף מידע רגיש | "מעריב" ממשיך לחשוף את פגיעה בלטקיה | גידי וייץ מסביר את הסדר הטיעון של דן כהן'}]
48
[{'summary_text': 'המזון המעופש של מדורי הספורט יגדיל את מספר הקוראים של העיתונות המודפסת, שהולך ומתמעט גם ככה, או שבבוא יום הדין האמיתי יעמדו שוב עורכים וכתבים בתור לתא הווידויים ויודו שהסיבה העיקרית לבריחת הקוראים היא עובדה פשוטה: הם מתעסקים בטפל'}]
77
Your max_length is set to 3000, but your input_length is only 1940. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=970)
[{'summary_text': 'העיתונות הכלכלית מתכוננת להחלפת עיתונות | רועי ורמוס ממשיך לנסות להוכיח כי הוא אינו מסקר את ההתפתחויות מהזווית הפרסונלית | ו"דה-מרקר" ממשיך לנסות להוכיח כי הוא אינו מסקר את ההתפתחויות מהזווית העקרונית'}]
73
[{'summary_text': 'דו"ח ועדת גרונאו מציג את דרך המוצא הסבירה היחידה להגברת התחרות בתחום התקשורת בישראל. הפתרון שמציעה הוועדה הוא חיוב הספקים הקיימים להעניק למתחריהם זכות שימוש במקטעי תשתית'}]
55
[{'summary_text': 'העדפת כלי תקשורת על-ידי משרד החינוך בעייתית במיוחד לנוכח הפיקוח ההדוק שמפעיל המשרד על מקורות המידע שתחת סמכותו. "ידיעות אחרונות" הוא העיתון הנפוץ במדינה, ועל כן זוהי מדיניות המשרד'}]
56
Your max_length is set to 3000, but your input_length is only 2967. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1483)
[{'summary_text': 'העיתונים מדווחים על הפגנת 300 אלף מפגינים | "ידיעות אחרונות" ממשיך לנסות לקדם את המאבק | סבר פלוצקר ממשיך לנסות לקדם את המיסוי'}]
51
[{'summary_text': '"ידיעות אחרונות" מתעלם לחלוטין מהאיום על המפעל של תפרון | "ישראל היום" מצטט את ניר חפץ | "הארץ" מצטט את נשיא איראן'}]
46
Your max_length is set to 3000, but your input_length is only 1036. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=518)
[{'summary_text': '"מעריב" ממשיך לנסות להגן על נתניהו | "ידיעות אחרונות" ממשיך לנסות להגן על יהושע בן-ציון | ו"גלובס" ממשיך לנסות להגן על עיתונאים'}]
49
Your max_length is set to 3000, but your input_length is only 1920. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=960)
[{'summary_text': 'אחרי הפסקה קלה במצעד הח"כים הנעלמים, הפעם נתמקד ב(חוסר) פועלו של חבר הכנסת מהליכוד חיים כץ. נראה שלצד ההתמודדות עם תיקו הפלילי הוא לא מצא זמן רב לבצע את עבודתו למען הציבור שבחר בו לבית המחוקקים. כץ חתם לאחרונה על הסדר טיעון בעבירה שגורדה מתחתית ספר החוקים: "השגת מטרה כשרה באמצעים פסולים". אחת הסיבות המרכזיות שהובילו להפחתה משמעותית מעבירה של הפרת אמונים שבה נחשד לעבירה מקלה היא החסינות שקיבל מחבריו לכנסת, חסינות מפני העמדה לדין בכנסת ה-22 (פברואר 2020). מתן החסינות הביא לעצירת ההליך כולו. לקראת פרישתו של היועמ"ש לשעבר אביחי מנדלבליט, התיק נסגר וגומד'}]
197
Your max_length is set to 3000, but your input_length is only 785. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=392)
[{'summary_text': 'השופט רוזן בחר במונח "בוגד" כדי לתאר את מעשיו של איש ציבור המועל באמון הציבור. המלים מעצבות את תודעת הציבור'}]
39
Your max_length is set to 3000, but your input_length is only 1587. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=793)
[{'summary_text': 'אנשים בכירים בליכוד, המתנגדים לתוכנית ההינתקות של אריאל שרון, תהו בשבועיים האחרונים עד כמה היתה התקשורת הישראלית ממררת את חייו לו, בנסיבות הקיימות, היה מחליט לא על נסיגה מרצועת עזה אלא על סיפוח מעלה-אדומים'}]
67
Your max_length is set to 3000, but your input_length is only 2016. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1008)
[{'summary_text': 'השליט הסורי בשאר אסד פירסם תקנות חדשות לחוק התקשורת, המבטלות את עונש המאסר לעיתונאים שהורשעו בדיבה. השליט הסורי בשאר אסד: "פירסם תקנות חדשות לחוק התקשורת"'}]
54
Your max_length is set to 3000, but your input_length is only 1384. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=692)
[{'summary_text': 'נועם אמיר, הכתב הצבאי של ערוץ 20, על האופן שבו מתמודד כתב צבאי עם מערך הדוברות של צה"ל, על היכולת להטיח ביקורת בצה"ל במדינה שבה הצבא הוא פרה קדושה'}]
59
Your max_length is set to 3000, but your input_length is only 1928. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=964)
[{'summary_text': '"ידיעות אחרונות" נחשף יותר ויותר כמכונת מניפולציות משוכללת, המזכירה את התינוק המפלצתי שהולידה, "ישראל היום"'}]
40
Your max_length is set to 3000, but your input_length is only 1534. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=767)
[{'summary_text': 'שרי מקובר-בליקוב, מנהיגת כת החשודה בהתעללות, זוכה לכיסוי עיתונאי במתכונת של טורי זכרונות'}]
35
Your max_length is set to 3000, but your input_length is only 397. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=198)
[{'summary_text': 'הפרסום הסמוי הוא הפתרון למצוקתה התקציבית של הטלוויזיה הישראלית, אך הוא מסכן את יכולתה של התקשורת למלא את תפקידה כזירה שבה מתנהל השיח הציבורי'}]
43
Your max_length is set to 3000, but your input_length is only 592. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=296)
[{'summary_text': 'דו"ח מבקר המדינה שוב דלף לרשת לפני פרסומו הרשמי. לא כמו בפעמים קודמות, שבהן פורסם המידע על-ידי עובדי משרד מבקר המדינה, מפרסמי הדו"ח הנוכחי טרם זמנו הם גורמים שקיבלו אותו מכורח אזכורם במסמך'}]
63
Your max_length is set to 3000, but your input_length is only 2554. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1277)
[{'summary_text': 'ערוץ 10 חשף את השם ומספר הטלפון של המתלוננת פגועת הנפש בפרשת האונס הקבוצתי בירושלים. התשובה הנכונה היא 4 כמובן'}]
41
[{'summary_text': 'מטה ההסברה המשפחתי: מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים, מירוץ השליחים'}]
1728
Your max_length is set to 3000, but your input_length is only 1751. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=875)
[{'summary_text': '"ידיעות אחרונות" ממשיך לקדם את פמליית ראש הממשלה | "ישראל היום" ממשיך לקדם את פמליית רה"מ בוושינגטון | ו"מעריב" ממשיך לקדם את דיווחי הנדל"ן'}]
56
Your max_length is set to 3000, but your input_length is only 2474. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1237)
[{'summary_text': 'הבחירה בעיקרון הקולנועי-תיעודי של ראיונות וקטעי ארכיון התגלתה כבעייתית במיוחד בפרקיה הראשונים של הסדרה, שיחסם אל ההיסטוריה שסופרה בהם היה רומנטי וסנטימנטלי מזה שאפיין את הפרקים המאוחרים יותר'}]
64
[{'summary_text': 'העיתונים ממשיכים לנסות לפענח את מפגן הניתוק של העיתונות הישראלית | ב"גלובס" זורקים שאמנם יש מוצרים שהתייקרו מאוד | ב"מעריב" מנסים לשרוף את הגז כמה שיותר מהר'}]
57
[{'summary_text': 'היח"צנים ניסו לקדם את שלמה ארצי במערכת יחסי ציבור, אך לא הצליחו. העיתונות הכתובה לא הצליחה לקדם את הופעתו. היח"צנים לא הצליחו לקדם את הופעתו'}]
56
Your max_length is set to 3000, but your input_length is only 482. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=241)
[{'summary_text': '"ידיעות אחרונות" ו"מעריב" ממשיכים לנצל את תאונות הדרכים כדי לסחוט את רגשות הקוראים | "ישראל היום" ו"מעריב" מדווחים על שופט מחוזי | ו"גלובס" מקדם רכישת מוצרי צריכה'}]
62
Your max_length is set to 3000, but your input_length is only 1806. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=903)
[{'summary_text': 'שקמה ברסלר, ממובילות המחאה נגד ההפיכה המשטרית בישראל, תובעת 400 אלף שקל מתומכת נתניהו שהִדהדה את תיאוריית הקשר השקרית שלפיה ידעה מראש על טבח חמאס בתושבי הדרום'}]
58
[{'summary_text': 'ברוב של 63 מול 55 אושר הבוקר במליאת הכנסת התיקון ל"חוק יסוד: הממשלה" שנועד להכשיר את אריה דרעי לכהן כשר. הצעת החוק הפרטית של משה ארבל תאפשר לאדם שהורשע ונידון למאסר על תנאי לחזור למחרת לשולחן הממשלה, דבר שלא התאפשר עד כה'}]
82
[{'summary_text': 'העיתונים החרדיים מתמקדים בבחירות | "ישראל היום" מתמקד בבחירות | "ידיעות אחרונות" מתמקד בגדעון סער'}]
33
Your max_length is set to 3000, but your input_length is only 1445. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=722)
[{'summary_text': '"ידיעות אחרונות" ממשיך לנסות להציל את רכבת ישראל | "ישראל היום" ממשיך לנסות להציל את שר התחבורה | "מעריב" מרכין ראש עם פטירתו של דב יודקובסקי'}]
52
Your max_length is set to 3000, but your input_length is only 1111. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=555)
[{'summary_text': 'רם לנדס פוסק שהמלאכה העיתונאית בזמננו היא חסרת תכלית ונדונה מראש לכישלון. הוא הופך את אכזבתו מתפקוד עיתונאים לאידיאולוגיה'}]
45
Your max_length is set to 3000, but your input_length is only 1420. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=710)
[{'summary_text': 'עיתונאי, משורר, פזמונאי, סופר, מתרגם וסופר. היה משורר, מתרגם וסופר. כתב את "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו", "מהנעשה בעירנו",'}]
1482
Your max_length is set to 3000, but your input_length is only 1538. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=769)
[{'summary_text': 'המחאה האדירה שהתפרצה בקיץ לא הפכה כלי לניתוץ מבנה השליטה התקשורתי במדינה, ואם היתה מחאה כלפי התקשורת, היא נשמעה בשוליים והיתה חסרת שיניים'}]
45
Your max_length is set to 3000, but your input_length is only 1693. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=846)
[{'summary_text': 'העיתון הקומוניסטי בשפה הערבית. היה העיתון הערבי הראשון שהחל לציין ימי זיכרון של מאורעות חשובים בתולדות המיעוט הערבי בישראל. מייסדי העיתון היו אמיל חביבי ואמיל חביבי. מייסדי העיתון היו עורכיו, סאלם גובראן ואמיל חביבי. מייסדי העיתון היו אמיל חביבי ואמיל חביבי. מייסדי העיתון היו עורכיו, סאלם גובראן ואמיל חביבי. מייסדי העיתון היו אמיל חביבי ואמיל חביבי'}]
127
[{'summary_text': 'ההנחיות החדשות של ועדת הסחר הפדרלית האמריקאית מנסות לקדם שקיפות ולהגן על הגולשים מפני שרלטנים ורמאים'}]
34
[{'summary_text': '"ידיעות אחרונות" מציג תצלום דומה | "ישראל היום" מציג בלון ניסוי | "מעריב" מציג תמונת מראה'}]
36
Your max_length is set to 3000, but your input_length is only 1658. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=829)
[{'summary_text': 'העיתונים מדווחים על דו"ח מבקר המדינה | "ישראל היום" ממשיך לנסות לקדם קמפיין נגד הרמטכ"ל המיועד | "מעריב" ממשיך לנסות לקדם את העיתונות העברית'}]
53
Your max_length is set to 3000, but your input_length is only 2092. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1046)
[{'summary_text': 'הטרחנות לשבת על אגודות עותמניות וצביעות קואליציונית ואופוזיציונית: שרת המשפטים איילת שקד לא פועלת לתיקון העוול ואף הפילה חוקים שהציעה האופוזיציה בנושא. היא ואחרים מתנגדים לשינוי כי יש פה לחצים מטורללים מכיוון ההסתדרות על ח"כים מכל הסיעות לשמר את המצב הקיים. מביך איך כולם מאוחדים לשמר את הרעה החולה הזו, למעט כמה צדיקים דוגמת מיקי רוזנטל ועליזה לביא'}]
122
Your max_length is set to 3000, but your input_length is only 1079. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=539)
[{'summary_text': 'שני הגברים שהתיישבו זה מול זה לשיחה, באחד מימי הקיץ האחרון בווארשה, נמנים עם צמרת עולם התקשורת והתרבות בפולין'}]
36
Your max_length is set to 3000, but your input_length is only 1275. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=637)
[{'summary_text': 'הדלפות מבית המשפט העליון הן אירוע שהמילה "חריג" קטנה עליו. העיתונאים לא מבינים אם המידע הגיע ישירות לדרעי עצמו'}]
34
Your max_length is set to 3000, but your input_length is only 2366. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1183)
[{'summary_text': '"העיתונאים פיקסל, פייגל והלברשטאם מנופפים בזרועות ומציפים אותה בשאלות. שלושתם ביחד (בערבוביה) יש לך סימנים של הנאגאייקות? בואי תראי אותם? אנו רוצים פרטי פרטים, details. איך הייתה המוסקוואיות? מה הרשמים שלך? את בוודאי סבלת נורא, את שומעת, בוודאי ס ב ל ת? פיקסל: תארי כיצד התייחסו אליך כאל אסירה! פייגל: אנא ספרי על רשמייך עבור מהדורת הערב! הלברשטאם: תארי עבור מהדורת הבוקר מה הייתה האווירה בדרך חזרה! אלפרידה ריטר: רבותי, אני מודה לכם על העניין הרב, זה באמת נוגע ללב, שהווינאים האהובים שלי שמרו את אהדתם אלי. אני מודה לכם מכל הלב, שכל כך טרחתם באופן אישי". תגובה'}]
206
Your max_length is set to 3000, but your input_length is only 2698. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1349)
[{'summary_text': 'העיתונים מדווחים על מהומות דמים באוקראינה | אוקראינה עדיין בים | "ידיעות אחרונות" נגד מכירת תנובה לסינים'}]
36
Your max_length is set to 3000, but your input_length is only 733. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=366)
[{'summary_text': 'העיתונים מדווחים על אירועים פליליים בלבנון | "כל אל-ערב" ממשיך להתייחס ליום האדמה | "פנורמה" ממשיך להתייחס ליום האדמה'}]
43
[{'summary_text': 'תוכניות תחקיר בנושא צרכנות יכולות להיות תפקיד חשוב בהעצמת כוחו של האזרח מול נוכלים סדרתיים'}]
27
[{'summary_text': 'מהדורה חדשה של מפת הבעלויות בתקשורת הישראלית ממחישה את חילופי המשמרות של השנים האחרונות • המשמעות: השליט ייפול לממלכה, ונתניהו ימשיך לנסות לקדם מהלך עיתונאי • רופרט מרדוק, הארכיטיפ של טייקון תקשורת מרובה זרועות, מסביר כיצד עיתונות יכולה להיות כוח חיובי בעולם'}]
85
Your max_length is set to 3000, but your input_length is only 1294. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=647)
[{'summary_text': 'העיתונים מדווחים על אלימות גזענית בדרום תל-אביב | "ידיעות אחרונות" מתקשה להגיש לקוראים תמונת עולם מורכבת שאינה טורים "בעד" ו"נגד" | גיא מרוז ממשיך לנסות לכתוב על סלקום'}]
62
Your max_length is set to 3000, but your input_length is only 1600. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=800)
[{'summary_text': '"הטלת איסור על עורכי המוספים לשתף פעולה עם המבקשת, ולנהוג בה כבעבר, כמו לגבי כל עובדת אחרת של המשיבה, יש משום פעולה פוזיטיבית של המשיבה המביעה כוונה ברורה שלא לקיים את הצו"'}]
59
Your max_length is set to 3000, but your input_length is only 1082. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=541)
[{'summary_text': 'העיתונאים המסורתיים מנסים להוכיח את חיותה, אבל לא את חיותה. האם התקשורת המסורתית מנסה להוכיח את חיותה?'}]
39
Your max_length is set to 3000, but your input_length is only 1016. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=508)
[{'summary_text': 'יעקב כץ, יו"ר מועצת המנהלים של קבוצת ערוץ 7, משיב לשאלות בנוגע לזהות הבעלים של שניים מכלי התקשורת שייסד במו אצבעותיו'}]
43
[{'summary_text': 'שכר הח"כים יעלה השבוע בכ-1,300 שקלים. את זה אתם כבר יודעים. אבל מה היה קורה אילו הח"כים היו מקבלים את המלצת הוועדה שהם בעצמם מינו לענייני התנאים שלהם? בדקנו: השכר היה עולה במצטבר, מאז 2015, בכ-680 שקל בלבד, במקום בכ-5,300 ש"ח. הפעם ב #טרחנות_לשבת החלטנו לבדוק מה היה קורה אם הח"כים לא היו קובעים לעצמם את השכר.'}]
121
Your max_length is set to 3000, but your input_length is only 2035. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1017)
[{'summary_text': '"ידיעות אחרונות" ממשיך לעקוב אחר מותו של המדינאי המנוח | "ישראל היום" ממשיך לעקוב אחר רוגר ווטרס | "הארץ" ממשיך לעקוב אחר המהלך של פוטין'}]
50
Your max_length is set to 3000, but your input_length is only 851. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=425)
[{'summary_text': 'העיתונים מדווחים על קטילת חייל צה"ל | העיתונות העברית מפרסמת תמצית מתורגמת של דו"ח הארגון עיתונאים ללא גבולות | ו"כלכליסט" מציג תמצית מתורגמת של דו"ח הארגון עיתונאים ללא גבולות'}]
69
Your max_length is set to 3000, but your input_length is only 2429. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1214)
[{'summary_text': 'בג"ץ דחה את עתירתו נגד ראש הלשכה אילן מנוה, שהגיש נגדו כתב אישום בגין "התערבות בעניינה"'}]
38
Your max_length is set to 3000, but your input_length is only 1311. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=655)
[{'summary_text': '"מעריב" מעניק מענה לכל סוגי הקוראים | "הארץ" מעניק מענה לכל סוגי הקוראים | ו"ישראל היום" מעניק מענה לכל סוגי הקוראים'}]
40
[{'summary_text': 'כתב כאן 11 ואנשי מהדורת השבת שכחו כנראה את הפרט החשוב הזה. הם לא יכולים לבחור את מי לבקר, תפקידנו לפקח על כולם'}]
38
Your max_length is set to 3000, but your input_length is only 797. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=398)
[{'summary_text': 'העיתונים מדווחים על מעצרו של יעקב טייטל | "דה-מרקר" ממשיך לשלם על הסדר החוב | ו"ידיעות אחרונות" ממשיך לשלם על הסדר החוב'}]
47
Your max_length is set to 3000, but your input_length is only 427. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=213)
[{'summary_text': 'רועי עידן, שחקן ותסריטאי, התבטא על חוסר ההיגיון המובנה בהחלטה לסגור את תאגיד השידור הציבורי בישראל'}]
35
Your max_length is set to 3000, but your input_length is only 2160. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1080)
[{'summary_text': 'האם ערוץ 10 זכה לקידום בבחירות? האם יש סיכוי שמישהו ייגש למכרז חדש? ומה קורה עם איציק רוזנבלום, מנהל מכון "PORI", ומינה צמח, מנהלת מכון "דחף"?'}]
58
Your max_length is set to 3000, but your input_length is only 783. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=391)
[{'summary_text': 'התנועה לטוהר המידות: מינוי ממלא מקום לשירות בתי הסוהר הוא תהליך דחוף, אבל לא מוכרע. מינוי המפכ"ל נמצא על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע. מינוי המפכ"ל נמצא כל העת על סדר היום, אבל לא מוכרע'}]
836
Your max_length is set to 3000, but your input_length is only 704. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=352)
[{'summary_text': 'במדור "שאל את הרב" באתר האינטרנט של ישיבת בית־אל נדרשים הרבנים מעת לעת לענות לגולשים האלמונים על שאלות הלכתיות'}]
38
Your max_length is set to 3000, but your input_length is only 580. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=290)
[{'summary_text': 'העיתונאים מדווחים על מבצע של אייגיאן-איירליינס, שמטרתו לאפשר להם עיתונאים לזנוח את כללי האתיקה הבסיסיים ביותר. המבצע יתקיים לכל השנה הקרובה'}]
48
Your max_length is set to 3000, but your input_length is only 1914. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=957)
[{'summary_text': 'דובר צה"ל: דובר צה"ל נקמן מאוד מול כל מי שמבקר אותם. משתמשים בחומרים שהם שולטים בהם כדי לקבוע סדר יום ולחנך כתבים'}]
42
Your max_length is set to 3000, but your input_length is only 2125. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1062)
[{'summary_text': 'שלמה בן-צבי, העורך הראשי והמו"ל של "מעריב", מציג תוכנית מגירה חדשה: סגירת המהדורה היומית תאפשר להציל את העיתון, שיתבסס על מהדורת סוף-שבוע רחבה ומושקעת, לצד השקעה הולכת וגוברת בזרוע האינטרנטית של "מעריב"'}]
76
Your max_length is set to 3000, but your input_length is only 1911. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=955)
[{'summary_text': '"התיקון לחוק אינו מכיל כל מנגנון לקביעת סדר עדיפויות בין הצרכים התקשורתיים של מגזרים שונים. הוא עלול להביא למצב שבו כל התדרים הפנויים ייתפסו על-ידי תחנות המשדרות למגזר מסוים בלבד, בעוד שמגזרים אחרים, שגם להם צרכים מיוחדים, לא יזכו בתחנה כלשהי משלהם"'}]
83
Your max_length is set to 3000, but your input_length is only 1181. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=590)
[{'summary_text': 'תוכנית התרבות "המתורבתים" מציעה עמדה אחת ויחידה הזוכה לפרפרזות ולחזרות אינספור: ה"תרבות" בכללותה אינה אלא קונספירציה זדונית של המעמד השליט, ה"לבן", ה"יהודי" וה"אשכנזי" – וכל תוצריה של התרבות נבחנים אך ורק לאורה של דוֹגמה זו'}]
88
Your max_length is set to 3000, but your input_length is only 315. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=157)
[{'summary_text': 'מנכ"לית עמותת כ"ן לקידום נשים למוקדי קבלת ההחלטות: "כל עוד לא יהיה שוויון מסביב לשולחן קבלת ההחלטות לא יבואו לידי ביטוי הצרכים של החברה כולה"'}]
50
Your max_length is set to 3000, but your input_length is only 1503. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=751)
[{'summary_text': 'דו"ח ממצאים של מרכז המחקר והמידע של הכנסת על מענה לפניות הציבור בציבור: רק 26 טרחו להשיב'}]
32
Your max_length is set to 3000, but your input_length is only 1199. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=599)
[{'summary_text': 'הטלוויזיה החינוכית החליטה לוותר על שירותיה של האקדמיה ללשון העברית, אך לא את היקף העבודה ואיכותה. השרה יולי תמיר: "לא מתקבל על הדעת שבטלוויזיה החינוכית לא יהיה יועץ לשון, לפחות אחד, במשרה קבועה ומלאה"'}]
71
Your max_length is set to 3000, but your input_length is only 541. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=270)
[{'summary_text': 'רשת צומת-ספרים הודיעה כי תסיר מהמדפים את מניפסט "השמאל הלאומי" פרי עטם של שמואל הספרי ואלדד יניב. הרשת הודיעה שהיא מסירה את הספר מהמדפים בנימוק שהיא רשת עממית שלא רוצה להסתבך במחלוקות פוליטיות'}]
68
Your max_length is set to 3000, but your input_length is only 1062. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=531)
[{'summary_text': 'הפרסום ברשת הפרסום "סקס" הוא סוגיה טעונה, וחברות הפרסום מפיקות מודעות פרסום שונות נטולות תמונות נשיות עבור הירושלמים. סמנכ"ל חברת השילוט רפיד: "לא תמיד"'}]
52
Your max_length is set to 3000, but your input_length is only 1493. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=746)
[{'summary_text': 'גבי גולדמן: "נסיונות רבים לגייס חברים חדשים לוועד נתקלו בתגובות מהססות, מכיוון שאנשים חוששים מגורל דומה כשל חגי מטר"'}]
41
Your max_length is set to 3000, but your input_length is only 1857. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=928)
[{'summary_text': 'רשת ב מגישה את החדשות בשבת, אבל לא את החדשות בשבת | מדור הספורט של "ידיעות אחרונות" ממשיך לפעול | עלה תאנה ממשיך לפעול'}]
44
Your max_length is set to 3000, but your input_length is only 1813. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=906)
[{'summary_text': 'העיתונות האמריקאית עוסקת בישו, אבל לא בהכרח בביקורת על ייצוגו של הצלוב מנצרת. הביקורת על ייצוגו של ישו היא מנה הגונה של כפרנות בריאה'}]
50
Your max_length is set to 3000, but your input_length is only 683. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=341)
[{'summary_text': 'בנק הפועלים: רצף ההחלטות שסייע לממן את העיתון בתקופת עופר נמרודי התקבל לאחר בחינה מקצועית ועניינית, תוך לקיחת סיכון מחושב, וללא כל מניעים זרים'}]
49
[{'summary_text': 'כנס החירום של העיתונאים: העיתונאים הולכים ופוחתים, מילולית ומטפורית. הפוליטיקאים מנסים להשפיע על התקשורת ולכופף אותה, ובעלי הבית מחרים מחזיקים אחריהם ואף מתעלים עליהם'}]
56
Your max_length is set to 3000, but your input_length is only 411. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=205)
[{'summary_text': 'המדיניות הגורפת של כלי התקשורת היא לספק לעיתונאים שהם מעסיקים את מלוא הגיבוי המשפטי במקרה של תביעה, גם אם העיתונאי הנתבע הספיק לעזוב את מקום העבודה'}]
44
Your max_length is set to 3000, but your input_length is only 296. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=148)
[{'summary_text': 'בית-המשפט המחוזי: צווי איסור הפרסום בעידן האינטרנט תופסים מקום מרכזי בשיח הציבורי, אך לא תופסים מקום מרכזי בשיח הציבורי'}]
36
[{'summary_text': 'האם התקשורת הגזימה בביקורתה של המיליארדרית שרי אריסון? ומה קורה עם שלומי ברזל, עורך מדור הספורט ב"הארץ", ואורי שילה, מנכ"ל ההתאחדות לכדורגל?'}]
55
Your max_length is set to 3000, but your input_length is only 876. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=438)
[{'summary_text': 'ישעיהו פורת, בן דור המייסדים של עיתונות הספורט, מסביר כיצד התייחסו לעיתונאים של שנות השמונים כאל מי שלא מבינים בספורט, חסרי הכשרה, נטולי ידע, הפועלים ללא אתיקה, ללא יכולת כתיבה וללא הבנה מקצועית'}]
66
Your max_length is set to 3000, but your input_length is only 2450. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1225)
[{'summary_text': 'עיתונאי, כתב ופרשן לענייני ערבים. היה כתב ופרשן לענייני ערבים בערוץ 2, ערך והגיש במהדורת שישי של חדשות ערוץ 2, "אולפן שישי". היה גם יועץ התקשורת הראשון בשגרירות ישראל בקהיר. ערך והגיש במהדורת שישי של חדשות ערוץ 2, "אולפן שישי". היה גם יועץ התקשורת הראשון בשגרירות ישראל בקהיר'}]
99
Your max_length is set to 3000, but your input_length is only 762. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=381)
[{'summary_text': 'מחקר חדש מלמד על הקשר בין פייסבוק לעיתונות, ומציג תמונה שונה של צעירים וצעירים. פייסבוק היא שחקן מרכזי במשחק התקשורתי'}]
36
[{'summary_text': 'אמיתי זיו, כתב התקשורת של "דה-מרקר", התייחס לדברים שאמר שאול אמסטרדמסקי בראיון ל"העין השביעית"'}]
37
Your max_length is set to 3000, but your input_length is only 886. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=443)
[{'summary_text': 'העיתונות הישראלית, החלשה ואכולת רגשות האשם – זו שנתפסת בעיני חוגים רחבים בציבור כלא-פטריוטית דווקא מפני שהיא ממלאה את תפקידיה – אינה רשאית להתבשם בהישגי הפרסום. הוא נפל על ראשה בהפתעה גמורה'}]
66
Your max_length is set to 3000, but your input_length is only 684. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=342)
[{'summary_text': 'המכון הישראלי לדמוקרטיה ביטל את השתתפותו של בכיר החברה המזהמת כיל בכנס "אלי הורביץ לכלכלה וחברה" • המכון: "הנציג הוזמן כחלק מדיון רחב משתתפים בנושא קידום יזמות אקלים כמי שמובילים חממה טכנולוגית"'}]
71
[{'summary_text': 'רשות השידור היא ארגון בלתי ניתן לניהול תקין. לאורך השנים נערמו בה עיוותים ועקמומיות והשתרשו מושגים בוטים של חוסר תקינות, עד שהיתה לארגון שאין עוד דרך לשנותו'}]
50
Your max_length is set to 3000, but your input_length is only 1666. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=833)
[{'summary_text': '"ידיעות אחרונות" ממשיך לנסות לחשוף את תוכנית הגרעין האיראנית | "הארץ" מנסה להאניש את עובדי הקבלן | יאיר לפיד מתראיין אצל רז שכניק'}]
49
Your max_length is set to 3000, but your input_length is only 1225. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=612)
[{'summary_text': 'חגי רזניק, מנכ"ל משרד הבינוי והשיכון, מסביר על רקע הבחירות הקרובות: "אני חושב שנוצר פה כוח שהוא בעיקרו חברתי, שמייצר מאבק מעמדי וקידום מעמדי"'}]
52
Your max_length is set to 3000, but your input_length is only 2065. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1032)
[{'summary_text': 'מודעות האבל מתקיימות בשולי העיתונים, וכמו בתי-הקברות, גם על פניהן יהיו רבים יותר שיעדיפו לחלוף ולא להתעכב ולחוש בצינה הנושבת מהן'}]
46
[{'summary_text': 'הפגנה מול השגרירות הבריטית היתה הזדמנות לחשוף את האופן שבו הפגנה הפכה למפגן סמלי לאירוע. העיתונאים לא טרחו לבוא, המשטרה לא טרחה לבוא, המשטרה לא טרחה לבוא, המשטרה לא טרחה לבוא, המשטרה לא טרחה לבוא, המשטרה לא טרחה לבוא, המשטרה לא טרחה לבוא, המשטרה לא טרחה לבוא'}]
89
[{'summary_text': '"ידיעות אחרונות" ממשיך להעמיס על עשרות פרטי מידע ביקורתיים על התנהלות המדינה בשנים האחרונות | "ישראל היום" ממשיך להזכיר את סוד הסוד של צה"ל | "מעריב" ממשיך להציע אגנדה עצמאית'}]
59
Your max_length is set to 3000, but your input_length is only 1149. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=574)
[{'summary_text': '"הארץ" ממשיך לבקר את המשט לעזה | "דה-מרקר" ממשיך לבקר את הרפורמה בתחבורה הציבורית | עמוס הראל מצטט מקור משפטי'}]
42
Your max_length is set to 3000, but your input_length is only 968. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=484)
[{'summary_text': 'עוזרים פרלמנטריים לשעבר שלקחו את אוצר הידע שלהם מימים עברו וכעת הם משתמשים בו לטובת בעלי אינטרסים שמנסים להשפיע מבחוץ על חקיקה ורגולציה. הכל לצד שלט גדול עם סמל כנסת ישראל, שכולם נהנו להתרפק על הימים שבהם עבדו בה, ולא מולה'}]
78
Your max_length is set to 3000, but your input_length is only 2802. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1401)
[{'summary_text': 'הרשות השנייה: הטלוויזיה החינוכית נהגה במשך שנים להתעלם מחובתה החוקית לשדר תוכניות בשפה הערבית'}]
31
[{'summary_text': 'דו"ח השכר בשירות המדינה ממשיך למלא את הכותרות הראשיות | "גלובס" מקדיש את כותרתו הראשית לחשדות לניגודי עניינים של שר הביטחון אהוד ברק | ו"מעריב" ממשיך לקדם את דניאל בן סימון'}]
65
Your max_length is set to 3000, but your input_length is only 1166. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=583)
[{'summary_text': '"ישראל היום" ממשיך לספק לקורא הוגנות ומאוזן | "הארץ" ממשיך לקדם את הפרסום בעיתונות הכלכלית | "מעריב" ממשיך לנפנף בגליון "ידיעות אחרונות"'}]
55
Your max_length is set to 3000, but your input_length is only 2917. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1458)
[{'summary_text': 'יש עתיד מנסה לקדם את הצעת החוק שלו, אבל ההיסטוריה מלמדת אותנו שלא רחוק היום שבו תעלה המחלוקת בין הוועדה הציבורית לבין חברי הכנסת. טוב יעשו ביש עתיד אם יאשרו את הצעת החוק כבר עכשיו'}]
55
[{'summary_text': 'העיתונים מדווחים על התפתחות יוצאת דופן בנוגע לגידול המתמיד בפערים החברתיים | העיתונים מאמצים את עמדת הצבא בשתי ידיים | "ישראל היום" ממשיך להגן על שלדון אדלסון'}]
54
Your max_length is set to 3000, but your input_length is only 1068. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=534)
[{'summary_text': 'איתי אנגל וצבי יחזקאלי מנסים לייצר סוג בעייתי של עיתונות, המתריס נגד הרעיון של עיתונות אובייקטיבית, ניטרלית ומאוזנת'}]
43
Your max_length is set to 3000, but your input_length is only 1656. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=828)
[{'summary_text': 'עיתונאי ישראל עורכים לראשונה כנס חירום "למען תקשורת חופשית". בין מוביליו של הכנס מיטב העיתונאים, ובהם רזי ברקאי, אילנה דיין, חגי סגל, איילה חסון, עורך "הארץ" אלוף בן ועורך "מעריב" ניר חפץ'}]
73
Your max_length is set to 3000, but your input_length is only 1729. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=864)
[{'summary_text': 'יו"ר ועדת הכלכלה מיכאל ביטון הצליח לחשוף את סבך הקורים שנרקם בין ענקית הכימיקלים כי"ל לבין תושבי הדרום • במקום לנסות ולשבור את מעגל התלות הבעייתי, נציג המדינה מתייצב מול העובדים הממולכדים ומריע במגפון לחברה המזהמת • במקום לנסות ולשבור את מעגל התלות הבעייתי, נציג המדינה מתייצב מול העובדים הממולכדים ומריע במגפון לחברה המזהמת'}]
118
[{'summary_text': 'הנהלת "ידיעות אחרונות" מחזיקה בעמדה כי היא מייצגת את עיתונאי "ידיעות אחרונות" • ארגון העיתונאים: "התארגנות ראשונית פורצת"'}]
45
Your max_length is set to 3000, but your input_length is only 1174. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=587)
[{'summary_text': '"מעריב" ממשיך להתעלם מהטראומת נוחי דנקנר | "ידיעות אחרונות" ממשיך להתעלם מהטראומת יאיר לפיד | "ישראל היום" ממשיך להתעלם מהטראומת יאיר לפיד'}]
57
Your max_length is set to 3000, but your input_length is only 1387. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=693)
[{'summary_text': 'הטלוויזיה מעבירה את החיים בזרימתם. גם כאשר המצולמים אינם עוד בין החיים, הטלוויזיה מעירה אותם מתרדמתם ומראה לנו אותם כפי שהיו'}]
37
Your max_length is set to 3000, but your input_length is only 1533. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=766)
[{'summary_text': 'תושבי פרדס חנה כרכור: "התפילות ברחבי המושבה התנהלו כפי שהתנהלו לאורך השנים ובהתאם לסטטוס קוו של היישוב". במועצה טוענים כי לא נתנו לכך כל אישור. במועצה טוענים: "עשיתם את זה בלי אישור ובלי שפניתם אליהם"'}]
77
Your max_length is set to 3000, but your input_length is only 1220. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=610)
[{'summary_text': 'העיתונאים סוהא סיבאני ורוברט פרסונס העבירו את הערב הבחירות ברשת פראנס 24, בניסיון להסביר לקהל הבינלאומי את הניואנסים והמורכבויות של מערכת הבחירות בישראל'}]
48
Your max_length is set to 3000, but your input_length is only 2664. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1332)
[{'summary_text': 'יוצרי הסרט הדוקומנטרי "יבי" יפצו בכ-200 אלף שקל את התסריטאית אגי פרידמן בשל הפרת זכויות היוצרים שלה'}]
40
Your max_length is set to 3000, but your input_length is only 1258. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=629)
[{'summary_text': '"הבצל" הוא עיתון פופולרי באמריקה, שבו ניתן למצוא פודקאסטים, סרטוני וידיאו קצרים ואטלס אלטרנטיבי. "אנחנו מנוסים ובקיאים באקטואליה ולכתוב בצורה יבשה ועובדתית", אומרת מייגן גאנץ, עורכת משנה ב"The Onion". "אנשים אוהבים שעושים צחוק מדברים, עד שזה מגיע למשהו שקרוב אליהם"'}]
97
Your max_length is set to 3000, but your input_length is only 1832. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=916)
[{'summary_text': 'במשרד הכלכלה טענו במצגת פנימית שמשרד הבריאות "הקשיח עמדות" בכל הנוגע לאפשרות של כריית פוספטים על ידי כיל בשדה בריר. כעת עונים במשרד לטענות, בתגובה לפניית "שקוף" בנושא'}]
61
Your max_length is set to 3000, but your input_length is only 1673. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=836)
[{'summary_text': 'מחקר מרכז אקורד: הציבור בישראל, יהודי וערבי כאחד, חושב שהתקשורת מעניקה לחברה הערבית בישראל ייצוג גבוה פי 6 עד פי 10 משיעור הייצוג שלה בפועל'}]
46
Your max_length is set to 3000, but your input_length is only 2329. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1164)
[{'summary_text': '"הצדקה להגבלתם של תשדירי פרסומת טלוויזיוניים נובעת מכך שמדובר בכלי זמין וזול יחסית לשימוש בידי כל מפרסם, שאיכותו נתונה לביקורת עצמית בלבד ואשר הינו נגיש לצפייה בפני ציבור עצום ורב של צרכני הערוצים, אשר לא אחת מהווה "קהל שבוי""'}]
82
Your max_length is set to 3000, but your input_length is only 600. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=300)
[{'summary_text': 'העיתונות האמריקאית לא ביטאה את הפרס ללה-קלזיו, אבל היא לא ביטאה את הפרס ללה-קלזיו. צר לי על עמוס עוז, שעל-פי כל קריטריון הוא מועמד ראוי לנובל'}]
59
Your max_length is set to 3000, but your input_length is only 1723. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=861)
[{'summary_text': 'האוניברסיטה העברית תפצה את הוצאת שוקן והוצאת מוסד-ביאליק ב-300 אלף שקל'}]
28
Your max_length is set to 3000, but your input_length is only 1025. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=512)
[{'summary_text': 'גדי להב, מנהל קול-ישראל ומנהל גלי-צה"ל, הציגו את חזונם לשנים הקרובות • מנהל קול-ישראל: "אני לא מפריע לך" • מנהל קול-ישראל: "אני לא מפריע לך"'}]
54
Your max_length is set to 3000, but your input_length is only 786. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=393)
[{'summary_text': 'אייל גולן דרש מאתר החדשות ynet לשלם לו פיצויים בשל כתבה שבה צוטטה ביקורת חריפה שמתחה עליו אחינועם ניני'}]
37
Your max_length is set to 3000, but your input_length is only 2644. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1322)
[{'summary_text': 'היועץ המשפטי לוועדה ביקש מהיועץ המשפטי להציע ניסוח מרוכך שיאפשר לבג"ץ להגן על חוק כבוד האדם וחירותו. אך מבדיקת "שקוף", גם אם רוטמן יקבל נוסח מרוכך מסוג זה, כנסת עדיין תהיה אפשרות לפגוע בחלק מזכויות האדם'}]
75
Your max_length is set to 3000, but your input_length is only 2336. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1168)
[{'summary_text': 'השינוי שעשתה איקאה הוא לקראת ההאחדה המתבקשת מרשת ענקית הפונה לקהל צרכנים אוניברסלי, כך שהטקסט הייצוגי של החברה יהיה נגיש בכל מקום, בכל מדיום, ועל כל אמצעי תצוגה'}]
59
Your max_length is set to 3000, but your input_length is only 519. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=259)
[{'summary_text': '"ישראל היום" ו"ידיעות אחרונות" שולפים את ה"פחות אבל כואב" כדי לדווח על שינויים בתקציב המדינה | "ישראל היום" ו"ידיעות אחרונות" שולפים את ה"פחות אבל כואב" כדי לדווח על שינויים בתקציב המדינה'}]
64
Your max_length is set to 3000, but your input_length is only 2173. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1086)
[{'summary_text': 'מבקר המדינה קובע בדוח רשמי כי על כל איש ציבור לפרסם מדיניות למחיקת פוסטים ביקורתיים בדפיו הציבוריים, וכי חסל סדר חסימה שרירותית! השנה אספנו יחד אתכם מידע על פוליטקאים שחוסמים אזרחים בעמודי הפייסבוק שלהם - ללא אזהרה מראש, וללא כל סיבה מוצדקת. כלומר מגיבים שלא התבטאו באלימות, אלא רק העבירו ביקורת מנומסת או שאלו שאלות - אוידו מדפים שאנו מממנים באמצעות כספי מיסים. אותם גולשים נחסמו מדפים שלא דנים בהם על עיצוב הסלון, אלא על התנהלות ציבורית'}]
143
Your max_length is set to 3000, but your input_length is only 1773. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=886)
[{'summary_text': 'עיתונאי בכיר, דן מרגלית, החליט לעבוד אצל משפחת נמרודי. לכאורה מעבר נוסף של עיתונאי מעיתון אחד למשנהו, עוד תזוזה קלה בבצה התקשורתית'}]
48
Your max_length is set to 3000, but your input_length is only 1334. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=667)
[{'summary_text': 'הוועדה למדרוג לא פועלת כך, אבל היא לא מפרסמת נתונים על שיעור הצפייה לפי משקי בית. הנתונים מפורסמים בעיתונות, אבל לא בתקשורת הזרה'}]
42
[{'summary_text': 'העיתונות הכלכלית אינה שותפה למגמה הזו. העיתונות הכלכלית אינה שותפה למגמה הזו'}]
28
Your max_length is set to 3000, but your input_length is only 2545. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1272)
[{'summary_text': '"הארץ של הסופרים" חוגג את פתיחת שבוע הספר העברי | "מעריב" מעניק כותרת לשר התקשורת | "ידיעות אחרונות" מעניק כותרת ל"מעריב"'}]
49
[{'summary_text': 'הרשות השנייה: היועצים הכלכליים שגו בתחזיותיהם אינם ריאליים, אך תנאי המכרז לא היו אפשריים • ניסן שריפי: "הכשל של המכרז היה בשאלת ההגדרות"'}]
51
[{'summary_text': '"ידיעות אחרונות" ממשיך לקדם את דו"ח מבקר המדינה | "ישראל היום" ממשיך לקדם את דו"ח מבקר המדינה | יצחק לאור מראיין את קלאריס ליספקטור'}]
48
Your max_length is set to 3000, but your input_length is only 1501. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=750)
[{'summary_text': '"הארץ" ממשיך לנסות לקדם את מבקר המדינה | "ישראל היום" ממשיך לנסות לקדם את גל האלימות | "דה-מרקר" ממשיך לנסות לקדם את שוק הטלפונים הניידים'}]
51
[{'summary_text': 'יו"ר ועדת האתיקה ברשות השידור העריכה השבוע את תקבלות עבודת הוועדה לאתיקה בראשותה. "כישלון רודף כישלון", אמרה'}]
39
Your max_length is set to 3000, but your input_length is only 2057. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1028)
[{'summary_text': '"ישראל היום" מציג את יחסו של מחמוד עבאס לנתניהו | "ידיעות אחרונות" מציג אגנדה של כיף | "דה-מרקר" מציג את יחסו של לואי ד. ברנדייס'}]
54
Your max_length is set to 3000, but your input_length is only 1321. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=660)
[{'summary_text': 'בדיקת "שקוף" מגלה שרוב הח"כים בכנסת ה-24 השתתפו באופן פעיל בדיוני התקציב וחוק ההסדרים - חודשיים משמעותיים שישפיעו על החיים של כולנו בשנים הבאות. מנגד גילינו מי הח"כים שהשקיעו זמן עצום בדיונים: ולדימיר בליאק ונירה שפק מ"יש עתיד"'}]
81
Your max_length is set to 3000, but your input_length is only 2047. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1023)
[{'summary_text': 'העיתונות האמריקאית נחשבת לנושאת הדגל של העיתונות החופשית, העצמאית, שלא עושה חשבון. וודוורד וברנסטיין כבר אמרנו? אבל לא במה שנוגע ל"אינטרסים הלאומיים החשובים באמת"'}]
57
Your max_length is set to 3000, but your input_length is only 1072. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=536)
[{'summary_text': 'פרשת האסיר X: התקשורת בשפה הערבית לא מרוצה מדיווחים על נושאים בטחוניים, אלא מרוצה מדיווחים עובדתיים בלבד'}]
34
Your max_length is set to 3000, but your input_length is only 909. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=454)
[{'summary_text': 'לא כל מה שהתקשורת הישראלית מייצרת מדי יום ביומו הוא באמת אקטואלי כפי שהוא מוצג'}]
23
Your max_length is set to 3000, but your input_length is only 934. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=467)
[{'summary_text': 'ארגון השחקנים: קופרמן-הפקות עומדת בכל דרישות שח"ם ומעסיקה מאות שחקנים בהתאם לתעריפים שנקבעו ואף למעלה מכך'}]
37
Your max_length is set to 3000, but your input_length is only 1309. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=654)
[{'summary_text': 'מנכ"ל התנועה לטוהר המידות עומר מקייס: "קמפיין מימון ההמונים להגנתו של ראש האופוזיציה חושף את האבסורד שבאי הקמתה של ועדת האתיקה בכנסת"'}]
52
Your max_length is set to 3000, but your input_length is only 1982. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=991)
[{'summary_text': 'פרויקט ביג דאטה של אנדי וורמס, שמטרתו להנגיש בצורה פתוחה וגולמית נתונים על הנעשה בבתי-המשפט בישראל, מציג מידע על התיקים המשפטיים הנידונים בבתי-המשפט ברחבי הארץ'}]
55
Your max_length is set to 3000, but your input_length is only 720. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=360)
[{'summary_text': 'דו"ח של עמותת הצלחה על פרשת ההתנצלות של ערוץ 10: לא מדובר על אירוע חד-פעמי, רמיזה או תהליך אגבי, אלא מדובר על מהלך שהונע לא מכיוון הגורמים המקצועיים בחברת החדשות, אלא מגורמים שונים בעלי תפקידים שונים בערוץ'}]
66
[{'summary_text': 'רגב גולדמן, כתב המקומון של "מעריב", מבטיח כי הפרטים המלאים על פיצוץ מטען החבלה יגיעו לגיליון הקרוב של "זמן חולון-בתים"'}]
45
Your max_length is set to 3000, but your input_length is only 1418. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=709)
[{'summary_text': 'העיתונים מדווחים על דו"ח האו"ם | "מעריב" ממשיך להוביל את הגישה המיליטנטית כלפי הדו"ח | ו"ישראל היום" ממשיך להגיב'}]
44
Your max_length is set to 3000, but your input_length is only 2405. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1202)
[{'summary_text': 'כאשר הרשת תופס את מקומה המרכזי כאמצעי להעברת מסרים רשמיים וכאמצעי שכנוע דיפלומטי, אפשר להניח בביטחון כי השלב הבא הוא הכרה רחבה היקף ברשת כמקור רשמי להעברת מסרים והחלפת דעות'}]
60
Your max_length is set to 3000, but your input_length is only 1616. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=808)
[{'summary_text': 'מהדורה מרכזית של חדשות ערוץ 2 מזכירה את מהדורה אחרת של המגזין השבועי של חברת החדשות, "אולפן שישי"'}]
37
Your max_length is set to 3000, but your input_length is only 1297. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=648)
[{'summary_text': 'אוניברסיטת בן גוריון בנגב עשויה לשנות את מדיניותה ולחשוף את היקף התרומות שהיא מקבלת מחברת כי"ל. בעוד היקף התרומות המלא עדיין לא ידוע, בפרט אחד דווקא מתגאים באוניברסיטה'}]
55
[{'summary_text': 'רעייתו של יו"ר הכנסת התלוותה לכל טיסה בשנה האחרונה. עלות הכרטיסים של מזכירת הכנסת היתה כ-24 אלף שקל. בלשכתו של יו"ר הכנסת הדגישו כי הנסיעה מוסדרת בנוהל והסבירו ש"בדומה לרעיית הנשיא ורה"מ, לרעיית יושב ראש הכנסת יש תפקיד משמעותי וחשוב בביקורים מדיניים רשמיים"'}]
94
Your max_length is set to 3000, but your input_length is only 847. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=423)
[{'summary_text': '"ידיעות אחרונות" ממשיך לבקר את התקשורת העולמית | "ישראל היום" ממשיך לבקר את בנימין נתניהו | גוזף שטיגליץ מסביר את מחיר האי-שוויון'}]
44
[{'summary_text': 'ב"העין השביעית" דיווח איתי רום על עתירה לבג"ץ בדרישה כי לשכת העיתונות הממשלתית תשנה את הקריטריונים להענקת תעודות לעיתונאים העובדים באתרי אינטרנט'}]
52
Your max_length is set to 3000, but your input_length is only 894. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=447)
[{'summary_text': '"ישראל היום" מעניק במה למצדדים בשחרור האסירים | "ידיעות אחרונות" מעניק במה למשפחות השכולות | סבר פלוצקר מסביר כיצד ניתן לקבוע כי לא מדיניות ממשלתית מודעת אחראית לשיעור העוני הגבוה בישראל'}]
61
Your max_length is set to 3000, but your input_length is only 1629. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=814)
[{'summary_text': 'ממשלת ה"שינוי" דחתה סופית היום הצעת חוק לשקיפות בהצהרות הון של ראשי המפלגות • במפלגה שמוביל יאיר לפיד מאמינים כי המציאות הנוכחית מספקת מידע אישי ולאור צנעת הפרט מספיק שמבקר המדינה יפקח על ניגודי עניינים ונושאים פיננסיים במהלך כהונת נבחר ציבור'}]
82
Your max_length is set to 3000, but your input_length is only 2022. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1011)
[{'summary_text': 'הדיון בוועדת הפנים בוועדת הפנים: 47 בעד 41 נגד - החוק הפרסונלי של ח"כ עמית הלוי עבר בקריאה ראשונה במליאה. ברוב של 47 בעד מול 41 נגד. חברי הקואליציה הצביעו בעד כנגד ארבעה מחברי הוועדה מטעם האופוזיציה'}]
81
Your max_length is set to 3000, but your input_length is only 2913. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1456)
[{'summary_text': 'העיתונאי יריב לוין הגיש תביעת סרק חסרת בסיס: "בניגוד לטענותיו חסרות השחר וחסרות כל בסיס עובדתי של התובע – במהלך כל שנות עבודתו בידיעות הוא נהנה מתנאי ההעסקה שסוכמו עימו"'}]
59
Your max_length is set to 3000, but your input_length is only 2119. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1059)
[{'summary_text': 'בדיקת "יפעת מחקרי מדיה" מגלה כי התקשורת חזרה על חטאיה הקודמים • הטיה כמותית לטובת גוש המפלגות המתנגדות לנתניהו, המתיישבת עם ההטייה המסורתית, שהתקיימה גם במערכת הבחירות הנוכחית, לטובת פוליטיקאים המכהנים בממשלה'}]
75
[{'summary_text': 'העיתונים מתכוננים לחילופין עם חמאס | בן כספית מנסה לרמוז לקוראיו | ו"דה-מרקר" ממשיך לנסות לחשוף ידיעה תמימה'}]
46
[{'summary_text': '"ידיעות אחרונות" משיק קמפיין לשיקום תדמיתו | "ישראל היום" ממשיך להרוס את העדות האישית של בנימין נתניהו | "הארץ" ממשיך להרוס את דוכן העיתונים'}]
50
Your max_length is set to 3000, but your input_length is only 1804. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=902)
[{'summary_text': '"ידיעות אחרונות" ו"ישראל היום" מדווחים על מבצע אחמדינגאד | "הארץ" מציג תצלום עיתונאי מוצלח במיוחד | "מעריב" מציג ידיעה על יום הולדתו של סילבן שלום'}]
56
[{'summary_text': 'הצעת חוק חדשה מנסה להרחיב את האפשרות של חושף שחיתות להגיש תביעות בבתי הדין לעבודה, גם אחרי שמבקר המדינה יסיים את הטיפול בעניינם • הבעיה: המשרד לא שלח נציגים לישיבה, ומשרד המבקר לא שלח נציגים לישיבה'}]
67
Your max_length is set to 3000, but your input_length is only 514. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=257)
[{'summary_text': 'וולטר סוריאנו הגיש תביעות נגד עיתונאים, עיתונאים ועיתונאים בשל פרסום שקרים על אודותיו • השופט רונן דחה את תביעת סוריאנו ועו"ד בומבך על כל טענותיו • השופט רונן: "הנתבעים עשו מאמץ ניכר להפיס את דעת סוריאנו"'}]
78
Your max_length is set to 3000, but your input_length is only 586. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=293)
[{'summary_text': 'אתר "ידיעות אחרונות" מבית "ידיעות אחרונות" ממשיך לדווח על עדותה של רעיית ראש הממשלה בבית-הדין לעבודה בירושלים • בדף הבית של ynet הגיעו ההפניה לדיווח על העדות עד לכותרת השנייה בחשיבותה בלבד'}]
60
Your max_length is set to 3000, but your input_length is only 2278. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1139)
[{'summary_text': 'שיטוט אקראי באתר הישראלי של חברת כי"ל עלול ליצור את הרושם שמדובר בארגון חדש שכל ייעודו שמירה על הסביבה'}]
33
Your max_length is set to 3000, but your input_length is only 1003. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=501)
[{'summary_text': 'העיתונות האמריקאית מנסה להפיל את הרעיון הגדול הבא של גונה לרר, אבל לא מצליחה להפיל אותו'}]
28
Your max_length is set to 3000, but your input_length is only 2260. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1130)
[{'summary_text': '"העותרות מבקשות צו על תנאי המורה למשיב 1 לנמק מדוע לא יעניק להן, באמצעות משיבות 6-3, היתר לכלול פרסומת ישראלית בשידורי הערוץ"'}]
50
[{'summary_text': 'העיתונים מדווחים על פרשת המרגל במצרים | "הארץ" ממשיך להגיב לעיתונאים | "ידיעות אחרונות" מציג ספר לילדים'}]
37
[{'summary_text': 'עיתונאים שבדרך כלל אוהבים להציג את עצמם כמשקיפים אובייקטיביים מן הצד הופכים לפתע לחסידיהם של עובדי סיוע כאשר הם נתקלים באסונות הומניטריים'}]
47
[{'summary_text': 'העיתונים מדווחים על מינויו של יוחנן דנינו למפכ"ל המשטרה | "ישראל היום" ממשיך לנסות לקדם את הרפורמה | "ידיעות אחרונות" ממשיך לנסות לקדם את המהלך'}]
54
[{'summary_text': 'העיתונים מדווחים על המאורעות בסוריה | "כל אל-ערב" מגיב לשופט סלים גובראן | "פנורמה" מצטט את עורך "פנורמה"'}]
44
[{'summary_text': 'העיתונים הכלכליים מדווחים על פרשת פסגות | "ידיעות אחרונות" ממשיך לנסות להסביר את התערבות שרה נתניהו בענייני המדינה | סבר פלוצקר ממשיך לקעקע את קדימה פלוצקר'}]
54
Your max_length is set to 3000, but your input_length is only 2883. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1441)
[{'summary_text': 'בני ציפר, הבלוגר הסורר של "מעריב", ממשיך לשחק את דמותו החתרנית, אבל ללבי מתגנב החשש שהוא עומד להיכשל בניסוי התקשורתי המזהיר שהוא עורך'}]
48
Your max_length is set to 3000, but your input_length is only 1574. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=787)
[{'summary_text': '"ידיעות אחרונות" ממשיך לדווח על תקרית אש בדרום | "ישראל היום" ממשיך לדווח על הגרעין האיראני | ניר חפץ ממשיך להציל את "מעריב"'}]
47
Your max_length is set to 3000, but your input_length is only 1211. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=605)
[{'summary_text': 'יו"ר הכנסת אמיר אוחנה הודיע על הקמת ועדת האתיקה בכנסת ה-25, לאחר שלא פעלה ברציפות בשנים האחרונות • כעת יעמדו בפניה שורה ארוכה של סוגיות • נושאים נוספים הם קידום חברות מסחריות, החלטה על מימון טיסות לחו"ל - והנושא הנפיץ ביותר - גיוס כספים למימון משפטו של נתניהו'}]
90
Your max_length is set to 3000, but your input_length is only 903. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=451)
[{'summary_text': 'החברות המכובדות והמהוגנות האלה מפעילות מערכות של שקר שיטתי, שמעל ראשן מתנוססת הכותרת השקרית מכולן: "שירות לקוחות". החברות האלה – והאירוניה העצובה היא שחברות התקשורת הן כנראה המובילות בכך – מחנכות מאות או אלפי צעירים שהתגובה הראשונה לתלונה של לקוח היא שקר'}]
80
Your max_length is set to 3000, but your input_length is only 1685. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=842)
[{'summary_text': 'בג"ץ הורה לרשות השידור להעביר לארגוני היוצרים דיווחים קבועים על היקף התקשרותה להפקת הפקות מקומיות בשנים הקרובות'}]
37
Your max_length is set to 3000, but your input_length is only 1164. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=582)
[{'summary_text': 'דן כספי מסביר כיצד התקשורת הישראלית מסקרת את הרצח בבר הנוער, אבל לא את הומופוביה, אלא את החוסר הבנה המשווע של הקהילה'}]
41
Your max_length is set to 3000, but your input_length is only 233. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=116)
[{'summary_text': 'המדינה ערערה לבית המשפט העליון על שלילת חירות "בוטה ומשוללת יסוד" של אזרח מעורב שמבקש לפעול באופן חיובי ובדרכי שלום למען שלטון החוק, המשטר הדמוקרטי, טוהר המידות, זכויות האדם והדיאלוג עם אזרחים ששייכים לציבור שתפיסת עולמו שונה לא אחת משלו'}]
77
Your max_length is set to 3000, but your input_length is only 1153. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=576)
[{'summary_text': 'נעמי נידם, העורכת הראשית של "שקוף", התארחה בתכנית "הצינור" של גיא לרר וסיפרה על פרויקט העיתונות העצמאית ברשתות המקומיות'}]
45
Your max_length is set to 3000, but your input_length is only 895. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=447)
[{'summary_text': 'הכותבים נגד שיתופו של עבריין מין מורשע בתוכנית ריאליטי לא מצאו פתרון חלופי עבור המבקרים, אלא ניסו למנוע את הופעתו'}]
40
[{'summary_text': 'שני שידורי הספורט היוקרתיים שעלו בתחילת אוקטובר בערוץ החדש שבו והוכיחו את מה שיש לקוות שמימן כבר ידע: אין קיצורי דרך'}]
41
Your max_length is set to 3000, but your input_length is only 1784. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=892)
[{'summary_text': '"ידיעות אחרונות" ו"מעריב" מדווחים על מותו של חייל צה"ל | אמנון לורד קורא לשינוי גישה | "ישראל היום" ממשיך לסקר את קריסת "מעריב"'}]
52
[{'summary_text': 'השופט אישר את הקפאת ההליכים של "מקור ראשון המאוחד" ו"מקור ראשון" אך דחה חלקים אחרים מבקשת ההקפאה'}]
35
Your max_length is set to 3000, but your input_length is only 518. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=259)
[{'summary_text': 'הבחירות לרשויות המקומיות: כניסה של גוף שלטוני לשדה התקשורת במטרה לצבור הון פוליטי'}]
27
[{'summary_text': 'גון סטיוארט, מנחה ה"דיילי שואו" בערוץ קומדי-סנטרל, הוא הסטיריקן המצליח והמפורסם ביותר בארה"ב. סקרים ומחקרים טענו כי התוכנית בהגשתו שקולה למשדרי חדשות רגילים מבחינת היקף המידע המוצע לצופים, וכי עבור נתח גדול של צופי הטלוויזיה האמריקאית היא משמשת ספק המידע העיקרי של אקטואליה'}]
94
Your max_length is set to 3000, but your input_length is only 1357. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=678)
[{'summary_text': '"ידיעות אחרונות" נלחם בתושבי האיטי | "ישראל היום" מפרסם ידיעה גדולה | "גלובס" מגיש קובלנה פלילית'}]
37
[{'summary_text': 'הניסיון לעמוד על טיבו של העימות בין יוצר הסרט התיעודי "ממלכת הסוד", ניר טויב, ובין הצנזורית הראשית סימה ואקנין-גיל טומן בחובו מלכוד'}]
50
Your max_length is set to 3000, but your input_length is only 903. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=451)
[{'summary_text': 'העיתונות האמריקאית מתמודדת עם תהום, או התהום, במלחמת הבחירות בין הרפובליקאים לדמוקרטים'}]
33
[{'summary_text': 'השופטת דליה דורנר: העיתונות מפירה את חוק הסוביודיצה באופן קבוע וביודעין, אך קראה להימנע מחקיקת כל חוק נוסף המגביל את חופש העיתונות'}]
45
[{'summary_text': '"לא זו בלבד שההדלפה, היא לבדה, הינה גורם שיש לטפל בו ולעוקרו מן השורש, אלא אם כן היא נעשית למטרת חקירה או למטרה הגונה אחרת"'}]
47
Your max_length is set to 3000, but your input_length is only 707. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=353)
[{'summary_text': 'העיתונים מתכוננים למלחמת התשה | "מעריב" ממשיך לנסות למנוע פרסום חומר חסוי | ו"ידיעות אחרונות" ממשיך לנסות לדווח על תופעות עומק בחברה'}]
49
[{'summary_text': 'רון בן-ישי, עורך מהדורת "מבט", על דן סממה, כתב הערוץ הראשון ועורך מהדורת "מבט" לשעבר'}]
35
Your max_length is set to 3000, but your input_length is only 2792. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1396)
[{'summary_text': 'העיתונים מדווחים על עימות מדיני עם ארה"ב | צה"ל ממשיך לצאת למבצעי מעצרים בערים | ו"הארץ" מסביר כיצד ייתכן שישראל תוכל לצאת למבצעי מעצרים בשטחים'}]
59
Your max_length is set to 3000, but your input_length is only 925. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=462)
[{'summary_text': '"מעריב" מדפיס מחדש תצלום של משפחת חיימוב | "ישראל היום" ממשיך לנסות לקדם את דעת הקהל | "גלובס" ממשיך לקדם את ועדת בכר'}]
45
Your max_length is set to 3000, but your input_length is only 568. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=284)
[{'summary_text': 'חוק הכנסת מעודכן: יו"ר האופוזיציה יהיה ראש הסיעה הגדולה בכנסת שאינה חברה בממשלה • בכנסת ה-21 לא הוקמה ממשלה וכך מאז הבחירות האחרונות ועד שממשלה תוקם אחרי הבחירות הבאות - לא מכהן יו"ר אופוזיציה בישראל • גנץ: "לא קיבלנו תדרוך מרה"מ"'}]
83
Your max_length is set to 3000, but your input_length is only 1287. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=643)
[{'summary_text': 'תוכנית החדשות "מה קורה" המשודרת בערוץ 2 מצהירה על עצמה כ"תוכנית החדשות הראשונה שבה הקהל עורך את הכותרות"'}]
37
Your max_length is set to 3000, but your input_length is only 170. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=85)
[{'summary_text': 'ראש מטה המתנדבים הארצי של הליכוד: מפלגת הליכוד שומרת נתונים אישיים על אזרחים, יתכן כי באופן מפר חוק • דובר הליכוד: "אנחנו צריכים אתכם" • דובר הליכוד: "אנחנו צריכים אתכם"'}]
62
Your max_length is set to 3000, but your input_length is only 2535. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1267)
[{'summary_text': 'עיתונאי, חבר הכנסת השלישית, הרביעית והחמישית. היה חבר הכנסת השלישית, הרביעית והחמישית. היה חבר הכנסת השלישית, הרביעית והחמישית. נפטר ב-2001 בתל אביב "הכול פוליטי", עמוס כרמל, דביר'}]
66
Your max_length is set to 3000, but your input_length is only 2031. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1015)
[{'summary_text': 'יואב יצחק ממשיך לחשוף את מקורו של אמנון אברמוביץ, אך לא מרוצה מהאופן שבו הוא מסביר את האופן שבו סיקר את החלק שייחס לבניהו בפרשה'}]
46
[{'summary_text': 'פורום נאמני העצים של ירוחם מנסה לקדם את הצל בעיר המדברית, בשכונות החדשות וברחובות הוותיקים • "הרצון העקרוני הוא לשתף ולשמוע ואיפה שניתן – לממש", אומר איתן דלח, יו"ר ועדת הסביבה של העיר, חבר המועצה איתן דלח • "התושבים התחברו וגם המועצה וזה נהיה נושא מדובר"'}]
91
Your max_length is set to 3000, but your input_length is only 1619. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=809)
[{'summary_text': '"ישראל היום" ממשיך לנסות לחשוף את המלחמה בעזה | "הארץ" ממשיך לנסות לחשוף את המלחמה בעזה | ו"גלובס" ממשיך לנסות לחשוף את המלחמה בעזה'}]
52
Your max_length is set to 3000, but your input_length is only 880. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=440)
[{'summary_text': 'תחזיות העיתונאים על המשבר הכלכלי מבלבלות, אבל לא מצליחות להסביר את התוצאה'}]
25
[{'summary_text': 'ארגון "פרטיות ישראל" הגיש דרישה רשמית כי יחדול מאיסוף מידע על בוחרים ללא הסכמתם ואף ימחוק כל מידע שנאסף בדרך זו. הדרישה חריגה בייחוד משום שלא מדובר בעבודת שטח בקמפיין "יש עתיד" אלא בהשגחה על טוהר הבחירות'}]
69
[{'summary_text': 'העיתונים מדווחים על פשעי רצח סדרתיים | "ישראל היום" ממשיך לנסות לקדם את נתניהו | רפרם חדד שוחרר אל המולה התקשורתית'}]
42
Your max_length is set to 3000, but your input_length is only 2173. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1086)
[{'summary_text': '"פרסומם של שלושת הקטעים נשוא התובענה ברשימה "מסדר הצדקנים" היה בלתי ראוי ובלתי נחוץ, מה גם שהיוו חזרה על הדברים שפורסמו כבר ברשימות קודמות, פרי עטו של הנתבע על כן איני עושה צו להוצאות"'}]
62
Your max_length is set to 3000, but your input_length is only 814. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=407)
[{'summary_text': 'שלמה שרף מתנצל בפני הקוראים על אי-הנעימות | ערוץ 9 ממשיך לשלם את זכויות השידור שלו | ו"ידיעות אחרונות" ממשיך לשלם את המחיר'}]
44
Your max_length is set to 3000, but your input_length is only 2540. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1270)
[{'summary_text': 'עיתונאי, מנכ"ל קול-ישראל, מנהל קול-ישראל, מנכ"ל ערוץ 2, מנכ"ל גלי-צה"ל, מנכ"ל ערוץ 2, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל, מנכ"ל קול-ישראל'}]
1014
Your max_length is set to 3000, but your input_length is only 2482. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1241)
[{'summary_text': 'הזלזול בייחוס למקורות מידע הוא אחת הרעות החולות של העיתונות הישראלית. הזלזול בייחוס למקורות מידע הוא אחת הרעות החולות של העיתונות הישראלית'}]
40
[{'summary_text': 'העיתונאים והציבור בבריטניה משוכנעים שההודעות על מותו של הספין אלסטייר קמפבל הן ספין נוסף בלבד'}]
33
Your max_length is set to 3000, but your input_length is only 434. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=217)
[{'summary_text': '"מעריב" ממשיך לנסות לקדם את יאיר לפיד | "הארץ" ממשיך לנסות לקדם את חוק המסתננים | "ישראל היום" ממשיך לנסות לקדם את מיט רומני'}]
48
Your max_length is set to 3000, but your input_length is only 950. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=475)
[{'summary_text': 'מרכז הקניות "ריבר פארק סקוור" בעיר ספוקיין במדינת וושינגטון בארצות־הברית לא היה סיפור הצלחה מאז שהוקם, בשותפות בין העירייה לחברה פרטית'}]
47
Your max_length is set to 3000, but your input_length is only 1339. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=669)
[{'summary_text': 'העיתונים מדווחים על מותו של רוגר איברט, העיתונאים מנסים להפוך את האינטרנט לרשת חברתית, ועוד חדשות תקשורת מהרשת העולמית'}]
38
Your max_length is set to 3000, but your input_length is only 2184. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1092)
[{'summary_text': 'ממשלת ישראל לקחו לנו מהכיס 22 מיליארד שקל. כחלון ונתניהו יעבירו אותם גם לגמלאי השוטרים והסוהרים - כפיצוי על כך שיום אחד עלולים לפטר אותם ולא תהיה להם עבודה אחרת'}]
53
Your max_length is set to 3000, but your input_length is only 1930. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=965)
[{'summary_text': 'העיתונים מדווחים על כישלון בתקציב | סבר פלוצקר מציג גישה אוהדת | ו"מעריב" מוציא צו סגירה לעורך תחבורה'}]
41
Your max_length is set to 3000, but your input_length is only 2190. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1095)
[{'summary_text': 'החשד שלפיה דודו טופז עומד מאחורי התקיפה האלימה של בכירי ערוץ 2, אבי ניר ושירה מרגלית, מעורר מחדש את השאלה אם האלימות מפעפעת אל עולם העיתונות, ואם העיתונאי הישראלי איבד את ההגנה הבלתי נראית שאמורה לעטוף אותו מתוקף תפקידו ולאפשר לו לבצע את עבודתו בלא מורא ובלי משוא פנים'}]
94
Your max_length is set to 3000, but your input_length is only 798. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=399)
[{'summary_text': 'היומרה לייצר פרחי מדינאות והסברה לאומית באה ממניעים רחבים יותר משכלול התוכנית כשלעצמה'}]
30
Your max_length is set to 3000, but your input_length is only 537. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=268)
[{'summary_text': 'המפגש בין מהדורת החדשות המרכזית של ערוץ 2 ובין תוכנית הבידור המרכזית של ערוץ 2 הניב שפל חדש בתהליך הכניעה של החדשות בפני הבידור'}]
44
Your max_length is set to 3000, but your input_length is only 282. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=141)
[{'summary_text': 'המפגש בין קהל מצוין שאכפת לו לבין מרצים מרתקים ומגוונים ששיתפו מהידע והניסיון שלהם. הם קראו לבאים לעשות מעשה- להתפקד, לתרום לעיתונות עצמאית ולהצטרף לכלבי השמירה האזרחית. המרצים יודעים מה הם אומרים, ואם לא באתם – כדאי לכם לקרוא באדיקות'}]
80
Your max_length is set to 3000, but your input_length is only 1230. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=615)
[{'summary_text': 'גד פרץ: מנכ"ל משרד התקשורת אמר את הדברים ביום ד, אך לא אתמול. אתר הכנסת: אין תגובה'}]
28
[{'summary_text': 'החקירה הפוליטית של אביגדור ליברמן היא מיותרת. התוצאות שלה כתובות מראש במפת הדמיון הפוליטי שלנו, שבה אין שום סימטריה בין ימין לשמאל'}]
45
Your max_length is set to 3000, but your input_length is only 1435. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=717)
[{'summary_text': '"ישראל היום" ממשיך לנסות לפענח את ההסכם | אמנון לורד מבקר את אובמה | ו"ידיעות אחרונות" מבקר את צרלס קראוטהמר'}]
43
Your max_length is set to 3000, but your input_length is only 1663. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=831)
[{'summary_text': 'ב-ynet מדווחים על מציאות זרה, ב-ישראל היום מדווחים על מציאות זרה, ב-ישראל היום מדווחים על מציאות זרה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ישראל היום מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-ynet מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה, ב-הארץ מדווחים על קצח בקלנסווה, ב-nrg מעריב מדווחים על קצח בקלנסווה'}]
1422
Your max_length is set to 3000, but your input_length is only 1768. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=884)
[{'summary_text': 'שיתוף הפעולה המסחרי בין "הארץ" לאוניברסיטת בר-אילן ממשיך לעורר מחלוקות עיתונאיות, אך המחלקה המסחרית של האתר מנסה למכור למפרסמים לא רק מודעות, אלא גם את המותג עצמו'}]
56
[{'summary_text': 'העיתונות העברית אינה מתכוונת לנסות אפילו להחכים אותנו בעניין המדינה המתקראת "ירדן", על משטרה המדיני, חוקיה, יחסה לדת או סוג הכלכלה הנהוג בה'}]
45
Your max_length is set to 3000, but your input_length is only 2582. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1291)
[{'summary_text': '"ישראל היום" מציג את יאיר לפיד כנבל | "מעריב" מציג את יעל גרמן כנבל | "ידיעות אחרונות" מציג את שרה נתניהו כנבל'}]
43
[{'summary_text': 'ההתמודדות של חברה מודרנית עם המשמעויות התרבותיות והחברתיות של טלוויזיה מסחרית, של גלובליזציה תקשורתית ושל סגידה לרווחים ודיבידנדים היא עניין חוצה יבשות'}]
49
Your max_length is set to 3000, but your input_length is only 1538. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=769)
[{'summary_text': 'מזג האוויר חורפי, אבל לא כל יום | "מעריב" מדווח על צילומים עצמיים של פוליטיקאים | "ידיעות אחרונות" מציג תמונה של נוחי דנקנר'}]
45
Your max_length is set to 3000, but your input_length is only 1770. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=885)
[{'summary_text': 'פרויקט "מפת המזהמים" של שקוף מבקש לחשוף את הגורמים המזהמים בארץ, אבל לא פחות חשוב, להגביר את הקולות של אלה שסובלים ממנו'}]
40
Your max_length is set to 3000, but your input_length is only 579. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=289)
[{'summary_text': 'אורי בלאו והכתבת לשעבר שי גרינברג מבקשים מבית-המשפט לבטל את כתב האישום שהוגש נגדם בגין הסגת גבול'}]
37
Your max_length is set to 3000, but your input_length is only 653. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=326)
[{'summary_text': 'ארגון העיתונאים: מעברם של עובדי "פנאי פלוס" למערכת ynet אינו מסמן מיזוג צפוי בין שני כלי התקשורת, אלא את הקמתו האפשרית של אתר אינטרנט חדש'}]
43
[{'summary_text': 'סילבן שלום חגג את יום הולדתו, אבל כבר אתמול הזדמנה לו הפתעה נעימה. בשער האחורי של "מעריב" הופיעה ידיעה שכותרת המשנה שלה הודיעה: "חוגגים מחר יום הולדת? אתם בחברה טובה"'}]
64
Your max_length is set to 3000, but your input_length is only 733. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=366)
[{'summary_text': '"ישראל היום" ממשיך לחנך את קהל הקוראים | "ידיעות אחרונות" ממשיך לחשוף את פרטים מעוררי תהייה על מוטי בן-משה | "ממון" ממשיך לחשוף את חקירת נוחי דנקנר'}]
61
Your max_length is set to 3000, but your input_length is only 1650. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=825)
[{'summary_text': 'ישנם עיתונאים שבעבורם אירוע חדשותי הוא סיבה מספקת ליום של חג, אבל לא סתם חג כי אם חג הפסח, הוא חג החירות'}]
41
[{'summary_text': 'עוזי בנזימן מנסה להציג את עצמו כילד שמזהה שהמלך עירום. הגישה המסכנת והמניפולטיבית של העיתונאים'}]
35
[{'summary_text': 'העיתונות הימנית מנסה לקדם את תוכנית ההתנתקות, אולם בחודשים האחרונים היא מאוחדת בהתגייסותם המוחלטת למאבק נגד מימושה'}]
38
Your max_length is set to 3000, but your input_length is only 1644. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=822)
[{'summary_text': '"ישראל היום" ממשיך לנסות לקדם את גלעד שליט | "ידיעות אחרונות" מקדם ספר חדש על אביו | "הארץ" מקדם ספר חדש על גלעד שרון'}]
44
Your max_length is set to 3000, but your input_length is only 1591. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=795)
[{'summary_text': 'הטלוויזיה האמריקאית מציעה לציבור הצופים טראש מרוכז. חבורה של גברים ונשים שמוכנים לעשות הכל מול המצלמה רק כדי לזכות בקצת חשיפה טלוויזיונית ואולי גם בקצת מזומנים'}]
50
Your max_length is set to 3000, but your input_length is only 2487. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1243)
[{'summary_text': 'אגודת העיתונאים: ארגון העיתונאים מביע אי-אמון בהצהרות הנהלת העיתון, אך מקיים מערכת יחסים ארוכה עם ההנהלה'}]
38
[{'summary_text': '"אני לא יודע אם הוא משפיע. אין פה אקדח מעשן. מעורבות מן הסוג הזה היא הרבה יותר דקה" • מרגוליק, העיתונאי הוותיק של "ניוזוויק", על יחסו של שלדון אדלסון לנתניהו • "הסיפור שלי לא מסתמך רק על עיתונאים, והאמת היא שנתניהו צודק בכך שהעיתונות היא מאוד שמאלית או מאוד ליברלית"'}]
96
Your max_length is set to 3000, but your input_length is only 1379. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=689)
[{'summary_text': 'העיתונים מדווחים על שחרורו של אילן גרפל | "ידיעות אחרונות" ממשיך לנסות לקדם את הדיון האופרטיבי והמדיני על אפשרות התקפה צבאית ישראלית על מתקני הגרעין של איראן'}]
54
Your max_length is set to 3000, but your input_length is only 2743. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1371)
[{'summary_text': 'קריירה מופלאה שעושה עיתונאי מנכונותו להפנות גב לחבריו, להתעלם ממחויבויותיו המוסריות, להחליף נאמנויות ולשנות עמדות'}]
40
Your max_length is set to 3000, but your input_length is only 1953. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=976)
[{'summary_text': 'מחקר חדש של סי. וו. אנדרסון מלמד על השפעתו של המידע הסטטיסטי על דפוסי העבודה העיתונאית. הנתונים מראים כי העיתונאים יכולים לעמוד לראשונה על טעמיהם של צרכני התקשורת ולספק את רצונותיהם, אבל טמונה בכך גם בעיה'}]
67
[{'summary_text': 'הטכנולוגיה הדיגיטלית מאפשרת קשר הידודי בין הצופה לחברת השידור, אבל מרגע שמאגר המידע הזה יהפוך למסד לקבלת החלטות ויועבר גם למפרסמים ולפרסומאים, עלולות לצוף בעיות חמורות בתחום הבטחת הפרטיות'}]
59
Your max_length is set to 3000, but your input_length is only 1428. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=714)
[{'summary_text': '"ידיעות אחרונות" מעניק יחס מתלקק לבעלי הון | "מעריב" ממשיך ללוות את משפחת שפירא | גו קונפינו מסביר כיצד בחר לצאת בקמפיין ערכי הסובב מושגים כמו יושר, שקיפות ותחושת שליחות'}]
63
Your max_length is set to 3000, but your input_length is only 964. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=482)
[{'summary_text': 'סגן שר האוצר לשעבר ח״כ מיקי לוי פעל למען "חוק המלט" המטיב לכאורה עם ענקית המלט "נשר" - בניגוד להסכם ניגוד העניינים עליו חתם'}]
48
Your max_length is set to 3000, but your input_length is only 2822. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1411)
[{'summary_text': 'בית-המשפט חייב את חברת אחים-נסטל לשלם 120 אלף שקל לחברת ידיעות-אחרונות בשל הפסקת הסכם ההפצה של העיתון'}]
39
Your max_length is set to 3000, but your input_length is only 1614. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=807)
[{'summary_text': 'במקום ריבוי כלי תקשורת שיוביל לזירה תקשורתית מגוונת, שפונה להרבה קהלים, להרבה טעמים - קיבלנו הרבה מאותו דבר'}]
35
[{'summary_text': 'הקמפיין של תנובה ל"חלב משק" מקדם מחקר שכלל לא התפרסם • המחקר מציג שיפור בבריאות הפרה, אבל לא בבריאות האוכלוסייה'}]
40
Your max_length is set to 3000, but your input_length is only 1645. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=822)
[{'summary_text': 'חנוך מילביצקי, המנהיג הרוחני של תנועת "קבלה לעם", לא הגיע לדיון בתביעת הדיבה שהוא מנהל נגד גור מגידו, כתב חוקר בעיתון "דה-מרקר" • מיכאל לייטמן, המנהיג הרוחני של תנועת "קבלה לעם", לא הגיע לדיון • שופט בתיק: "עשית דין לעצמך"'}]
86
Your max_length is set to 3000, but your input_length is only 1717. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=858)
[{'summary_text': 'הצנזורית הצבאית הראשית סיפרה כי התריעה בפני ראשי "הארץ" מפני הדפסת המסמכים שקיבל אורי בלאו, מחשש שאלה יובילו לחשיפת המקור. "הלקח שלי מהפרשה הזאת היא לומר לעיתונאים, מקשיבים לנו, מקליטים אותנו"'}]
70
[{'summary_text': 'השופטים מדווחים על אירועים מעצבנים, אבל לא על החלטות שיפוטיות. העיתונות מנסה לתפקד בסביבה חשופה'}]
34
Your max_length is set to 3000, but your input_length is only 2985. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1492)
[{'summary_text': 'ירון לונדון, מנכ"ל קשת, מסביר כיצד קרה שסדרת הטלוויזיה "הפואטיקה של ההמונים" עלתה לאוויר. רוני דגן, עורכת הסדרה, מסבירת'}]
50
Your max_length is set to 3000, but your input_length is only 1536. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=768)
[{'summary_text': 'העיתונים מדווחים על פצצות סוריות בגולן | "מעריב" ממשיך לפעול | "הארץ" ממשיך לנסות לסכסך עם נתניהו'}]
39
Your max_length is set to 3000, but your input_length is only 705. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=352)
[{'summary_text': 'אלון בן-דוד מותח ביקורת על "הארץ" בשל פרסום מידע סודיים. הביקורת היא הביקורת שהוא מותח על עיתון בשל פרסום מידע'}]
34
Your max_length is set to 3000, but your input_length is only 1688. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=844)
[{'summary_text': 'פייסבוק תעביר 4 מיליון שקל לקרן לתובענות ייצוגיות, סכום אשר יוקדש לקידום פעילויות הקשורות לפרטיות'}]
33
Your max_length is set to 3000, but your input_length is only 1643. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=821)
[{'summary_text': 'תצלומי "מלחמת לבנון השנייה" מערערים אט־אט את האמונה השלמה שבכוח ננצח'}]
28
[{'summary_text': 'דו"ח השכר בשירות הציבורי הוא כלי מרכזי למלחמה בשחיתות מוסדית. גם השנה, במקום לקבל עיסוק רציני בדו"ח ובמשמעויותיו, קיבלו רוב הקוראים כתבות שעיקרן רכילות וניסיון להדהים אותם ברמות השכר הגבוהות במגזר הציבורי'}]
66
[{'summary_text': 'מיזם חדש של תעשיית הפרסום באינטרנט, שמטרתו לספק מידע על הגלישה של גולשים באתרים הגדולים, מביא לידי משרדי הפרסום הגדולים בישראל נתונים על הרגלי הגלישה שלהם, אבל לא על הנתונים הדמוגרפיים של הגולשים'}]
64
Your max_length is set to 3000, but your input_length is only 696. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=348)
[{'summary_text': 'יצחק מרדכי, שר הביטחון, ממשיך לשרת את התקשורת בתפקידו. התקשורת מחלה לו על העדר השקפת עולם פוליטית מגובשת, והיא יוצאת מגדרה בתשבחות על הפרגמטיות שלו'}]
49
[{'summary_text': 'נוסד על-ידי ליאון טרוצקי ב-3 באוקטובר 1908 כעיתון סוציאל-דמוקרטי ברוסית. יצא לאור מחוץ לרוסיה והוברח אליה בחשאי, מאימת שלטון הצאר'}]
54
Your max_length is set to 3000, but your input_length is only 419. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=209)
[{'summary_text': '"ישראל היום" ממשיך לנסות לחשוף את יחסי נתניהו לנתניהו | "ידיעות אחרונות" ממשיך לנסות לחשוף את יחסי הליכוד לנתניהו | "גלובס" ממשיך לנסות למנוע סחבת'}]
56
Your max_length is set to 3000, but your input_length is only 907. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=453)
[{'summary_text': 'קרן התחקירים העצמאית: 100,000 ש"ח לעיתונאים עצמאיים, 3 תחקירים שיבצעו עיתונאים עצמאיים'}]
42
Your max_length is set to 3000, but your input_length is only 1538. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=769)
[{'summary_text': 'המשטרה תאכוף את החוק במקרה שמי שמפר אותו הוא בנימין נתניהו • העיתונאים שומרי החוק נשכו שפתיים ושתקו • נתניהו חשף בבולטות את ההתקדמות בחקירה, האסורה לפרסום, בדפי הפייסבוק שלו בעברית וברוסית'}]
62
[{'summary_text': 'הביקורת הפמיניסטית הקולנית על אובמה, על אף שיש בה מידה רבה של אמת, גורמת בסופו של דבר יותר נזק מאשר תועלת'}]
38
Your max_length is set to 3000, but your input_length is only 1578. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=789)
[{'summary_text': 'העיתונים מדווחים על מלחמה | "ישראל היום" ממשיך לחשוף את סוד הטלוויזיה | "ידיעות אחרונות" מציג טפח פה'}]
38
Your max_length is set to 3000, but your input_length is only 958. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=479)
[{'summary_text': 'יומנה השקוף של ח"כ תהלה פרידמן משקף את המצב העגום של הכנסת ה-23: פרידמן מתרוצצת בין ארבעה דיונים ביום בממוצע, ככל הנראה כי היא חברה במספר גדול במיוחד של ועדות. זאת, בשל ריבוי השרים וסגני השרים ממפלגתה, שאינם יכולים לתפקד כח"כים ולכן העומס מוטל על ח"כים בודדים בלבד'}]
97
Your max_length is set to 3000, but your input_length is only 240. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=120)
[{'summary_text': 'הראיון שערך הכתב הבכיר אטילה שומפלבי עם אשת העסקים קרלי פיורינה היה תוכן מערכתי לכל דבר, אך בפועל נעשה בעקבות יוזמה של מחלקת השיווק במרכז ללימודים אקדמיים'}]
53
[{'summary_text': 'שרי ממשלת נתניהו מתקבלת שיחת טלפון. על הקו - נציג מזכירות הממשלה. עוזרי השרים מתבקשים להציץ בדחיפות בתיבת הדוא"ל ולאשר את החלטה 871. כמו שאר החלטות הממשלה שהועלו לאישור טלפוני - גם זו אושרה ללא דיון. ההחלטה – שאנו חושפים כאן לראשונה – מגדילה משמעותית את תקציב שעות לימוד במוסדות חינוך חרדיים'}]
97
[{'summary_text': 'רונן ברגמן, עיתונאי "הבור", מסביר כיצד התגייסו כלי התקשורת לטובת הרמטכ"ל אשכנזי לאורך פרשת הרפז • "הבור" מציג תערובת ייחודית ומופלאה של הרבה מאוד עניינים • בן כספית מסביר כיצד כותב על אבי בניהו ב"מעריב"'}]
79
Your max_length is set to 3000, but your input_length is only 2015. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1007)
[{'summary_text': 'העיתונות כלל אינה מתעניינת בהסכם הסחר הבינלאומיים הגדולים, אבל הציבור נותר עיוור לחלוטין. לא רק הציבור נותר עיוור לחלוטין, גם חברי הכנסת לא יודעים על קיומו. חלקם אפילו לא יודעים על קיומו'}]
52
Your max_length is set to 3000, but your input_length is only 2927. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1463)
[{'summary_text': '"ידיעות אחרונות" ממשיך לנסות לסחוט את רגשות הקוראים | "מעריב" ממשיך לנסות לחשוף את הסכנות האיראניות בצרנוביל | ו"מעריב" ממשיך לנסות לחשוף את הסכנות האיראניות בצרנוביל'}]
63
Your max_length is set to 3000, but your input_length is only 1137. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=568)
[{'summary_text': 'העיתונאים, ולצידם הדוברים הצבאיים והממשלתיים, אחראי חופש המידע ומערכי הצנזורה וביטחון המידע • השיח בעניין אחריותם של העיתונאים יש לפתוח בהסתייגות מהדהדת'}]
50
Your max_length is set to 3000, but your input_length is only 720. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=360)
[{'summary_text': 'הנהלת "מעריב": "הנהלה לא גמלה בלבה החלטה מוגמרת של התזת ראשו של יו"ר הוועד"'}]
34
Your max_length is set to 3000, but your input_length is only 1121. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=560)
[{'summary_text': '"דה-מרקר" פירסם תרשים שהציג את שווי הקבוצות העסקיות בישראל ביחס לכלל השוק העולמי'}]
29
Your max_length is set to 3000, but your input_length is only 1407. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=703)
[{'summary_text': 'היה סטיקר בארץ: "העם נגד תקשורת עוינת". אלפי מכוניות נשאו אותו בגאווה על אחוריהן. למחרת רצח רבין הוא נעלם, בגירוד מבוהל אחד'}]
44
Your max_length is set to 3000, but your input_length is only 2320. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1160)
[{'summary_text': 'ה"ניו-יורק טיימס" לא היה מוצא לנכון לפרסם קריקטורות חדשות בימים כתיקונם, אז מדוע היום?'}]
35
Your max_length is set to 3000, but your input_length is only 1010. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=505)
[{'summary_text': 'ועדת חקירה ממלכתית קמה מאז ראשית המדינה מדי 4 שנים בממוצע • הסיכוי שתקום אחת אחרי הקורונה או האסון במירון - קלושה • יש גם אפשרות נוספת: להקים ועדת חקירה פרלמנטרית - כלומר ועדה בה יישבו חברי כנסת • אבל הסיכוי שראש הממשלה יאפשר לעלות להצבעה הקמת ועדת חקירה - כמעט ולא קיים • הסיכוי שראש הממשלה יאפשר לעלות להצבעה הקמת ועדת חקירה - כמעט ולא קיים • הסיכוי שראש הממשלה יאפשר לעלות להצבעה הקמת ועדת חקירה - כמעט ולא קיים • הסיכוי שראש הממשלה יאפשר לעלות להצבעה הקמת ועדת חקירה - כמעט ולא קיים'}]
158
[{'summary_text': 'עסקת שוחד בין נתניהו למו"ל "ידיעות אחרונות" מדגימה שוב את האמת המרה על עולם התקשורת הישראלי'}]
29
[{'summary_text': 'העיתונים מדווחים על משבר בקווקז | העיתונים מדווחים על משבר עולמי | נחום ברנע מסביר מה קרה עם סוריה'}]
38
Your max_length is set to 3000, but your input_length is only 1023. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=511)
[{'summary_text': '"ידיעות אחרונות" ממשיך לנסות לטפל בעובדי הדסה | "מקור ראשון" ממשיך לנסות לטפל בחוק הספרים | "הארץ" ממשיך לנסות לטפל בשער הראשי'}]
48
Your max_length is set to 3000, but your input_length is only 1950. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=975)
[{'summary_text': 'ההורים כבר קיבלו הודעה על השביתה, בשביל זה לא צריך עיתונאים. כן צריך עיתונאים בשביל, ובכן, שיעשו עבודה עיתונאית. לא כדי שיתווכו לנו הודעות שמגיעות אלינו במילא לווטסאפ, אלא כדי שיבדקו את הנושא לעומקו ויסבירו אותו לציבור ההורים והתלמידים, ואולי גם למורים שלא יודעים בדיוק את פרטי המאבק שמתקיים בשמם'}]
94
Your max_length is set to 3000, but your input_length is only 1848. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=924)
[{'summary_text': 'אחרי שנים של טרוניות על הדילים בוועדה לבחירת שופטים, מציגים גברי המתווה פתרון יצירתי: דילים על ספידים. כדי לבלבל את האויב, כלומר אותנו הציבור, ניסחו המנסחים שתי חלופות לוועדה לבחירת שופטים, שנדמות כמו שאלה בלתי קריאה בפסיכומטרי'}]
78
Your max_length is set to 3000, but your input_length is only 898. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=449)
[{'summary_text': 'מועצת הרבנות הראשית לישראל היא גוף שמייצג את 29 ערים ומועצות מקומיות בישראל. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים לישראל מכהנים ברוטציה כנשיאי מועצת הרבנות הראשית. בנוסף עליהם חברים הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות. בנוסף עליהם חברים הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות. בנוסף עליהם חברים הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות. בנוסף עליהם חברים הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות. מועצת הרבנות הראשית מורכבת כיום מ16 חברים. שני הרבנים הראשיים של ירושלים, תל-אביב, חיפה ובאר שבע מכהנים ברוטציה כנשיאי מועצת הרבנות.'}]
711
Your max_length is set to 3000, but your input_length is only 1713. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=856)
[{'summary_text': 'עיתונאים ברוסיה ממשיכים לחטוף מכות רצח, הגורמים הממשלתיים ממשיכים לחטוף אימה על העיתונות הרוסית, ועוד חדשות תקשורת מהרשת העולמית'}]
42
Your max_length is set to 3000, but your input_length is only 1678. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=839)
[{'summary_text': 'עונת המלפפונים בעיצומה, וכתבי האינטרנט נראים כמו מחפשי זהב להוטים במורד הנהר, נאבקים עד חורמה בתוך הבוץ. כל מי שמניח יד על פירור לא מלוטש, לא שוכח לצעוק מי היה ראשון'}]
61
Your max_length is set to 3000, but your input_length is only 1365. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=682)
[{'summary_text': 'אורי יוגב, מנהל רשות החברות הממשלתיות, מסביר כיצד הפגיעה האפשרית מתהליך פוליטיזציה במערכת המשפט תוביל לדעתו לירידה חדה במקצועיות ולשחיתות • "אני מכיר את תפיסתו הכלכלית ואני גם מכיר את החשיבות הגדולה שהוא נותן לגופים ולשווקים הבינלאומיים"'}]
73
Your max_length is set to 3000, but your input_length is only 1293. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=646)
[{'summary_text': 'במקום להתמודד עם המציאות, כלומר עם המקור, אמצעי התקשורת מעדיפים להתמודד עם החיקוי של המציאות. "הדבר היחיד שחשוב הוא מה שמתקיים כאן, בטלוויזיה"'}]
40
Your max_length is set to 3000, but your input_length is only 859. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=429)
[{'summary_text': 'הדיון על פעולות הממשלה לקראת תום הזיכיון של כיל בים המלח בכנסת, הדהדו את האינטרס של חברת הכימיקלים, ואיש לא חלק על הקביעות המטעות של נציגת החברה, פרט לחבר הכנסת לשעבר מיקי רוזנטל'}]
62
Your max_length is set to 3000, but your input_length is only 1860. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=930)
[{'summary_text': 'משרד התיירות שילם לקשת 1.5 מיליון שקל במסגרת קמפיין לעידוד תיירות הפנים • ברשות השנייה סירבו להתייחס לדברים'}]
35
Your max_length is set to 3000, but your input_length is only 1142. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=571)
[{'summary_text': 'היועמ"שית לממשלה ויתרה ונמנעת מזירת עימות נוספת עם השר בן גביר, מי שיפסיד הם אזרחי ואזרחיות ישראל שעלולים להתעורר בוקר אחד למציאות קולומביאנית'}]
48
Your max_length is set to 3000, but your input_length is only 1998. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=999)
[{'summary_text': 'ארגון לובי 99: "מאחר שנראה כי לא קיים הסכם ניגוד עניינים עם אבי לרנר, עולה חשש ממשי כי שיקוליו העסקיים מתערבבים בתפקידו כיועץ אסטרטגי"'}]
52
[{'summary_text': 'הגשת החומר ערוך אל שולחן השבת של הצופים מקשה גם על המתנגדים המובהקים ביותר להפעלת חוק הסוביודיצה מלטעון כי אין כאן כדי לבסס עמדה עוינת כלפי החשוד המסוים הזה'}]
53
Your max_length is set to 3000, but your input_length is only 740. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=370)
[{'summary_text': 'העיתונים מדווחים על פעולות צה"ל נגד פעילי שלום | "ידיעות אחרונות" מדווח על הפגנה נגד ימנית | "דה-מרקר" ממשיך לסקר את התגלית'}]
50
Your max_length is set to 3000, but your input_length is only 923. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=461)
[{'summary_text': '"תיקונים 37" 38: מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב, מינויים לנשיא ארה"ב'}]
1181
Your max_length is set to 3000, but your input_length is only 1274. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=637)
[{'summary_text': 'בריטניה, בבריטניה ובארה"ב, החל איסור על תיעוד הנעשה מאולמות הדיונים, אך בישראל הותר לצלם את פסק הדין רק בכמה מבתי-המשפט'}]
43
Your max_length is set to 3000, but your input_length is only 1176. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=588)
[{'summary_text': 'הדיון על שינוי האקלים, שעורר את הדיון על נזקי ההכחשה והדיסאינפורמציה שמלווים את הדיון על שינוי האקלים למעלה מעשרים שנה, הוא דיון חשוב ורלבנטי שמסקנותיו יקבעו מה התיקון שיש לעשות ובאיזה קצב ייעשה'}]
66
Your max_length is set to 3000, but your input_length is only 1355. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=677)
[{'summary_text': 'ארגונים ציבוריים תורמים כספים לעמותות שלהם. השרים גוזרים קופון וזוכים לצינורות מימון עקיפים. זהר אלטמן רפאל: "מדובר בתופעה המחייבת שקיפות של תרומות החברות הציבוריות"'}]
60
Your max_length is set to 3000, but your input_length is only 787. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=393)
[{'summary_text': 'ההסכם בין קבוצת "הארץ" לוואלה היה מהלך תקשורתי שגרתי. התוצאה היתה כמעט בלתי נסבלת'}]
27
[{'summary_text': 'בית-משפט השלום פסק כי "ישראל פוסט" תפצה את הצלם אריאל ירוזולימסקי ב-77,500 שקל בשל הפרת זכויותיו המוסריות'}]
42
Your max_length is set to 3000, but your input_length is only 959. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=479)
[{'summary_text': 'דוקטור ארז ברקאי, מומחה לאקולוגיה, מסביר כיצד נוצרה מלחמה על פיתוח עצים ברחבי הארץ • "הצלה מתרחשת כל יום, את העצים שהצלנו מידי היזמים הציבור לא רואה" • "הציבור רואה את העצים שאנחנו מאשרים לכרות ורבים עליהם" • "הצלה מתרחשת כל יום, את העצים שהצלנו מידי היזמים הציבור לא רואה"'}]
98
Your max_length is set to 3000, but your input_length is only 462. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=231)
[{'summary_text': 'הקלות הרגולטוריות לערוץ 14, המשדר שידורי תעמולה לממשלת נתניהו, יחולו על ערוץ 14 מחובות רגולטוריות שונות, בעלות משוערת של עשרות מיליוני שקלים'}]
50
Your max_length is set to 3000, but your input_length is only 1301. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=650)
[{'summary_text': 'יו"ר ועדת האתיקה של רשות השידור פירטה בפרוטוקולים את הגורמים שהביאו אותה לכדי ייאוש ואת ועדת האתיקה לסף פירוק'}]
43
[{'summary_text': '12 שרים ושרים לשעבר לא הגישו את הצהרות ההון למבקר המדינה • מבקר המדינה: שרים ושרים לא מגישים את הצהרות ההון שלהם בתוך 60 ימים מהיציאה מהתפקיד • בכך הם עוברים על ההנחיות: שרות ושרים לשעבר, כמו גם סגניהם, מחויבים להגיש את הצהרות ההון שלהם בתוך 60 ימים מהכניסה או היציאה מהתפקיד'}]
98
[{'summary_text': 'אהרון ברנע, מגיש מהדורת החדשות של יום שישי בערוץ 2, עובר לדווח מוושינגטון. את מקומו על כיסא "אולפן שישי" יתפוס יאיר לפיד'}]
48
Your max_length is set to 3000, but your input_length is only 534. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=267)
[{'summary_text': 'העיתונים מדווחים על מירוץ כלבים | "ידיעות אחרונות" ממשיך לקדם את גלעד שליט | "כלכליסט" ממשיך לקדם את דו"ח המבקר'}]
44
[{'summary_text': 'האם הצנזורה הצבאית פסלה את הסרט "ממלכת הסוד"? האם העיתונות הישראלית פתוחה יותר מבעבר? ומה קורה עם נשים בכדורגל?'}]
39
Your max_length is set to 3000, but your input_length is only 825. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=412)
[{'summary_text': 'העיתונים החרדיים ממשיכים לדוש בה בראש סדר היום | "ידיעות אחרונות" ממשיך לקדם את המבצע | "מעריב" ממשיך לקדם את העיתון'}]
40
[{'summary_text': 'הישגים יפים רשמה לזכותה העיתונות הישראלית בשבועות האחרונים: תחקירו של יואב יצחק על תשלומי הסתר החודשיים שקיבל הנשיא עזר ויצמן זכה לאישור מלא בחקירת המשטרה'}]
53
Your max_length is set to 3000, but your input_length is only 2764. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1382)
[{'summary_text': '"ישראל היום" ו"ידיעות אחרונות" מתכוננים למבצע הקרקעי | עמירה הס וגיקי חורי מדווחים על הרג יהודים בעזה | "המבשר" מציג תמונה ברורה של בהירות מוסרית'}]
54
Your max_length is set to 3000, but your input_length is only 917. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=458)
[{'summary_text': 'העיתונים האמריקאיים מתכוננים לאולימפיאדת 2012, אבל לא יודעים מה לעשות עם הנשיא אובמה בקופנהגן | העיתונים מתכוננים לסוף השבוע הדרמטי בקופנהגן | ומואל רוזנר מתאר קשר עם שמואל רוזנר'}]
63
[{'summary_text': 'ארגון נכי צה"ל הגיש תביעת דיבה נגד "דה-מרקר", השנייה בתוך שנה. הארגון דורש פיצוי של כ-140 אלף שקל בשל פרסום תחקיר מאת טלי חרותי-סובר'}]
53
[{'summary_text': '"ישראל היום" שוב מתייחס לאוכלוסייה היהודית בישראל כאל "הציבור" כולו | "ידיעות תל-אביב" ממשיך לקדם את תושבי קריית-שלום | "מקור ראשון" ממשיך לקדם את "כתב-עת מדיני"'}]
58
Your max_length is set to 3000, but your input_length is only 430. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=215)
[{'summary_text': 'הבטחות יפות שנתנו חלק ממפלגות השלטון ל"שקוף" לפני הבחירות הקודמות, וחלק אחר פיזרו במצעים מטעמן - לא זזו מילימטר, על אף שלכאורה לא אמור היה להיות גורם שיסכל את החקיקה • ממשלת השינוי לא ביצעה כמעט מהלכים בכיוון - אך הציבור צריך לדרוש מנציגיו הרבה יותר כדי לחסום את השחיתות בשערי הדמוקרטיה • ננסה להתחיל מהטוב'}]
104
[{'summary_text': 'שידורי הגל-השקט, המצאה ישראלית מקורית בתחום הרדיו והאזעקה, החלו בימי התקפות הטילים של מלחמת המפרץ הראשונה, והם "ככל הידוע המצאה ישראלית מקורית בתחום הרדיו והאזעקה"'}]
56
[{'summary_text': 'העיתונות החדשה לא תהיה טובה מקודמתה. שהרי העולם הווירטואלי מאמץ לעצמו לא מעט מדפוסי העבודה והערכים המקצועיים של העיתונות הממוסדת, לטוב וגם לרע'}]
47
[{'summary_text': '"גלובס" מסגר את הסיפור באופן הפוך | "מעריב" מסגר את הסיפור באופן הפוך | "ידיעות אחרונות" ממשיך לחשוף את סוד השייטת'}]
41
[{'summary_text': 'העיתונים מדווחים על הפסגה המשולשת בניו-יורק | "ידיעות אחרונות" מדווח על ציפיות גדולות | "ישראל היום" מדווח על ציפיות גדולות'}]
46
[{'summary_text': 'העיתונים מדווחים על מופע האימים של חמאס | "מעריב" ממשיך לנסות למנוע הפסקות מים | ו"הארץ" ממשיך לנסות לפצח את חידת ההמון'}]
46
Your max_length is set to 3000, but your input_length is only 902. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=451)
[{'summary_text': 'העיתונים מדווחים על גזירות בתקציב המדינה | "ידיעות אחרונות" ממשיך לעבוד עליכם | יעל ברדה מסבירת כיצד עשו הישראלים'}]
39
[{'summary_text': 'המעבר מסיקור הרשות המבצעת והרשות המחוקקת לסיקור הרשות השופטת מאפשר לעיתונאי להשוות גם בין יחסם של שלושת עמודי היסוד של הדמוקרטיה הישראלית לרשות הרביעית, העיתונות'}]
56
[{'summary_text': 'העיתונים מדווחים על מחיר פסק-זמן | "ידיעות אחרונות" ו"ישראל היום" מדווחים על התנהגות לא הולמת | "הארץ" ממשיך לנסות לקדם את המהלך'}]
47
Your max_length is set to 3000, but your input_length is only 473. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=236)
[{'summary_text': '"מעריב" מנסה לפזר מעט את הערפל שבו מתנהלים המגעים הבלתי מתוקשרים | "ידיעות אחרונות" ו"ישראל היום" מדווחים על פיטורים מוניים | "גלובס" מציג סקופ יוצא דופן'}]
57
[{'summary_text': 'משרד התחבורה מבקש לתקן את פקודת התעבורה ולהעניק לחברות התחבורה כלים אפקטיביים לאכיפה, ביניהם: בעיניי, ישנו הגיון רב בחלק מהתיקונים המוצעים – ואולי גם בכולם. עם זאת, שווה להסתכל רגע לצדדים ולראות כיצד ממשיכה הממשלה לתת עדיפות לרכבים פרטיים על-פני תחבורה ציבורית'}]
85
[{'summary_text': 'דן מרגלית כותב על פרשת חשבון הדולרים של יצחק רבין, עיתונאי שחשף את המקרה בניו-יורק. דן מרגלית כותב על פרשת "העולם הזה"'}]
54
Your max_length is set to 3000, but your input_length is only 282. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=141)
[{'summary_text': 'העיתונים בישראל מדווחים על עיתונות אלטרנטיבית, אך לא על עיתונות עצמאית. העיתונים האחרים, כמו "כאן", מנסים לקדם עיתונות אלטרנטיבית'}]
47
Your max_length is set to 3000, but your input_length is only 2083. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1041)
[{'summary_text': 'נחום ברנע: הזיהום בחיפה טוב יותר מאשר בשאר אזורי הארץ. ב"מוסף לשבת" של העיתון התייחסו נחום ברנע לסוגיית תחלואת הילדים'}]
45
Your max_length is set to 3000, but your input_length is only 2349. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1174)
[{'summary_text': 'הצעת החוק לאיחוד רשויות הפיקוח על הטלוויזיה היא פרי עבודה של שר התקשורת משה כחלון, שאומצה על-ידי השר הנוכחי גלעד ארדן'}]
35
Your max_length is set to 3000, but your input_length is only 1994. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=997)
[{'summary_text': 'העיתונים מדווחים על מלחמה, המבצע מתקתק | "ישראל היום" ממשיך לדשדש | "מעריב" ממשיך לפעול במתכונת חירום'}]
39
Your max_length is set to 3000, but your input_length is only 2368. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1184)
[{'summary_text': 'העיתונים מדווחים על המלחמה בגיאורגיה | "הארץ" מדווח על סחר נשק ישראלי לגיאורגיה | יוסי מלמן מתלונן על טקס הפתיחה חסר חיוך'}]
45
Your max_length is set to 3000, but your input_length is only 1103. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=551)
[{'summary_text': '"מעריב" יוצא עם כותרת ראשית דרמטית | "ידיעות אחרונות" מצטט את ירמי עמיר | ונחום ברנע ממשיך לבקר את שימי גת'}]
44
[{'summary_text': 'שר המידע הסיני: אין צנזורה מקוונת, אין עיתונאים בסין, אין עיתונאים בסין, אין עיתונאים בסין, אין עיתונאים בסין, אין עיתונאים בסין, אין עיתונאים בסין'}]
54
Your max_length is set to 3000, but your input_length is only 2380. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1190)
[{'summary_text': '"גלובס" מגיב להחלטה לאסור על פרסום תצלומים של חשודים במתן שוחד | "ישראל היום" מתגאה בצה"ל | סבר פלוצקר מגן על גילה'}]
46
Your max_length is set to 3000, but your input_length is only 2220. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1110)
[{'summary_text': 'רשות השידור מעניקה קרטל שידורים ישירים לאולימפיאדה 2012 | "ישראל היום" ממשיך לשלם על טעם וריח | "ידיעות אחרונות" ממשיך לטפל באייטם'}]
53
Your max_length is set to 3000, but your input_length is only 1049. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=524)
[{'summary_text': 'הבחירה בדמויות המככבות בתוכנית "מחוברים" מתאימה למגמה שהעיתונות עצמה כבר שועטת בה: הפרטת העבודה, התרחבות פערי המעמדות בין הטאלנטים ל"פועלים השחורים", היעלמות המערכת ועוד'}]
60
[{'summary_text': 'העיתונות העברית במקום להיות גשר לקירוב בין שני העמים שנגזר עליהם לחיות יחדיו בארץ תורמת להנצחת הפערים בין שתי האוכלוסיות ולהעמקת תחושת הניכור של הפלסטינים בישראל'}]
49
Your max_length is set to 3000, but your input_length is only 831. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=415)
[{'summary_text': '"מעריב" מדווח על קרב פומבי | "ידיעות אחרונות" מבלט את עמדת משרד האוצר | "גלובס" מבלט את עמדת משרד האוצר'}]
41
Your max_length is set to 3000, but your input_length is only 1110. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=555)
[{'summary_text': 'פעיל נגד צריכת חלב חויב לשלם 70 אלף שקל פיצוי לרפתן בשל סטטוס שפירסם בפייסבוק'}]
32
[{'summary_text': 'חיים ריבלין, כתב חדשות ערוץ 2, על היחסים בין יעקב ליצמן לחברות הסיגריות, על הפרסום האגרסיבי של חסידות גור, על הניקוי העצמי של נחום ברנע, על העיתונות המסחרית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית, על העיתונות העברית'}]
2073
[{'summary_text': 'העיתונים מדווחים על המשך הקפאה של נתניהו | העיתונים הכלכליים מדווחים על מלחמה על הגז | ו"מעריב" ממשיך לנסות לקדם את המלחמה'}]
45
Your max_length is set to 3000, but your input_length is only 758. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=379)
[{'summary_text': '"ידיעות אחרונות" ו"ישראל היום" מתכוננים למלחמה בתקציב הביטחון | "מקור ראשון" ו"מקור ראשון" מדווחים על ברית הזוגיות | "מקור ראשון" ו"מקור ראשון" מדווחים על ברית הזוגיות'}]
56
Your max_length is set to 3000, but your input_length is only 1339. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=669)
[{'summary_text': 'הטיעון שהעיתונאים מקדמים כך את עצמם ומקבלים במה נוספת להשמיע את עמדותיהם הוא טיעון מעוות וחסר משמעות. והלא גם בעיתון מקבלים העיתונאים במה, ותפוצה, ותהודה, וזוכים להכרה ולפרסום – ובכל זאת איש אינו מעלה על דעתו להציע להם לכתוב בו בהתנדבות'}]
80
[{'summary_text': 'דני זקן מנסה לאלץ את מנהל גלגלצ למנות לשדרן בתחנה. זקן: "אני בחיים לא פגשתי את ביבי נתניהו. מעולם לא"'}]
42
[{'summary_text': 'עובדי ynet מתכוננים לשינוי במערכת העיתונאית, אך לא מתכוננים לשינוי ביחס לעובדים לשעבר. השינויים במערכת העיתונאית של האתר מלמדים על השינוי הגלוי שחל בנפח המודעות ובמיקומן'}]
55
[{'summary_text': 'העיתונים מדווחים על גראד בבאר-שבע | "ישראל היום" מדווח על ירי בניו-זילנד | "ידיעות אחרונות" ממשיך לקדם את "3 חשיפות"'}]
47
[{'summary_text': '"הביוגרפיה של יוסף לנג על אליעזר בן-יהודה (אב"י) ממחישה את ערוותו המקצועית מתוך חוכמה שבדיעבד, במלאכת מחשבת של הצלבת מקורות היסטוריים"'}]
53
Your max_length is set to 3000, but your input_length is only 239. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=119)
[{'summary_text': '"אני עומד שם ליד הניידת כאשר מפרקים את קרביה, כבלים ומצלמות, וחושב לעצמי: זה הרי לא רציונלי, הרצון הזה לטלוויזיה אינסטנט, זה ביטוי לחטא התאווה שלנו לשדר תכף ומיד ויהי מה". חיים יבין, "עובר מסך", ספרו האוטוביוגרפי של חיים יבין'}]
80
Your max_length is set to 3000, but your input_length is only 1536. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=768)
[{'summary_text': 'כיצד ישפיע המהלך של שר המשפטים על כוחם של בנקים ומונופולים - ומכאן גם על הכיס שלנו? לוביסטים בכירים עמם שוחחנו, מי שתפקידם לקשר בין בעלי ההון לשלטון, מספרים כי העברת הכוח לממשלה ולכנסת, במצב הנוכחי ובהיעדר שקיפות, תיתן עוד כוח לתאגידים רבי עוצמה, על חשבוננו'}]
92
Your max_length is set to 3000, but your input_length is only 2134. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1067)
[{'summary_text': 'ניתוח מילולי של 61 הדיונים האחרונים במליאה מגלה: עופר כסיף, אמילי מואטי ואבי מעוז – אלו חברי הכנסת שמשתמשים באוצר המילים המגוון ביותר בעת נאומיהם במליאה'}]
52
Your max_length is set to 3000, but your input_length is only 271. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=135)
[{'summary_text': 'עמוס קינן, עיתונאי סאטירי, מוצא עצמו מחזר אחרי פתחיהם של העיתונים האחרים. ספרו "על דעת עצמו" מלמד על עיתונאי חשוב'}]
43
Your max_length is set to 3000, but your input_length is only 2056. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1028)
[{'summary_text': 'קביעתו של דובר צה"ל בתוך התגובה שמסר לראיון עימי ("המטה הקטן", 1.3.11), כאילו "השאלות שהועברו מטעמו ומטעם מר מרגלית הגיעו ערב יציאת ספרם, לאחר שכבר נערך ונחתם", רחוקה מהאמת'}]
71
Your max_length is set to 3000, but your input_length is only 915. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=457)
[{'summary_text': 'בית-הדין לעבודה דחה את בקשת אגודת העיתונאים לקבל מעמד של ארגון עובדים יציג באתר ynet. "לא עולה על הדעת שמשום שארגון עובדים חדש מנסה מטעמים פוליטיים כאלה ואחרים לקבל הגמוניה, דרך אמצעי תקשורת שבו לא היתה פעילות, אני אמצא את עצמי נאלץ לנהל משאים-ומתנים עם כמה קבוצות", אמר בא-כוחה של ההנהלה'}]
96
Your max_length is set to 3000, but your input_length is only 2411. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1205)
[{'summary_text': 'השמחה הגדולה ביותר על מינויו של היועץ המשפטי החדש, מני מזוז, לא נרשמה במסדרונות הממשלה, וגם לא בבית משפחתו'}]
34
Your max_length is set to 3000, but your input_length is only 1379. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=689)
[{'summary_text': 'רשות ההגבלים העסקיים אינה נוטה להגדרות שוק צרות ומגבילות, ובמיוחד בשוקי תקשורת ומדיה. אחד המבחנים המרכזיים בהקשר הזה הוא מבחן התחליף; איזה מוצר תחליפי ל"מקור ראשון" ייחשב בעיני קוראיו כסביר'}]
62
[{'summary_text': 'ח"כ איתן גינזבורג, יו"ר ועדת הכנסת, ביקש להפריך את הטענות לפיהן הצעת החוק לשינוי הרכב הוועדה הציבורית שדנה בשכר הח"כים נובעת ממניעים לא תמימים: "בימים האחרונים ראיתי כבר כל מיני טענות כאילו אנחנו משנים את החוק כדי למנות יושב ראש ידידותי יותר לח״כים, כדי שיתאפשר לנו לשפר את תנאינו"'}]
96
Your max_length is set to 3000, but your input_length is only 692. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=346)
[{'summary_text': 'העיתונים מדווחים על כשלון המשא-ומתן בקהיר | העיתונים מדווחים על גמישות של חמאס | ומדווחים על חוסר הדיוק במידע'}]
43
Your max_length is set to 3000, but your input_length is only 1383. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=691)
[{'summary_text': 'שוקי טאוסיג תוקף את מיכאל שטראוס ב"ממון" על חוסר היכולת להתייחס לעובדיו בענייני מזון'}]
34
Your max_length is set to 3000, but your input_length is only 1889. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=944)
[{'summary_text': '"ידיעות אחרונות" ממשיך לעצבן את אמיר חדד | "הארץ" ממשיך לעצבן את הנכאים | ו"ידיעות אחרונות" ממשיך לעצבן את העיתונאים'}]
47
Your max_length is set to 3000, but your input_length is only 1109. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=554)
[{'summary_text': 'מדוע לא נענתה דרישתו להכין סקר סיכונים מצרפיים לגבי מפרץ חיפה? מדוע לא הוציא מבקר המדינה דו"חות חריפים? ומה קורה עם המשרד להגנת הסביבה?'}]
49
Your max_length is set to 3000, but your input_length is only 1442. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=721)
[{'summary_text': 'העיתונאי עומר נזאל שוחרר מהכלא הישראלי לאחר כעשרה חודשים של מעצר מינהלי. ראיון עם בא-כוחו, עו"ד מחמוד חסאן, על מצבו ותחושותיו'}]
51
[{'summary_text': 'דב אלפון, העורך המיועד של "הארץ", העיד על עצמו כמי שעוסק ב-ווב 2.0 קלאסי. "אני לא באמת חושב שזה כך, אם כי בואו לא נתעלם מהעובדה הבלתי ניתנת לערעור שמרבית התכנים שהווב 2.0 בתצורותיו השונות מייצר מופרכים לחלוטין, חסרי שחר ולא ראויים למאכל גולש"'}]
94
[{'summary_text': '"ישראל היום" מנסה לספק דיווח הגון על ראש הממשלה | "ידיעות אחרונות" מנסה לספק דיווח ארוך יותר על אהוד אולמרט | "כלכליסט" מנסה לספק פרטים על שכר החציוני'}]
57
[{'summary_text': 'אחרי שנים של "מלחמת עולם" בין העירייה לבין המקומון "כל העיר", פורש עורכו של המקומון, ועימו חלק ניכר מצוות העיתונאים'}]
37
Your max_length is set to 3000, but your input_length is only 2438. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1219)
[{'summary_text': 'העיתונים מדווחים על עסקת טילים עם טהרן | "ישראל היום" מדווח על מקרה שמאלני | חיים שיין מוצא לנכון לנגח את ערוץ 2'}]
44
[{'summary_text': 'אגודות העיתונאים: מדינת ישראל תומכת בדרישת אגודות העיתונאים לבטל את מינויו של משה נסטלבאום לתפקיד מנהל חטיבת החדשות בערוץ 1'}]
43
Your max_length is set to 3000, but your input_length is only 674. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=337)
[{'summary_text': 'העיתונים מדווחים על שגיאות מקצועיות, אבל לא על שגיאות אישיות | דן מרגלית ממשיך לכתוב על קיצוץ בתקציב הביטחון | מיכאל הנדלזלץ ממשיך לבקר את המחזמר "לילה לא שקט"'}]
60
Your max_length is set to 3000, but your input_length is only 949. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=474)
[{'summary_text': 'עסקת החיפוש הסינית באידו עם מיקרוסופט תסייע לשוק החיפושים הסיני ללכוד את כל השוק ברשתה'}]
32
Your max_length is set to 3000, but your input_length is only 1096. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=548)
[{'summary_text': 'יו"ר מפעל המלט "נשר", אבי פישר, עוזב את תפקידו. בהודעה שהופצה לעובדים, הודיע בן משה כי יפסיק לכהן בתפקידו הנוכחי ואת מקומו יתפוס סמנכ"ל הכספים, יובל לזרוב'}]
59
[{'summary_text': 'ראש מנהלת תקומה משה אדרי הציג אתמול לראשונה את חזון התוכנית לשיקום היישובים שנפגעו בשבעה באוקטובר • "אנחנו עוברים ותופרים חבילה לכל יישוב ויישוב", אמר • "החזון שלנו לחזור וליישב מחדש את הקהילות, לחדש ולהרחיב את היישובים, למנף ולהביא לשגשוג הקהילות והחבל כאזור חיוני, פורח ואטרקטיבי לתושבי החבל ומדינת ישראל"'}]
103
Your max_length is set to 3000, but your input_length is only 995. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=497)
[{'summary_text': '"הארץ" מציג ספקנות בריאה בגרסתו של חיים פרלמן | "מעריב" מציג ספקנות בריאה בגרסתו של פרלמן | ו"ידיעות אחרונות" מציג ראיון עם אמנון נדב'}]
54
[{'summary_text': 'ארקדי גאידמק הוא דמות פופולרית, והסיכוי לרייטינג - בשמים. וזו תכלית הכל. לכן צריך לשאול: אפילו אם החוק מתיר זאת ככתבו וכלשונו, הלו, רשת, ירדתם מהפסים? את כל הרעיונות היצירתיים ביותר כבר מיציתם?'}]
72
[{'summary_text': 'גרשום שוקן היה מן הסתם מתפלץ אילו ראה גיליון של העיתון הכלכלי "דה־מרקר". ב־51 שנות כהונתו כבעלים, מו"ל ועורך עיתון "הארץ" (מ־1939 עד 1990), הנחיל שוקן ל"הארץ" את תרבות העשייה העיתונאית שהפכה את העיתון לסמל של אמינות, איכות, עומק ומכובדות'}]
102
Your max_length is set to 3000, but your input_length is only 1141. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=570)
[{'summary_text': '"הארץ" מדווח על 1,200 מסתננים | "מעריב" מדווח על מפגש בין גבר אפריקאי לקבוצת מפגינים | "ידיעות אחרונות" ממשיך לנסות לגלות פנים בתורה שלא כהלכה'}]
58
Your max_length is set to 3000, but your input_length is only 574. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=287)
[{'summary_text': 'התאחדות עיתונאי החוץ בישראל עתרה לבג"ץ כדי לאפשר כניסת עיתונאים זרים לעזה בליווי כוחות'}]
33
[{'summary_text': 'ישיבות מועצת העיר קרית אתא עלולות להיות לא יותר מחותמת גומי. אולי ישיבה של 4 דקות היא חוקית - אבל היא לא סבירה. המשמעות היא שאין מרחב לחברי המועצה להביע את דעתם, ואין דרך לציבור לפקח על עבודת חברי המועצה שמטרתם לשרת אותו. התנהלות שכזו פוגעת בדמוקרטיה המקומית של העיר: אם הכל נסגר לפני ישיבת המועצה או בחדרים הפנימיים ולאף אחד אין מה לומר - ישיבת המועצה היא אחיזת עיניים.'}]
122
[{'summary_text': 'אילן ישועה, מנכ"ל "וואלה" לשעבר, העיד כי התערב במערכת העיתונאית של "ידיעות אחרונות" ו"גלובס" כדי לשרת את האינטרסים של אלוביץ • "תקשיב טוב עכשיו", כתב לו המנכ"ל לשעבר, "תוציא לגמרי מראשית ברנזה" • "אני לא מסוגל להבין איך שני אנשים חכמים כמוכם חושבים שכלכליסט יכול יום יום לכתוב נגד בזק ולחשוב שזה לא נוני" • "הוא האיש הכי חזק בקבוצה"'}]
120
Your max_length is set to 3000, but your input_length is only 1861. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=930)
[{'summary_text': 'העיתונים מדווחים על מחאת המתמחים | "ישראל היום" ו"הארץ" מדווחים על הוזלת מחירי מוצרי החלב | "זורנל" ו"גלריה" מדווחים על סלבריטיזציה'}]
52
Your max_length is set to 3000, but your input_length is only 1197. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=598)
[{'summary_text': 'ההחלטה לשמור על ערוץ כלכלי עצמאי ב-ynet לצד האתר הכלכלי של "כלכליסט" נובעת מכוונתו של ynet לשמור על עצמאות מערכתית כמו גם מאינטרסים מסחריים של קבוצת "ידיעות אחרונות". "הסימביוטיות של כלכליסט עם ynet צריכה להיפתר באופן הגון"'}]
73
[{'summary_text': 'קומוניקט הוציא את הכתבה "צרכנות נבונה בנדל"ן" של העורך הכלכלי הבכיר נחמיה שטרסלר, אך לא את הכותרת "צרכנות נבונה בנדל"ן". העיתונאים מנסים להסביר את ההבדל'}]
60
Your max_length is set to 3000, but your input_length is only 581. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=290)
[{'summary_text': 'העיתונים מדווחים על מחדלים חמורים | "ידיעות אחרונות" ממשיך לנסות להסביר מה מגוחך, מיותר וזול כל-כך בריצתם משורבבת הלשון של אנשי פרס ספיר שואפי המכובדות'}]
56
Your max_length is set to 3000, but your input_length is only 642. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=321)
[{'summary_text': 'לאחר ועידת הליכוד האחרונה, זימן אביגדור ליברמן עיתונאים כדי להציג בפניהם את גרסתו על מה שהתרחש בה'}]
35
Your max_length is set to 3000, but your input_length is only 1517. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=758)
[{'summary_text': 'בדיקה שערכנו ב׳מאה ימים של שקיפות׳ חושפת טפח מאימפריית הנדל״ן של משפחת דרעי: לבת אחת של שר הכלכלה דירה בירושלים ושליש בית נוסף בת״א. על בת אחרת רשומות 3 דירות בשכונת התקווה בת״א וחצי דירה נוספת בתל אביב. לבת שלישית דירה לא רחוק בת״א לצד בית במושב בין ת״א לירושלים. לבן אחד דירה במגדלי שאול בירושלים. באותו בניין, אגב, גם ממוקמות דירות של אחיינו של דרעי, כלתו של הרב עובדיה זצ״ל ונכדתו של הרב עובדיה זצ״ל. בן אחר רכש דירה במסגרת קבוצת רכישה בירושלים'}]
164
Your max_length is set to 3000, but your input_length is only 1520. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=760)
[{'summary_text': 'מדד החריצות לחברי הכנסת ה-24: "בתכלס יש קצת בעייתיות במדד אבל הוא הכי פחות גרוע שאפשר" • מדד החריצות לחברי הכנסת ה-24: "התכלס יש קצת בעייתיות במדד אבל הוא הכי פחות גרוע שאפשר" • מדד החריצות לחברי הכנסת ה-24: "בתכלס יש קצת בעייתיות במדד אבל הוא הכי פחות גרוע שאפשר" • מדד החריצות לחברי הכנסת ה-24: "התכלס יש קצת בעייתיות במדד אבל הוא הכי פחות גרוע שאפשר" • מדד החריצות לחברי הכנסת ה-24: "בתכלס יש קצת בעייתיות במדד אבל הוא הכי פחות גרוע שאפשר"'}]
170
[{'summary_text': 'בין שידורי הקדימונים (פרומו) בערוצים המסחריים לבין המוצר שעולה על המסך פעורה לעתים קרובות מדי תהום של תוכן שמתגלגלת בסולם האמינות מ"עבודה בעיניים" עד ל"הונאה"'}]
59
[{'summary_text': '"גלובס" ממשיך לנסות לקדם את הריכוזיות | "מעריב" ממשיך לנסות לקדם את משרד השיכון | גונן גינת מתעלם משמו של "ישראל היום"'}]
46
Your max_length is set to 3000, but your input_length is only 1298. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=649)
[{'summary_text': '"ידיעות אחרונות" ממשיך לבקר את פרופ יולי תמיר, וכך גם את משרד החינוך | "הארץ" ממשיך לבקר את המערכת החינוכית | ו"הארץ" ממשיך לבקר את המערכת החינוכית'}]
56
[{'summary_text': 'הדיוקן המצטבר של שאול מופז שונה לחלוטין מזה שהכרנו עד כה. התקשורת קולטת את התדמית האפויה הזו ומנחילה אותה לציבור כולו'}]
39
Your max_length is set to 3000, but your input_length is only 1292. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=646)
[{'summary_text': 'המעבר המהיר בדלת המסתובבת שבין עולם הלובי למשכן מערבב באופן מדאיג את האינטרס הציבורי והאינטרסים הכלכליים של חברות פרטיות. קשרים בין ח"כים מכהנים ללוביסטים ולחברות עשויים לגרום להם להעמיד את טובת החברות לפני טובת הציבור הרחב'}]
73
[{'summary_text': 'אתר חדשות הגולשים "סקופ" היה אתר חדשות אזרחית. האתר קיבל את כל הידיעות שלו מגולשים מרחבי הארץ והעולם. האתר עבר אימות ועריכה של עורכים מקצועיים טרם פרסומם. האתר נסגר ב-2010'}]
58
Your max_length is set to 3000, but your input_length is only 2599. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1299)
[{'summary_text': 'העיתונים החרדיים מתכוננים לספין פוליטי של אריה דרעי | "דה-מרקר" ממשיך לעסוק במשרד רואי-החשבון של משה ליאון | "ידיעות אחרונות" ממשיך לעסוק בתערוכה של גל וולינץ'}]
59
Your max_length is set to 3000, but your input_length is only 1059. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=529)
[{'summary_text': 'המונדיאל, החגיגה למפרסמים, לכיסם של כלי התקשורת | "ישראל היום" ממשיך לנסות לרדת אל העם | "ידיעות אחרונות" ממשיך לנסות לרדת אל העם'}]
48
Your max_length is set to 3000, but your input_length is only 2994. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1497)
[{'summary_text': 'הבעיה טמונה עמוק בתת-המודע של השרים הישראלים, שרואים בנו כוח אלקטוראלי ותו לא. הם עושים הכל כדי להשריש בקרבנו את ההרגשה שאנחנו לא שייכים למדינה, ולאחר מכן לנהל נגדנו מסע צלב ולהאשים אותנו בבדלנות ובפלסטיניזציה'}]
71
Your max_length is set to 3000, but your input_length is only 1615. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=807)
[{'summary_text': 'העיתונות הממוסדת לא מצאה את הפתרון לבעיה הבסיסית של אתרי החדשות, אלא את הפתרון הבעייתי של העיתונות הממוסדת'}]
38
Your max_length is set to 3000, but your input_length is only 2298. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=1149)
[{'summary_text': 'פסטיבל "יוצרים מציאות" 2009: תפיסות רווחות בתקשורת באשר לאנשים עם מוגבלות'}]
30
Your max_length is set to 3000, but your input_length is only 1438. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=719)
[{'summary_text': '"ידיעות אחרונות" מנסה לנחש את הדרישה של קוראיו מהממשלה | "הארץ" מנסה לסחוט את רגשות הקוראים | ו"ישראל היום" מנסה למנוע את הגעתו לישראל'}]
51
[{'summary_text': 'עיתונות הספורט מתכוננת למינוי המאמן הלאומי הבא | ב-ONE מדביקים לו סטיגמה של מושחת כדי ללחוץ עליו לשנות את החלטתו | ו-ONE מדביקים לו סטיגמה של מושחת כדי ללחוץ עליו לשנות את החלטתו'}]
59
Your max_length is set to 3000, but your input_length is only 635. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=317)
[{'summary_text': 'קונראד בלאק, האיש המשפיע ביותר על העיתונות בקנדה, היה איש עסקים ותאב בצע שבא על עונשו. הסיפור שלו הרבה יותר מורכב'}]
39
[{'summary_text': 'נולד בוורשה, ברח זבוסקה 23, לוולף וצירל מודניצר, הבכור מחמישה ילדים. היה רוכש מודעות עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשקיף". היה רוכש מודעות גם עבור בטאון התנועה "הירדן", ואחריו "המשק'}]
"""

summary_texts = re.findall(r"'summary_text': '([^']*)'", output)
print(summary_texts)

