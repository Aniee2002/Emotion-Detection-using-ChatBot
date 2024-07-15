# Emotion-Detection-using-ChatBot
This chatbot will ask you some questions & based on your replies it will detect your emotion.
Model_code contains ML code to train the model which is stored in ML_model.h5 file. We are using flask(app.py) to link trained model to our chatbot website
# Methodology
We begin by asking the user some fundamental questions and then taking the input as text data. To input the data to our NN (Neural Network) Model we'll need some preprocessing. The first step is to tokenize our texts and count unique tokens. Tokenization is the process of dividing a text or a series of characters into smaller parts, known as tokens, which are typically words, phrases, or symbols. Tokenization's purpose is to make text analysis easier by splitting it into meaningful units that can be handled by a machine learning algorithm or other software. Then the padding is done. Padding is a machine learning approach that adds zeros or another value to a dataset to make all of the inputs identical in length. Padding is very frequent in the setting of recurrent neural networks (RNNs), such as long short-term memory (LSTM) and gated recurrent unit (GRU) networks, which are commonly employed for processing sequential data such as text, audio, or time series data. Labels have to be converted to integers and categorized. 
Basic preprocessing and tokenization using NLTK to double-check that sentences are properly split into words. We could also add stop word removal but steps like stemming, or lemmatization are not needed since we are using word2vec, and words with the same stem can have a different meaning. We Imported pre-trained word2vec from the file and created an embedding matrix, later mapped each word in our corpus to an existing word vector. We used 300-dimensional w2v pre-trained on Wikipedia articles. For creating a neural network pipeline embedding layer is formed. An embedding layer is a sort of neural network layer that is used to convert categorical data into numerical data in the form of dense vectors, or embeddings. The layer maps each category to a fixed-size vector, with each element of the vector representing a category feature. Neural networks can efficiently capture the semantic relationships between words by utilizing embeddings, allowing them to generalize to new data and perform well on a range of NLP tasks. During training, the parameters of the embedding layer are learned using techniques like backpropagation and stochastic gradient descent. We will use 300-dimensional word vectors pre-trained on Wikipedia articles. We can also train the w2v model with our data, however, our dataset is quite small, and trained word vectors might not be as good as using pre-trained W2V.In the model pipeline, the input is the first N words of each text (with proper padding). The first level creates embedding of words, using vocabulary with a certain dimension, and a given size of embeddings. We will use a 1D convolutional neural network to extract features from our data. The result of each convolution will fire when a special pattern is detected. By varying the size of the kernels and concatenating their outputs, you’re allowing yourself to detect patterns of multiple sizes (2, 3, or 5 adjacent words). The output level has several neurons equal to the classes of the problem and a “SoftMax” activation function. Then the model is trained, and the results are evaluated. 
We used HTML and CSS to design a homepage for our website that greets and chats with the user. During the conversation, the user will be asked a series of questions from an array. After collecting all of the information, we construct a string by merging all of the inputs. The learned model, which was trained with Keras and TensorFlow, then processes the input. The algorithm then predicts the user's sentiment and a response is created and presented on screen. 

# Results
Confusion Matrix:-

![image](https://github.com/Aniee2002/Emotion-Detection-using-Chatbot/assets/88838805/891a292e-e14e-4663-a301-0903897f407d)


Model accuracy:-

![image](https://github.com/Aniee2002/Emotion-Detection-using-Chatbot/assets/88838805/37f8fa53-a200-4c68-84ca-218cc4c40e1e)

Model loss:-

![image](https://github.com/Aniee2002/Emotion-Detection-using-Chatbot/assets/88838805/0aff81d8-8bbd-415f-8acc-740181cdfe4c)



