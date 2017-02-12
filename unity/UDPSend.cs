using UnityEngine;
using System.Collections;

using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading;

public class UDPSend : MonoBehaviour
{
	private static int localPort;
	//private GameObject MainCamera;

	// prefs
	private string IP;  // define in init
	public int port;  // define in init

	// "connection" things
	IPEndPoint remoteEndPoint;
	UdpClient client;

	// gui
	string strMessage="";
	double CameraDirectionCheck = 0.0;


	// call it from shell (as program)
	private static void Main()
	{
		UDPSend sendObj=new UDPSend();
		sendObj.init();

		// as server sending endless
		//sendObj.sendEndless(" endless infos \n");

	}
	// start from unity3d
	public void Start()
	{
		init();
	}

	void Update()
	{
		double CameraDirection = GameObject.Find("Main Camera").GetComponent<Transform> ().rotation.y;
		if (CameraDirectionCheck < CameraDirection) 
		{
			sendString("turn right\n"); //send pin 1
			CameraDirectionCheck = CameraDirection;
		}
		else if (CameraDirectionCheck > CameraDirection) 
		{
			sendString("turn left\n"); //sen pin 2
			CameraDirectionCheck = CameraDirection;
		}
		else
		{
			sendString("stop\n"); //sen pin 0
			CameraDirectionCheck = CameraDirection;
		}

	}
		

	// init
	public void init()
	{
		print("UDPSend.init()");

		// define
		IP="127.0.0.1";
		port=5005;

		// ----------------------------
		// Sender
		// ----------------------------
		remoteEndPoint = new IPEndPoint(IPAddress.Parse(IP), port);
		client = new UdpClient();

		// status
		print("Sending to "+IP+" : "+port);
		print("Testing: nc -lu "+IP+" : "+port);

	}
		

	// sendData
	private void sendString(string message)
	{
		try
		{
			//if (message != "")
			//{

			// Daten mit der UTF8-Kodierung in das Binärformat kodieren.
			byte[] data = Encoding.UTF8.GetBytes(message);

			// Den message zum Remote-Client senden.
			client.Send(data, data.Length, remoteEndPoint);
			//}
		}
		catch (Exception err)
		{
			print(err.ToString());
		}
	}


	// endless test
	private void sendEndless(string testStr)
	{
		do
		{
			sendString(testStr);


		}
		while(true);

	}

}
