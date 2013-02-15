package edu.ufl.brainless;

import android.graphics.Bitmap;

public class Sprite {
	protected Bitmap texture;
	protected float x;
	protected float y;
	
	public Sprite(Bitmap texture, float x, float y) {
		this.texture = texture;
		this.x = x;
		this.y = y;
	}
	
	public void draw() {
		// Draw texture at position
	}
}
