from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd
from langchain_community.llms import OpenAI
def query_agent(data, query):
    df = pd.read_csv(data)
    llm = OpenAI()
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    return agent.run(query)
# And somewhere in your app.py, after you have processed the DataFrame


#from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent 
#import pandas as pd 
#from langchain_community.llms import OpenAI
#def query_agent(data, query):
 #   df=pd.read_csv(data)
  #  llm = OpenAI()
   # agent= create_pandas_dataframe_agent(llm,df,verbose=True)
    #return agent.run(query)