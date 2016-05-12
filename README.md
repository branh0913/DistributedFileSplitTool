# DistributedFileSplitTool
This project will help streamline the ability to split flat files, and send them to destinations.



Right now you can run the program like so.



python SplitServer.py --file <sample file> --split <sampple split> --prefix <output file prefix>

e.g

Let's say I have a file of 1,000 lines.   And I do the following

```bash
python SplitServer.py --file input.txt --split 100 --prefix output
```


My output will be

* output1 
* output2 
* output3 
* output4 
* output5 
* output6 
* output7 
* output8 
* output9 
* output10 



Follow along at my blog:

https://drdefenseitblog.wordpress.com/
