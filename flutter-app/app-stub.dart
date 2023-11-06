import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:math';
//import 'package:nfc_manager/nfc_manager.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  MyAppState createState() => MyAppState();
}

class MyAppState extends State<MyApp> {
  final TextEditingController apiKeyController = TextEditingController();
  final TextEditingController conversationIdController =
      TextEditingController();

  String _log = '';
  bool _isLogging = false;
  Timer? _timer;

  void _addToLog(String event) {
    setState(() {
      _log += '$event\n';
    });
  }

  void _startListening() {
    // TODO: Validate api key and convo id fields before starting.
    _timer = Timer.periodic(const Duration(seconds: 5), (timer) {
      final mockUserId = Random().nextInt(100);
      // TODO: Get the actual voteType from SegmentedButton.
      final voteType = "agree";
      _addToLog('Detected user $mockUserId. Voted xxx.');
      print("POST Authorization:${apiKeyController.text} userId=$mockUserId voteType=$voteType https://example.com/conversations/${conversationIdController.text}/votes/active");
    });
//     NfcManager.instance.startSession(onDiscovered: (NfcTag tag) async {
//       final uri = tag.data['uri'];
//       if (uri != null) {
//         final userId = uri.queryParameters['user_id'];
//         _addToLog('Detected user $userId');
//       }
//     });
  }

  void _stopListening() {
    _timer?.cancel();
    _timer = null;
  }

  void _toggleListening() {
    setState(() {
      if (_isLogging) {
        // Stop logging
        _isLogging = false;
        _stopListening();
      } else {
        // Start logging
        _isLogging = true;
        _startListening();
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            children: [
              TextField(
                controller: apiKeyController,
                decoration: const InputDecoration(
                  labelText: 'API Key',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 8),
              TextField(
                controller: conversationIdController,
                decoration: const InputDecoration(
                  labelText: 'Conversation ID',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 8),
              SegmentedButton(
                segments: const <ButtonSegment>[
                  ButtonSegment(value: 0, label: Text('Agree')),
                  ButtonSegment(value: 1, label: Text('Disagree')),
                  ButtonSegment(value: 2, label: Text('Pass')),
                ],
                selected: const {0},
              ),
              const SizedBox(height: 8),
              ElevatedButton(
                onPressed: _toggleListening,
                style: ElevatedButton.styleFrom(
                  minimumSize: const Size(double.infinity, 60),
                ),
                child: Text(_isLogging ? 'Stop' : 'Start'),
              ),
              const SizedBox(height: 8),
              Expanded(
                child: TextField(
                  readOnly: true,
                  maxLines: null,
                  controller: TextEditingController(text: _log),
                  style: const TextStyle(color: Colors.black),
                  decoration: InputDecoration(
                    fillColor: Colors.grey[300],
                    filled: true,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
