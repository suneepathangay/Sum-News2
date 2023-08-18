from sentence_transformers import SentenceTransformer,util
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from collections import defaultdict
import pandas as pd
import numpy as np
from heapq import heapify,heappop
import networkx as nx

import re



def return_summary(text):

    #text="On the morning of February 24th, 2022, Russian forces launched a multi-pronged invasion by land, air, and sea on Ukraine. The deadly conflict continues unabated. Even as Ukrainian forces made significant ground gains, strikes by Russia against Ukraine on civilian targets exacerbated concern for humanitarian needs in winter.One year later, 17.7 million people need humanitarian assistance and nearly 8 million refugees from Ukraine have been recorded across Europe. In Ukraine, 6.3 million people are internally displaced, and 6.9 million people are sheltering in place. The UN Human Rights Monitoring Mission in Ukraine reports that from February 24 to December 26, 2022, 6,884 civilians in Ukraine had been killed and 10,974 injured. The real numbers are likely much higher.A year of war has caused widespread destruction, reducing some cities to rubble, damaging or destroying hundreds of thousands of homes along with critical infrastructure and leaving millions of people with limited or no access to electricity, water or heat. Many people are living either in collective centers or damaged buildings, without basic needs for daily life and vulnerable to a range of health threats. Internally displaced persons living in collective centers are most at risk with the majority being women, children, the elderly, and people with disabilities. Overall, an estimated 14.5 million people in Ukraine need health assistance."

    ##defining our model
    
  

    model = SentenceTransformer('sentence-transformers/sentence-t5-base')
    
    #text="ISLAMABAD (AP) — Pakistan’s finance minister on Thursday said China has rolled over a $2.4 billion loan for the cash-strapped Islamic nation for two years, a move aimed at helping the country overcome one of its worst economic crises.The latest extension in loan maturities by Beijing was a boost to Pakistan’s fragile foreign exchange reserves, which are still only enough to pay the import bill for a period of two months.In a post on the X platform, formerly known as Twitter, Ishaq Dar said the Chinese EXIM Bank rolled over for two years the “principal amounts” of the $2.4 billion loan, which Islamabad was to have paid back in 2024 and 25.China is a longtime friend of Pakistan and it has played a key role in helping Pakistan avoid a default this year, though there has been concern in the country about how Islamabad would repay the growing Chinese loans.Some analysts in Pakistan call it a debt trap, though the government says there is no truth to such assumptions. The latest development comes two weeks after the International Monetary Fund deposited a much-awaited first installment of $1.2 billion in Pakistan’s central bank under a bailout to help Pakistan avoid default. It bolstered Pakistan’s foreign exchange reserves, which shrank to $4 billion recently, raising fears of a default.Pakistan’s foreign exchange reserves jumped to $14 billion last week.The IMF loans had been on hold since December mainly because of non-compliance with the terms of the previous $6 billion bailout by Pakistan. It forced Pakistan to seek financial help from friendly countries like China, Saudi Arabia and the United Arab Emirates.Pakistan has said China in recent months gave it $5 billion in loans to avoid a default.In Pakistan, Beijing is bankrolling the so-called China-Pakistan Economic Corridor, a sprawling package that includes a multitude of mega projects such as road construction, power plants and agriculture.China has already invested billions of dollars in Pakistan and the package is considered a lifeline for the country, which had struggled until June to overcome the economic crisis when Pakistan and the IMF agreed to a new $3 billion bailout.On Wednesday, Prime Minister Shehbaz Sharif said that Pakistan no longer faces the risk of default.Since coming to power in April 2022, Sharif has blamed alleged corruption under former Prime Minister Imran Khan for Pakistan’s economic downturn.Sharif is likely to step down next month when the current parliament completes its five-year term, paving the way for new parliamentary elections, which will be held under the supervision of an interim government that will be installed next month when the National Assembly is dissolved. "
    
    #text="On the morning of February 24th, 2022, Russian forces launched a multi-pronged invasion by land, air, and sea on Ukraine. The deadly conflict continues unabated. Even as Ukrainian forces made significant ground gains, strikes by Russia against Ukraine on civilian targets exacerbated concern for humanitarian needs in winter.One year later, 17.7 million people need humanitarian assistance and nearly 8 million refugees from Ukraine have been recorded across Europe. In Ukraine, 6.3 million people are internally displaced, and 6.9 million people are sheltering in place. The UN Human Rights Monitoring Mission in Ukraine reports that from February 24 to December 26, 2022, 6,884 civilians in Ukraine had been killed and 10,974 injured. The real numbers are likely much higher.A year of war has caused widespread destruction, reducing some cities to rubble, damaging or destroying hundreds of thousands of homes along with critical infrastructure and leaving millions of people with limited or no access to electricity, water or heat. Many people are living either in collective centers or damaged buildings, without basic needs for daily life and vulnerable to a range of health threats. Internally displaced persons living in collective centers are most at risk with the majority being women, children, the elderly, and people with disabilities. Overall, an estimated 14.5 million people in Ukraine need health assistance."
        
     


    #removing stop words from text and splitting them up.



    list_stopwords=stopwords.words('english')

    sentence_list=re.split('(?<=[^A-Z].[.?]) +(?=[A-Z])',text)
    #sentence_list=sent_tokenize(text)
    

    nostop_senteces=[]

    for sentence in sentence_list:
        formatted_sent=""
        for words in sentence.lower().split(' '):
            if words not in list_stopwords:
                formatted_sent=formatted_sent+' '+words
        nostop_senteces.append(formatted_sent)
    
    
    
    sentence_embeddings=model.encode(nostop_senteces,convert_to_tensor=True)
    
    
    
    def cosine_simialrit(vector1,vector2):
        cosine_score=util.cos_sim(vector1,vector2)
        return cosine_score
    
    

    sim_matrix=np.zeros([len(sentence_embeddings),len(sentence_embeddings)])
    
    for i in range(len(sentence_embeddings)):
        for j in range(len(sentence_embeddings)):
            if i!=j:
                vec1=sentence_embeddings[i]
                vec2=sentence_embeddings[j]
                similairty=cosine_simialrit(vec1,vec2)
    #           
                sim_matrix[i][j]=similairty
    
    nx_graph = nx.from_numpy_array(sim_matrix)
    
    scores = nx.pagerank(nx_graph)
    
    list_scores=[]
    
    for score in scores:
        list_scores.append((-scores[score],score))
    
    heapify(list_scores)
    
    summary=""
    
    print(list_scores) 
    
    
    
 
    
    
    for i in range(4):
        print(i)
        if list_scores:
            index=heappop(list_scores)
            index=index[1]
            summary=summary+sentence_list[index]
        else:
            return summary
    
    
    return summary
    
    
    
    
        





            
        
            
