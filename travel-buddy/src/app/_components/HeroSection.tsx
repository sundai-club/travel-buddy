import React from "react";
import Link from "next/link";

const HeroSection: React.FC = () => {
  return (
    <section className="flex w-full flex-col items-center justify-center bg-gradient-to-r from-purple-500 to-indigo-600 px-4 py-16">
      <div className="container text-center">
        <h1 className="mb-4 text-6xl font-extrabold tracking-tight text-white">
          Welcome to <span className="text-yellow-400">Travel Buddy</span>
        </h1>
        <p className="mb-8 text-lg text-white/80 md:text-xl">
          Your ultimate companion for all your travel adventures.
        </p>
        <Link
          href="#app-integration"
          className="mt-8 rounded-full bg-yellow-400 px-6 py-3 text-lg font-semibold text-black hover:bg-yellow-300"
        >
          Explore the App
        </Link>
      </div>
    </section>
  );
};

export default HeroSection;
