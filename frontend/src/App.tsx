import { useState, useEffect } from 'react'
import './App.css'

interface ApiStatus {
  status: string
  version: string
}

function App() {
  const [apiStatus, setApiStatus] = useState<ApiStatus | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const response = await fetch('/api/v1/status')
        if (!response.ok) {
          throw new Error('Failed to fetch API status')
        }
        const data = await response.json()
        setApiStatus(data)
        setError(null)
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error')
      } finally {
        setLoading(false)
      }
    }

    fetchStatus()
  }, [])

  return (
    <div className="app">
      <header className="app-header">
        <h1>Truthline</h1>
        <p>Welcome to Truthline</p>
      </header>
      
      <main className="app-main">
        <div className="status-card">
          <h2>API Status</h2>
          {loading && <p>Loading...</p>}
          {error && <p className="error">Error: {error}</p>}
          {apiStatus && (
            <div>
              <p>Status: <strong>{apiStatus.status}</strong></p>
              <p>Version: <strong>{apiStatus.version}</strong></p>
            </div>
          )}
        </div>
      </main>
    </div>
  )
}

export default App

