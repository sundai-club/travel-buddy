import HeroSection from "travel-buddy/app/_components/HeroSection";
import { api, HydrateClient } from "travel-buddy/trpc/server";

export default async function Home() {
  const hello = await api.post.hello({ text: "from tRPC" });

  void api.post.getLatest.prefetch();

  return (
    <HydrateClient>
      <main className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-b from-[#2e026d] to-[#15162c] text-white">
        {/* Hero Section */}
        <HeroSection />

        {/* Integration Section */}
        <section
          id="app-integration"
          className="container flex flex-col items-center justify-center gap-12 px-4 py-16"
        >
          <h2 className="text-4xl font-extrabold text-white">Integrated App</h2>
          <iframe
            src="https://your-app-url.com"
            title="Integrated App"
            className="h-96 w-full rounded-xl border-2 border-white"
          ></iframe>
        </section>
      </main>
    </HydrateClient>
  );
}
