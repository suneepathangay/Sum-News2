from sentence_transformers import SentenceTransformer,util
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from collections import defaultdict
import pandas as pd
import numpy as np
from heapq import heapify,heappop
import networkx as nx


def return_summary(text):

    # text="On the morning of February 24th, 2022, Russian forces launched a multi-pronged invasion by land, air, and sea on Ukraine. The deadly conflict continues unabated. Even as Ukrainian forces made significant ground gains, strikes by Russia against Ukraine on civilian targets exacerbated concern for humanitarian needs in winter.One year later, 17.7 million people need humanitarian assistance and nearly 8 million refugees from Ukraine have been recorded across Europe. In Ukraine, 6.3 million people are internally displaced, and 6.9 million people are sheltering in place. The UN Human Rights Monitoring Mission in Ukraine reports that from February 24 to December 26, 2022, 6,884 civilians in Ukraine had been killed and 10,974 injured. The real numbers are likely much higher.A year of war has caused widespread destruction, reducing some cities to rubble, damaging or destroying hundreds of thousands of homes along with critical infrastructure and leaving millions of people with limited or no access to electricity, water or heat. Many people are living either in collective centers or damaged buildings, without basic needs for daily life and vulnerable to a range of health threats. Internally displaced persons living in collective centers are most at risk with the majority being women, children, the elderly, and people with disabilities. Overall, an estimated 14.5 million people in Ukraine need health assistance."

    ##defining our model

    model = SentenceTransformer('all-MiniLM-L6-v2')


    #removing stop words from the text and splitting them up.



    list_stopwords=stopwords.words('english')

    sentence_list=sent_tokenize(text)

    nostop_senteces=[]

    for sentence in sentence_list:
        formatted_sent=""
        for words in sentence.lower().split(' '):
            if words not in list_stopwords:
                formatted_sent=formatted_sent+' '+words
        nostop_senteces.append(formatted_sent)

    # print(nostop_senteces)
        

    [' morning february 24th, 2022, russian forces launched multi-pronged invasion land, air, sea ukraine.', 
    ' deadly conflict continues unabated.', 
    ' even ukrainian forces made significant ground gains, strikes russia ukraine civilian targets exacerbated concern humanitarian needs winter.one year later, 17.7 million people need humanitarian assistance nearly 8 million refugees ukraine recorded across europe.', 
    ' ukraine, 6.3 million people internally displaced, 6.9 million people sheltering place.', 
    ' un human rights monitoring mission ukraine reports february 24 december 26, 2022, 6,884 civilians ukraine killed 10,974 injured.', 
    ' real numbers likely much higher.a year war caused widespread destruction, reducing cities rubble, damaging destroying hundreds thousands homes along critical infrastructure leaving millions people limited access electricity, water heat.', 
    ' many people living either collective centers damaged buildings, without basic needs daily life vulnerable range health threats.', 
    ' internally displaced persons living collective centers risk majority women, children, elderly, people disabilities.', 
    ' overall, estimated 14.5 million people ukraine need health assistance.']



    sentence_embeddings=model.encode(nostop_senteces,convert_to_tensor=True)

    # print(sentence_embeddings)


    #function to calcualte the cosine similiartiy score


    def cosine_simialrit(vector1,vector2):
        cosine_score=util.cos_sim(vector1,vector2)
        return cosine_score

    # print(cosine_simialrit(sentence_embeddings[0],sentence_embeddings[1]))


    #precurosr for oour graph
    # similairty_matrix=defaultdict(list)

    ##create pandas dataframe


    sim_matrix=np.zeros([len(sentence_embeddings),len(sentence_embeddings)])


    for i in range(len(sentence_embeddings)):
        for j in range(len(sentence_embeddings)):
            if i!=j:
                vec1=sentence_embeddings[i]
                vec2=sentence_embeddings[j]
                similairty=cosine_simialrit(vec1,vec2)
    #           
                sim_matrix[i][j]=similairty

    # print(similairty_matrix)

    # print(sim_matrix)
    
    


    # vector_scores=[]

    # for i in range(len(sim_matrix)):
    #     total_score=0
    #     for scores in sim_matrix[i]:
    #         total_score=total_score+scores
    #     vector_scores.append((-total_score,i))

    # # print(vector_scores)

    # heapify(vector_scores)

    # summary=""

    # for i in range(4):
    #     index=heappop(vector_scores)
    #     print(index[1])
    #     sentence=sentence_list[index[1]]
    #     summary=summary+sentence

    # # print(summary)
    # return summary
    
    nx_graph = nx.from_numpy_array(sim_matrix)
    scores = nx.pagerank(nx_graph)
    
    list_scores=[]
    
    for score in scores:
        list_scores.append((-scores[score],score))
    
    heapify(list_scores)
    
    summary=""
    
    for i in range(3):
        index=heappop(list_scores)
        index=index[1]
        summary=summary+sentence_list[index]
        
    

    return summary
    
        
        
    
    
        





            
        
            
