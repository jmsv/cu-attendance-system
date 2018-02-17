package jamesvickery.net.cuattendancetracker;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.FormBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;
import okhttp3.ResponseBody;

public class RegisterAttendance extends AppCompatActivity {

    String eventId = "";
    TextView textViewEventId;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        String eventId = "";
        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            eventId = extras.getString("event_id");
        }

        setContentView(R.layout.activity_register_attendance);

        Button buttonBackHome = findViewById(R.id.buttonBackHome);
        buttonBackHome.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        textViewEventId = findViewById(R.id.textViewEventId);
        textViewEventId.setText("signing into: " + eventId);

        registerAttendancePost(eventId);
    }

    void registerAttendancePost(String event_id) {
        OkHttpClient client = new OkHttpClient();

        RequestBody formBody = new FormBody.Builder()
                .add("user", "6666666")
                .add("event", event_id)
                .build();

        Request request = new Request.Builder()
                .url("https://cu-attendance.net/api/register-attendance")
                .post(formBody)
                .build();

        // TODO: Better error checking in the http request below

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                try (ResponseBody responseBody = response.body()) {
                    if (!response.isSuccessful())
                        throw new IOException("Unexpected code " + response);

//                    Headers responseHeaders = response.headers();
//                    for (int i = 0, size = responseHeaders.size(); i < size; i++) {
//                        // Toast doesn't work here
//                        // responseHeaders.name(i) + ": " + responseHeaders.value(i)
//                    }

//                    // responseBody.string()

                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            textViewEventId.setText(textViewEventId.getText() + "... success!");
                        }
                    });
                }
            }
        });
    }
}
