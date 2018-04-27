# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:11:27 2018

@author: adite
"""
import pandas as pd
import math
from textblob import TextBlob as tb

#module to compute TF
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

#module to compute word count
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

#module to compute IDF
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

#module to compute TFIDF
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

#manually entering the top 20 words for each 25 expert users
avgaunz = tb("""blog thanks	security	scam	email	facebook	online	 mention	tip 	password	malware	privacy	business	spam	user	account	safe	microsoft	android	data
""")

CheckPointSW = tb("""mobile	security	threat	point	malware	attack	check	android	cloud	ransomware	mobilesecurity	infosec	prevention	cybersecurity	 webinar	device	learn	data	enterprise	video
""")

CLTCBerkeley = tb("""cybersecurity	cyber	cltc	policy	future	whcybercomm	commission	join	news	research	talk	host	weber	cyberattack	security	olympics	national	spos	master	cyberattacks
""")

cyber = tb("""chatstc		cybersecurity		cyber		cyberaware		security		business		awareness		month		national		online		help		secretary		privacy		career		criminal		resource		ncsam		rsac		infrastructure		work
""")

CyberArk = tb("""security		cyberark		account		cybersecurity		attack		privileged		today		learn		threat		cloud		credential		infosec		secure		access		risk		privilege		blog		free		join		cyber
""")

DarkReading = tb("""cybersecurity		cyber		cybercrime		security		threat		risk		cybercriminals		woman		insurance		crash		target		course		defense		interopitx		attack		career		business		cyberattack		cyberattacks		bhusa
""")

digicert = tb("""infosec		security		cybersecurity		digice		healthcare		device		ransomware		data		ceificate		attack		team		ceificates		malware		learn		suppo		breach		sorry		thanks		help		contact
""")

Fortinet = tb("""security		foinet		cloud		threat		cybersecurity		network		fabric		data		today		ransomware		attack		service		accelerate		secure		digital		solution		device		organization		malware		enterprise
""")

Gemalto = tb("""gemalto		mobile		security		payment		solution		digital		secure		card		world		contactless		data		technology		service		bank		thanks		today		great		authentication		latest		year
""")

Incapsula = tb("""ddos		incapsula		security		read		attack		learn		website		cybersecurity		repo		mirai		site		cloud		bot		botnet		performance		network		imperva		webperf		threat		protection
""")

LifeLock = tb("""lifelock		help		call		identity		sorry		please		service		thanks		member		learn		theft		happy		time		online		info		best		phone		tip		hear		frustration
""")

Mantech = tb("""mantech		contract		suppo		cyber		govcon		service		event		system		year		job		veteran		security		military		today		company		task		order		engineering		list		solution
""")

McAfee = tb("""cybersecurity		cybercriminals		mpower		security		cybercrime		cyber		threat		cyberattacks		cyberattack		best		work		company		attack		world		look		data		business		industry		mcafee		skill		late		protect		time		group		conference
""")

NISTCyber = tb("""cybersecurity		cyber		national		nist		nccoe		career		colloquium		join		nice		framework		trust		cyberframework		awareness		webcast		security		nstic		chatstc		strategy		identity		month
""")

NJCybersecurity = tb("""cyber		cybersecurity		threat		cyberaware		njccic		bulletin		join		incident		security		month		ale		read		today		business		victim		infosec		attack		njcyber		advisory		repo
""")

NortonOnline = tb("""cybersecurity		cyber		cybercrime		security		cybercriminals		mostdangeroustown		business		hack		help		victim		raiseourvoices		crime		chatstc		cyberattacks		attack		cyberattack		threat		device		year		watch
""")

PaloAltoNtwks = tb("""network		alto		palo		security		week		cybersecurity		unit		learn		cloud		join		threat		news		prevention		channel		trap		webinar		today		data		next		scoop
""")

proofpoint = tb("""email		threat		infosec		proofpoint		attack		cybersecurity		office		security		fraud		compliance		ransomware		malware		socialmedia		business		protection		repo		dmarc		visibility		risk		malicious
""")

splunk = tb("""splunk		data		security		splunkconf		learn		share		splunker		blog		customer		join		analytics		time		webinar		help		week		enterprise		team		today		check		devops
""")

stanford = tb("""news		week		cyber		data		security		stanford		cybersecurity		privacy		bitcoin		facebook		work		election		internet		talk		blockchain		tech		policy		today		episode		online		bpase		apple		hack		time		year
""")

symantec = tb("""cyber		cybersecurity		symantec		security		attack		cyberattacks		ransomware		cyberattack		group		tool		cybercrime		defense		malware		business		threat		korea		cybercriminals		repo		time		integrate		espionage		live		team		state		link
""")

TheCyberSecHub = tb("""cybersecurity		infosec		cyber		security		cybercrime		cyberattacks		threat		attack		cyberwar		business		year		cybercriminals		risk		cyberattack		malware		hacker		company		repo		itsecurity		global		week		cyber-attacks		hack		target		landscape
""")

threatintel = tb("""cyber		cybersecurity		infosec		security		attack		threat		group		history		cyberattacks		throwbackthursday		social		cybercrime		espionage		dangerous		engineering		istr		woman		sho		read		cyberespionage		miss		repo		target		career		sector
""")

TrendMicro = tb("""security		reinvent		ransomware		thanks		attack		learn		detail		cloud		help		threat		malware		cybersecurity		data		issue		device		today		follow		send		great		vulnerability		trend		business		year		wannacry		begin
""")

Verisign = tb("""domain		name		smallbiz		website		business		online		learn		tip		help		verisign		click		registration		email		social		brand		today		check		medium		read		small		register		keywords		ddos		consumer		good
""")

cols = ['Document', 'Word', 'TF-IDF']
data = []
bloblist = [avgaunz, CheckPointSW, CLTCBerkeley, cyber, CyberArk, DarkReading, digicert, Fortinet, Gemalto, Incapsula, LifeLock, Mantech,McAfee, NISTCyber, NJCybersecurity, NortonOnline, PaloAltoNtwks, proofpoint, splunk, stanford, symantec, TheCyberSecHub, threatintel, TrendMicro, Verisign]
for i, blob in enumerate(bloblist):
    doc= "Document " + str(i+1)
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:20]:
        data.append((doc, word, round(score, 5)))
        result = pd.DataFrame(data, columns=cols)

#saving the tfidf results of 25 users to csv file        
result.to_csv('tfidfResults.csv')
