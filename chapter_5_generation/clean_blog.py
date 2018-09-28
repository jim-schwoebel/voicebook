'''
================================================ 
##            VOICEBOOK REPOSITORY            ##      
================================================ 

repository name: voicebook 
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/voicebook 
author: Jim Schwoebel 
author contact: js@neurolex.co 
description: a book and repo to get you started programming voice applications in Python - 10 chapters and 200+ scripts. 
license category: opensource 
license: Apache 2.0 license 
organization name: NeuroLex Laboratories, Inc. 
location: Seattle, WA 
website: https://neurolex.ai 
release date: 2018-09-28 

This code (voicebook) is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

================================================ 
##               LICENSE TERMS                ##      
================================================ 

Copyright 2018 NeuroLex Laboratories, Inc. 

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

================================================ 
##               SERVICE STATEMENT            ##        
================================================ 

If you are using the code written for a larger project, we are 
happy to consult with you and help you with deployment. Our team 
has >10 world experts in Kafka distributed architectures, microservices 
built on top of Node.js / Python / Docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ js@neurolex.co. 

================================================ 
##                CLEAN_BLOG.PY               ##    
================================================ 

This script formats blog posts for use by the textgenrnn library.

I hate XML parsing, so just cleaning the script with a while loop.

Download the blog posts @ this link:
http://u.cs.biu.ac.il/~koppel/BlogCorpus.htm
'''
import os, random 

curdir=os.getcwd()
os.chdir('./data/blogs')
listdir=os.listdir()

random.shuffle(listdir)
posts=list()
for i in range(len(listdir)):
    # get 1000 blogs mined 
    if i == 100:
        break
    try:
        g=open(listdir[i]).read()
        while g.count('</post>')!=0:
            i1=g.find('<post>')+len('<post>')
            i2=g.find('</post>')
            post=g[i1:i2].replace('\n',' ').replace('  ','')
            posts.append(post[1:])
            g=g[i2+len('</post>'):]
    except:
        pass

# now we have a ton of posts and can output them to text file
os.chdir(curdir)
bpost=open('blogposts.txt','w')
for i in range(len(posts)):
    bpost.write(posts[i])
    bpost.write('\n')
bpost.close()

    
