package edu.ufl.brainless;

import android.util.Log;
import android.view.SurfaceHolder;

public class GameThread extends Thread {
	
	private static final String TAG = GameThread.class.getSimpleName();
	
	private SurfaceHolder surfaceHolder;
	private GamePanel gamePanel;
	private boolean running;
	public void setRunning(boolean running) {
		this.running = running;
	}	
	
	public GameThread(SurfaceHolder surfaceHolder, GamePanel gamePanel) {
		super();
		this.surfaceHolder = surfaceHolder;
		this.gamePanel = gamePanel;
	}
	
	@Override
	public void run() {
		while (running) {
			long tickCount = 0L;
			Log.d(TAG, "Starting game loop");
			while (running) {
				tickCount++;
				// update game state
				// render state to screen
			}
			Log.d(TAG, "Game loop executed " + tickCount + " times");
		}
	}
}
