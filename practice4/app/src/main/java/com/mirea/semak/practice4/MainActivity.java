package com.mirea.semak.practice4;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    int c = 0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView infoTextView = findViewById(R.id.textView);
        Thread maThrd = Thread.currentThread();
        infoTextView.setText("thrd: " + maThrd.getName());
        maThrd.setName("MireaThread");
        infoTextView.append("\n New thrd name: " + maThrd.getName());
    }
    public void onClick(View view) {
        Runnable runnable = new Runnable() {
            public void run() {
                int numberThread = c++;
                Log.i("ThreadProject", "started thrd №" + numberThread);
                long endTime = System.currentTimeMillis()
                        + 20 * 1000;
                while (System.currentTimeMillis() < endTime) {
                    synchronized (this) {
                        try {
                            wait(endTime -
                                    System.currentTimeMillis());
                        } catch (Exception e) {
                        }
                    }
                }
                Log.i("ThreadProject", "Thrd complete № " + numberThread);
            }
        };
        Thread thread = new Thread(runnable);
        thread.start();
    }
}