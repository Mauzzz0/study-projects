package com.mirea.semak.lifecycleactivity;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.PersistableBundle;
import android.util.Log;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.i("tag", "onCreate()");
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onStart() {
        super.onStart();
        Log.i("tag", "onStart()");
    }

    @Override
    protected void onRestoreInstanceState(@NonNull Bundle savedInstanceState) {
        super.onRestoreInstanceState(savedInstanceState);
        Log.i("tag", "onrestore");
    }

    @Override
    public void onPostCreate(@Nullable Bundle savedInstanceState, @Nullable PersistableBundle persistentState) {
        super.onPostCreate(savedInstanceState, persistentState);
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Log.i("tag", "onrestart()");
    }

    @Override
    protected void onPostResume() {
        super.onPostResume();
        Log.i("tag", "onpostresume()");
    }

    @Override
    public void onAttachedToWindow() {
        super.onAttachedToWindow();
        Log.i("tag", "onattachedwindow()");
    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.i("tag", "onpause()");
    }

    @Override
    public void onSaveInstanceState(@NonNull Bundle outState, @NonNull PersistableBundle outPersistentState) {
        super.onSaveInstanceState(outState, outPersistentState);
        Log.i("tag", "onsaveinstancestate()");
    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.i("tag", "onstop()");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.i("tag", "ondestroy()");
    }

    @Override
    public void onDetachedFromWindow() {
        super.onDetachedFromWindow();
        Log.i("tag", "ondetachedfromwindow()");
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.i("tag", "onresume()");
    }
}