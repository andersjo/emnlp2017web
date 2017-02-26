---
layout: default
nickname: GraphRep
title: "Graph-based Text Representations: Boosting Text Mining, NLP and Information Retrieval with Graphs"
presenters: Fragkiskos Malliaros, Michalis Vazirgiannis
slot: Day 1, afternoon
blurb: "The goal of this tutorial is to offer a comprehensive presentation of recent methods that rely on graph-based text representations to deal with various tasks in NLP and IR. We will describe basic as well as novel graph theoretic concepts and we will examine how they can be applied in a wide range of text-related application domains, including IR, text categorization and keyword extraction."
---

<div class="section tutorial" markdown="1">

## Graph-based Text Representations: Boosting Text Mining, NLP and Information Retrieval with Graphs

### Objectives

Graphs or networks have been widely used as modeling tools in Natural Language Processing (NLP), Text Mining (TM) and Information Retrieval (IR). Traditionally, the unigram bag-of-words representation is applied; that way, a document is represented as a multiset of its terms, disregarding dependencies between the terms. Although several variants and extensions of this modeling approach have been proposed (e.g., the n-gram model), the main weakness comes from the underlying term independence assumption. The order of the terms within a document is completely disregarded and any relationship between terms is not taken into account in the final task (e.g., text categorization). Nevertheless, as the heterogeneity of text collections is increasing (especially with respect to document length and vocabulary), the research community has started exploring different document representations aiming to capture more fine-grained contexts of co-occurrence between different terms, challenging the well-established unigram bag-of-words model. To this direction, graphs constitute a well-developed model that has been adopted for text representation.  The goal of this tutorial is to offer a comprehensive presentation of recent methods that rely on graph-based text representations to deal with various tasks in NLP and IR. We will describe basic as well as novel graph theoretic concepts and we will examine how they can be applied in a wide range of text-related application domains.


