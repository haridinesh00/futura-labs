import { configureStore } from '@reduxjs/toolkit'
import counterfunction from './Slice'
export const store = configureStore({
  reducer: {
    counter:counterfunction,
  },
})