//////////////////////////////////////
// Created by Bagus Manuaba - 2010
// Video Feedback Front
//////////////////////////////////////
using UnityEngine;
using System.Collections;
using UnityEngine.UI;

[RequireComponent(typeof(RawImage))]
public class VideoCapture : MonoBehaviour {
	string url;
	public Texture2D cameraTexture;
	int wVideo;
	int hVideo;
	WWW www;
	bool _testwww;
	Vector2 posVideo;
	Vector2 LengVideo;
	public Camera cam;
	private RawImage canvascamera;

	// Use this for initialization
	IEnumerator Start () {
		if (cam == null) {
			cam = Camera.main;
		}

		if (cam != null) {
			// Tie this to the camera, and do not keep the local orientation.
			transform.SetParent(cam.GetComponent<Transform>(), true);
		}

		url = "http://www.sudftw.com/imageppc.php";//"http://150.229.9.117/axis-cgi/jpg/image.cgi?resolution=CIF";
		wVideo = 284 ;
		hVideo = 188 ;
		cameraTexture = new Texture2D(wVideo,hVideo);
		canvascamera = (RawImage)GetComponent<RawImage> ();

		posVideo.x =Screen.width - wVideo -60;//30; 
		posVideo.y =70;//10; 
		LengVideo.x =wVideo+20;
		LengVideo.y =hVideo+10;

		StartCoroutine (captureVideo());
		yield return 0;
	}

	IEnumerator captureVideo () {
		while (true) {

			// Start a download of the given URL
			www = new WWW(url); 
			// wait until the download is done

			yield return www; 

			if (www.error == null){

				www.LoadImageIntoTexture(cameraTexture);

				yield return 0;		
			}
		}
	}

	void LateUpdate() {
		canvascamera.texture = (Texture2D)cameraTexture;
	}


}