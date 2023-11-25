import type { Metadata } from 'next'

import './globals.css'
import { Footer, Navbar } from '@/Components'


export const metadata: Metadata = {
  title: 'Fake News Predictor',
  description: 'Fake News Predictor using Machine Learning',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className='w-full relative'>
        {/* <Navbar /> */}
        {children}
        <Footer />
      </body>
    </html>
  )
}
