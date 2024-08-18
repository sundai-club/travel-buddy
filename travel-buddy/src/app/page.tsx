import HeroSection from "travel-buddy/app/_components/HeroSection";
import { api, HydrateClient } from "travel-buddy/trpc/server";

export default async function Home() {
  const hello = await api.post.hello({ text: "from tRPC" });

  void api.post.getLatest.prefetch();

  return (
    <HydrateClient>
      <main className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-b from-red-500 to-red-300 text-white">
        {/* Hero Section */}
        <HeroSection />

        {/* Integration Section */}
        <section
          id="app-integration"
          className="container flex flex-col items-center justify-center gap-12 px-4 py-16"
        >
          <iframe
            // todo: replace with actual iframe of the AWS instance
            src="https://your-app-url.com"
            title="Integrated App"
            className="h-screen w-full rounded-xl"
          ></iframe>
        </section>
      </main>
    </HydrateClient>
  );
}
