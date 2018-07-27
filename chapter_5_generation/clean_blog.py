'''
clean_blog.py 

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

    
