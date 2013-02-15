package edu.ufl.brainless;

import android.graphics.Bitmap;

public class Entity extends Sprite {
	
	// Y positions of top and bottom of bounding box. X positions of left and right of bounding box.
	protected float top, bottom, left, right;
	
	public Entity(Bitmap texture, float x, float y) {
		super(texture, x, y);
		bottom = y + texture.getHeight();
	}
}
