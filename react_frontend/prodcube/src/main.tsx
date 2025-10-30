import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import UserList from './components/teste'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <UserList></UserList>
  </StrictMode>,
)
