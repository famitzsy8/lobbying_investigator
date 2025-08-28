# 🏛️ Congressional Lobbying Investigation Dashboard

A beautiful React/Next.js frontend for visualizing multi-agent lobbying investigations based on the AutoGen agent system. Features modern design with subtle gradients, company logos, and interactive elements.

## ✨ Features

### 🎯 Core Investigation Flow  
- **🏢 Company Selection Interface**: Beautiful grid of 10 company boxes with logos and gradients
- **🔄 Seamless Transition**: Companies disappear after selection, revealing investigation dashboard
- **🎨 Brand-Themed Interface**: Each company has custom colors and branding throughout the flow
- **⏱️ Timed Presentation Flow**: Realistic investigation flow with precise timing:
  - Communication appears → 2 seconds → Tool call initiated → 3 seconds → Results obtained (green checkmark) → 2 seconds → Next communication

### 🔧 Tool Call Visualization
- **Nested Tool Call Boxes**: Directory-style nested layout showing tool calls as sub-items under agent communications
- **Loading Indicators**: Active spinning wheels and progress bars during tool execution
- **Compact Grey Design**: Small, unobtrusive tool call boxes that expand to show details
- **Green Success State**: Tool calls turn green with checkmarks when completed
- **Tool Summaries**: Instant summary of what each tool call accomplished

### 📊 Results Display
- **🎨 Notion-Style Final Table**: Stunning, interactive table with gradient headers and hover effects
- **📊 Enhanced Stats Cards**: Gradient-themed statistics boxes with borders and animations
- **🗺️ State Information**: Congressional member state data included in table
- **🔍 Sortable Columns**: Click any column header to sort the investigation results  
- **👤 Member Detail Modals**: Click on any member to see detailed involvement analysis
- **🎯 Visual Indicators**: Party colors, involvement score bars, and ranking badges

### 🎨 Design & User Experience
- **🌈 Subtle Gradients**: Beautiful gradients throughout the interface without being overwhelming
- **🎭 Company Branding**: Each company has custom colors that theme the entire investigation
- **✨ Glass Morphism**: Backdrop blur effects and translucent elements
- **🔄 Smooth Animations**: Hover effects, transitions, and loading states
- **📱 Responsive Design**: Works beautifully on all screen sizes
- **🎯 Expandable Details**: Each communication step has dropdowns showing:
  - Full detailed content from agents
  - Tool calls with arguments and results  
  - Execution timestamps and data point counts

## Architecture

### Components
- `AgentInvestigationDashboard`: Main dashboard component
- `CompanyBillSelector`: Dropdown for selecting company-bill pairs
- `CommunicationTimeline`: Real-time timeline display of agent communications
- `ExpandableStep`: Individual communication step with expandable details

### Services
- `AdvancedMockService`: Advanced simulation with realistic timing and status updates
- `MockAgentService`: Basic simulation (legacy)
- `LLMProcessor`: Placeholder for future LLM processing of agent communications

### Data Files
- `agent-communications.json`: Dummy agent communication data with simplified and full content
- `tool-calls.json`: Dummy tool call and result data based on actual MCP server responses
- `final-table.json`: Investigation results with Congressional member rankings

### Agent Types
- **Orchestrator**: Coordinates the investigation
- **Committee Specialist**: Analyzes committee relationships
- **Bill Specialist**: Examines bill structure and provisions
- **Actions Specialist**: Tracks legislative actions and timeline
- **Amendment Specialist**: Investigates bill amendments
- **Congress Member Specialist**: Analyzes voting patterns and member data

## Running the Application

### Development
```bash
npm install
npm run dev
```
Visit http://localhost:3000

### Docker
```bash
docker-compose up -d
```

### Production Build
```bash
npm run build
npm start
```

## Usage

1. Select a company-bill pair from the dropdown menu
2. Click "Run Investigation" to start the multi-agent analysis
3. Watch real-time agent communications appear in the timeline
4. Each communication shows:
   - Agent type with color coding
   - Communication type (message, tool call, reflection, handoff)
   - Timestamp
   - Detailed content

## Future Enhancements

- Connect to actual AutoGen agent system
- Implement LLM processing for communication simplification
- Add session persistence and history
- Real-time WebSocket integration
- Export investigation reports