All the material associated to the tutorial will be available at:  [http://fragkiskosm.github.io/projects/graph_text_tutorial](http://fragkiskosm.github.io/projects/graph_text_tutorial)

### Tutorial Overview

#### Part I: Graph-theoretic Concepts and Graph-based Text Representations

In the first part, we will start by providing an introduction to basic graph-theoretic concepts and algorithms, including the ones of node centrality, graph degeneracy and frequent subgraph mining. Then, we will present various graph-based text representations. In particular, due to the strong modeling capabilities of graphs, the vertices and edges can capture a plethora of linguistic units. The vertices can correspond to paragraphs, sentences, phrases, words and syllables. The edges of the graph can capture various types of relationships between two vertices, including co-occurrence within a window over the text, syntactic relationship as well as semantic relationship. Furthermore, depending on the task and the granularity level that we are interested in, the graph itself can represent different entities, such as a sentence, a single document, multiple documents or even the entire document collection.


####  Part II: Information Retrieval

In the second part, we will examine applications of graph-based text representations in the task of Information Retrieval. In particular, we will present methods that, building on the so-called graph-of-words model - where graph’s vertices correspond to terms linked by co-occurrence or grammatical modification -apply node ranking (or centrality) criteria (such as the ones of degree and PageRank), in order to determine term weights that achieve state-of-the-art retrieval results.


####  Part III: Keyword - Keyphrase Extraction and Text Summarization

In the third part, we will elaborate on how graph-based text representations along with sophisticated graph theoretic tools can be used to identify informative keywords and keyphrases. In particular, we will present methodologies that apply various graph centrality criteria to determine good keywords (for example, TextRank algorithm determines the importance of keywords based on the PageRank score of the terms). More recently, it was shown that keywords are better captured by dense subgraphs of the graph-of-words, compared to high centrality criteria; that way, keywords can be extracted efficiently by applying graph degeneracy methods and in particular the so-called k-core and K-truss graph decompositions. We will also present how word embeddings scores can be utilized in graph-based representations for keyword extraction. Lastly, we will present how graph-based keyword extraction and summarization techniques can be used for real-time novelty and event detection in text streams, such as Twitter.


#### Part IV: Text Categorization

In the fourth part of the tutorial, we will examine how graph-based document representations can be utilized in the text categorization task. One straightforward approach that performs well in practice is to replace the frequency-based term weighting criteria with graph-based ones (similar to the approach that has been applied in the domain of IR). Another line of research that will be covered by the tutorial, includes the one of subgraph extraction from the graph-of-words, using frequent subgraph mining algorithms (e.g., gSpan algorithm), that subsequently are used as features in the text classifier. We will also examine how the graph-based structure of documents can be applied as a regularization factor in text categorization.


### Structure

#### Part I: Graph-theoretic Concepts and Graph-based Text Representations [40 min]

* Basic graph definitions: node centrality criteria, graph degeneracy, frequent subgraph mining, basics on graph kernels
* Graph-of-words concept
* Graph construction issues: semantics of nodes and edges, edge directionality and weights, graph construction trade-offs

#### Part II: Information Retrieval [20 min]

* Graph-based term weighting in IR
* TW and TW-IDF weighting functions

####  Part III: Keyword - Keyphrase Extraction and Text Summarization [50 min]

* Clustering-based methods
* TextRank and PageRank-based approaches for single topic keyword extraction, HITS algorithm for keyword extraction
* Node centrality criteria for keyword and keyphrase extraction
* Graph degeneracy-based methods
* Keyphrase annotation
* Degeneracy-based event detection in Twitter streams
* Software demonstration

#### Part IV: Text Categorization [35 min]

* Graph-based term weighting for TC
* Frequent subgraphs as categorization features
* Term graph models for TC
* Graph matching approaches
* Graph-based regularization for TC

#### Part V: Final Remarks and Future Research Directions [20 min]

* Graph kernels for document similarity and categorization
* Dense subgraphs for keyword selection
* Multi-topic keyword extraction


### About the Speakers

**Fragkiskos D. Malliaros** ([web page](http://fragkiskos.me)) is currently a data science postdoctoral scholar in the Department of Computer Science and Engineering at UC San Diego and member of the Artificial Intelligence group. Right before that, he was a postdoctoral researcher in Ecole Polytechnique, France from where he also received his Ph.D. degree in 2015. He obtained his Diploma and his M.Sc. degree from the University of Patras, Greece in 2009 and 2011 respectively. He is the recipient of the 2012 Google European Doctoral Fellowship in Graph Mining and the 2015 Thesis Prize by Ecole Polytechnique. During the summer of 2014, he was a research intern at the Palo Alto Research Center (PARC), working on anomaly detection in social networks. His research interests span the broad area of data science, with focus on graph mining, social network analysis, applied machine learning and natural language processing.


**Michalis Vazirgiannis** ([web page](http://www.lix.polytechnique.fr/~mvazirg)) is a Professor in Ecole Polytechnique, France and the leader of the Data Science and Mining (DaSciM) team. He holds a degree in Physics, a M.Sc. in Robotics, both from University of Athens, Greece, and a M.Sc. in Knowledge Based Systems from Heriot-Watt University (Edinburgh, UK). He acquired his Ph.D. degree from the Dept. of Informatics, University of Athens. He has worked as a researcher in different places: NTUA, GMD-IPSI (currently Frauhofer-IPSI), Germany Fern-Universitaet Hagen, in project VERSO (later GEMO) in INRIA/Paris, in IBM India Research Laboratory and in MPI fur Informatik (Saarbruecken, Germany). He held a Marie Curie Intra-European fellow in area of P2P Web Search, hosted by INRIA FUTURS, Paris. His current research interests are on graph mining, text mining and recommendation algorithms. He is chairing the ''AXA Data Science'' chair in Ecole Polytechnique and has collaborations with the industry including Google and Airbus.


</div>
