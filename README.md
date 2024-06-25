This notebook walks through connecting a LangChain email to the Gmail API.

To use this toolkit, you will need to set up your credentials explained in the Gmail API docs. 
Once you've downloaded the credentials.json file, 
you can start using the Gmail API. Once this is done, 
we'll install the required libraries.

%pip install --upgrade --quiet  google-api-python-client > /dev/null
%pip install --upgrade --quiet  google-auth-oauthlib > /dev/null
%pip install --upgrade --quiet  google-auth-httplib2 > /dev/null
%pip install --upgrade --quiet  beautifulsoup4 > /dev/null # This is optional but is useful for parsing HTML messages

pip install -U langchain-community
