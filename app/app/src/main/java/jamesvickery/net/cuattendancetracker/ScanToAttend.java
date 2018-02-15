package jamesvickery.net.cuattendancetracker;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import android.support.design.widget.Snackbar;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.Result;

import java.util.Collections;
import java.util.List;

import me.dm7.barcodescanner.zxing.ZXingScannerView;

import static android.Manifest.permission.CAMERA;

public class ScanToAttend extends AppCompatActivity implements ZXingScannerView.ResultHandler {

    // TODO: This class needs to be tidied up a lot.

    private static final int REQUEST_CAMERA = 1;
    private ZXingScannerView scannerView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        scannerView = new ZXingScannerView(this);
        // Set barcode format: QR codes
        List<BarcodeFormat> formats = Collections.singletonList(BarcodeFormat.QR_CODE);
        scannerView.setFormats(formats);
        setContentView(scannerView);

        setTitle("Sign into lecture");

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            if (!checkPermission()) {
                requestPermission();
            }
        }

        Snackbar.make(findViewById(android.R.id.content), "Scan QR code to sign into lecture", Snackbar.LENGTH_INDEFINITE).show();
    }

    private boolean checkPermission() {
        return (ContextCompat.checkSelfPermission(ScanToAttend.this, CAMERA) == PackageManager.PERMISSION_GRANTED);
    }

    private void requestPermission() {
        ActivityCompat.requestPermissions(this, new String[]{CAMERA}, REQUEST_CAMERA);
    }

    private void explainPermission() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            if (shouldShowRequestPermissionRationale(CAMERA)) {
                AlertDialog alert = new AlertDialog.Builder(ScanToAttend.this)
                        .setMessage("CU Timetable Tracker needs to access your camera to scan into lectures")
                        .setPositiveButton("OK", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                                    requestPermissions(new String[]{CAMERA}, REQUEST_CAMERA);
                                }
                            }
                        })
                        .setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                finish();
                            }
                        })
                        .create();
                alert.show();
            }
        }
    }

    public void onRequestPermissionsResult(int requestCode, String permissions[], int grantResults[]) {
        switch (requestCode) {
            case REQUEST_CAMERA:
                if (grantResults.length > 0) {
                    boolean cameraAccepted = grantResults[0] == PackageManager.PERMISSION_GRANTED;
                    if (!cameraAccepted) {
                        explainPermission();
                    }
                }
                break;
        }
    }

    @Override
    public void onResume() {
        super.onResume();
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            if (checkPermission()) {
                if (scannerView == null) {
                    scannerView = new ZXingScannerView(this);
                    setContentView(scannerView);
                }
                scannerView.setResultHandler(this);
                scannerView.startCamera();
            }
        }
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        scannerView.stopCamera();
    }

    @Override
    public void handleResult(Result result) {
        final String scanResult = result.getText();

        Intent intent = new Intent(this, RegisterAttendance.class);
        intent.putExtra("event_id", scanResult);
        startActivity(intent);

        finish();
    }
}
