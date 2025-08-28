# AutoGen WebSocket Server

This directory contains the WebSocket server that bridges the React frontend_demo with the AutoGen multi-agent system.

## 🏗️ Architecture

- **serverTest.py**: Simplified AutoGen implementation with only `orchestrator` and `committee_specialist`
- **websocket_server.py**: WebSocket server that handles real-time communication
- **start_server.py**: Startup script for easy server launch

## 🚀 Quick Start

1. **Start Docker Container** (required for ragmcp server):
   ```bash
   cd /Users/tofixjr/Desktop/THESIS/2025_ba_thesis_ysimantob/03_Code
   docker start congressmcp_service
   
   # Or if not built yet:
   # docker-compose up -d
   ```

2. **Install Dependencies** (if not already installed):
   ```bash
   pip install websockets pyyaml openai autogen-ext autogen-agentchat
   ```

3. **Test Docker Connectivity** (optional but recommended):
   ```bash
   python test_docker_connection.py
   ```

4. **Start the WebSocket Server**:
   ```bash
   python start_server.py
   ```
   
   The server will be available at `ws://localhost:8765`

5. **Start the frontend_demo** (in a separate terminal):
   ```bash
   cd ../../frontend_demo
   npm run dev
   ```

6. **Test the Integration**:
   - Open http://localhost:3000
   - Select a company (e.g., ExxonMobil)
   - Look for "AutoGen Connected" status indicator
   - Click "Run Investigation" to start real-time investigation

## 📡 WebSocket API

### Messages from frontend_demo to Server

**Start Investigation:**
```json
{
  "type": "start_investigation",
  "sessionId": "session_123",
  "company": "ExxonMobil", 
  "bill": "hr2307-117"
}
```

**Stop Investigation:**
```json
{
  "type": "stop_investigation",
  "sessionId": "session_123"
}
```

### Messages from Server to frontend_demo

**Agent Communication:**
```json
{
  "type": "agent_communication",
  "sessionId": "session_123",
  "timestamp": "2025-01-16T...",
  "data": {
    "id": "comm_123",
    "agent": "orchestrator",
    "type": "message",
    "simplified": "Starting investigation...",
    "fullContent": "Full message content...",
    "status": "completed"
  }
}
```

**Tool Call Events:**
```json
{
  "type": "tool_call_start",
  "sessionId": "session_123", 
  "timestamp": "2025-01-16T...",
  "data": {
    "id": "tool_123",
    "name": "get_committee_members",
    "arguments": {"bill": "hr2307-117"},
    "agent": "committee_specialist",
    "status": "in_progress"
  }
}
```

## 🔧 Configuration

- **WebSocket Port**: 8765 (configurable in websocket_server.py)
- **AutoGen Agents**: Currently limited to orchestrator + committee_specialist
- **Max Turns**: Limited to 10 for testing (configurable in serverTest.py)

## 🐛 Troubleshooting

**"Server Offline" in frontend_demo:**
- Ensure WebSocket server is running on port 8765
- Check server logs for connection errors
- Verify firewall/proxy settings

**AutoGen Errors:**
- Ensure API keys are properly configured in util/api_util.py
- Check that ragmcp server is running
- Verify agent configurations in config/ directory

**Tool Call Failures:**
- Ensure MCP server (ragmcp) is accessible
- Check tool permissions in FilteredWorkbench setup
- Verify bill/company parameters are valid

## 📝 Development Notes

This is a simplified implementation for testing real-time integration. The full system should include:
- All 6 AutoGen agents (currently only 2)
- Enhanced error handling and recovery
- Session persistence and management
- Authentication and rate limiting
- Monitoring and logging improvements