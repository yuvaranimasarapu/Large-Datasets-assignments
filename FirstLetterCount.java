//package org.myorg;
import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import java.util.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;
import java.lang.Character;

public class WordCount {
    public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);
		private Text word = new Text();
		private boolean caseSensitive = false;

        public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException {
            String line = value.toString();
			if (!caseSensitive) {
				line = line.toLowerCase();
			}
            StringTokenizer tokenizer = new StringTokenizer(line);
			char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
            while (tokenizer.hasMoreTokens()) {
				String word1 = tokenizer.nextToken();
                //word.set(tokenizer.nextToken());
				Character letter = new Character(word1.charAt(0));
				//char firstletter = letter.charValue();
				for(int i=0; i < 26; i++)
				{
					if(letter.charValue() == alphabet[i])
					{
						String templetter = letter.toString();
                        word.set(templetter);
                        output.collect(word,one);
					}
				}					
            }
}
}

    public static class Reduce extends MapReduceBase implements Reducer<Text, IntWritable, Text, IntWritable> {
        public void reduce(Text key, Iterator<IntWritable> values, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException {
            int sum = 0;
            while (values.hasNext()) {
                sum += values.next().get();
            }
            output.collect(key, new IntWritable(sum));
        }
    }

    public static void main(String[] args) throws Exception {
        JobConf conf = new JobConf(WordCount.class);
        conf.setJobName("wordcount");

        conf.setOutputKeyClass(Text.class);
        conf.setOutputValueClass(IntWritable.class);

        conf.setMapperClass(Map.class);
        conf.setReducerClass(Reduce.class);
		
		conf.setInputFormat(TextInputFormat.class);
        conf.setOutputFormat(TextOutputFormat.class);

        FileInputFormat.setInputPaths(conf, new Path(args[0]));
        FileOutputFormat.setOutputPath(conf, new Path(args[1]));

        JobClient.runJob(conf);
    }
}

