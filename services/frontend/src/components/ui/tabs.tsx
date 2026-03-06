"use client";

import * as React from "react";
import { cn } from "@/lib/utils";

interface TabsProps {
  tabs: string[];
  active: string;
  onChange: (tab: string) => void;
  className?: string;
}

function Tabs({ tabs, active, onChange, className }: TabsProps) {
  return (
    <div className={cn("flex gap-2", className)}>
      {tabs.map((tab) => (
        <button
          key={tab}
          onClick={() => onChange(tab)}
          className={cn(
            "rounded-full px-4 py-2 text-sm font-medium transition-colors",
            active === tab
              ? "bg-primary text-white"
              : "bg-transparent text-gray-500 hover:bg-gray-100"
          )}
        >
          {tab}
        </button>
      ))}
    </div>
  );
}

export { Tabs };
